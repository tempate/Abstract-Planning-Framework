"""Generic object-set abstraction for typed PDDL tasks."""

from __future__ import annotations

import ast
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Optional, Union

from core.paths import PDDL_SYMMETRIES_TRANSLATOR


SExpression = Union[str, list["SExpression"]]


class AbstractionError(ValueError):
    """Raised when a requested abstraction cannot be constructed safely."""


@dataclass(frozen=True)
class RelaxedDelete:
    action: str
    predicate: str
    variable: str
    parameter_type: str


@dataclass(frozen=True)
class RankedSymmetryClass:
    objects: tuple[str, ...]
    object_type: str
    unary_delete_score: int


@dataclass(frozen=True)
class AbstractionResult:
    domain_text: str
    problem_text: str
    objects: tuple[str, ...]
    object_type: str
    abstract_name: str
    removed_deletes: tuple[RelaxedDelete, ...]

    @property
    def unary_delete_score(self) -> int:
        return len(self.removed_deletes)


def _symbol(value: SExpression) -> str:
    if not isinstance(value, str):
        raise AbstractionError(f"Expected a PDDL symbol, got {value!r}")
    return value


def _normalized(value: str) -> str:
    return value.casefold()


def _tokenize(text: str) -> list[str]:
    return [
        token
        for token in re.findall(r";[^\n\r]*|[()]|[^\s()]+", text)
        if not token.startswith(";")
    ]


def _parse(text: str, label: str) -> list[SExpression]:
    tokens = _tokenize(text)
    position = 0

    def parse_expression() -> SExpression:
        nonlocal position
        if position >= len(tokens):
            raise AbstractionError(f"Unexpected end of {label}")
        token = tokens[position]
        position += 1
        if token == "(":
            result: list[SExpression] = []
            while position < len(tokens) and tokens[position] != ")":
                result.append(parse_expression())
            if position >= len(tokens):
                raise AbstractionError(f"Unclosed list in {label}")
            position += 1
            return result
        if token == ")":
            raise AbstractionError(f"Unexpected ')' in {label}")
        return token

    expressions: list[SExpression] = []
    while position < len(tokens):
        expressions.append(parse_expression())
    if len(expressions) != 1 or not isinstance(expressions[0], list):
        raise AbstractionError(f"{label} must contain one top-level PDDL form")
    return expressions[0]


def _render(expression: SExpression, indent: int = 0) -> str:
    if isinstance(expression, str):
        return expression
    if not expression:
        return "()"
    if all(isinstance(item, str) for item in expression):
        return "(" + " ".join(expression) + ")"

    prefix = " " * indent
    continuation = " " * (indent + 2)
    parts: list[str] = []
    for item in expression:
        rendered = _render(item, indent + 2)
        parts.append(rendered)
    return "(" + parts[0] + "\n" + "\n".join(
        continuation + part.replace("\n", "\n" + continuation)
        for part in parts[1:]
    ) + "\n" + prefix + ")"


def _dump(expression: SExpression) -> str:
    return _render(expression) + "\n"


def _head(expression: SExpression) -> Optional[str]:
    if isinstance(expression, list) and expression and isinstance(expression[0], str):
        return _normalized(expression[0])
    return None


def _find_form(root: list[SExpression], name: str) -> Optional[list[SExpression]]:
    wanted = _normalized(name)
    for child in root:
        if isinstance(child, list) and _head(child) == wanted:
            return child
    return None


def _typed_symbols(
    items: Iterable[SExpression],
    default_type: str = "object",
) -> list[tuple[str, str]]:
    tokens = [_symbol(item) for item in items]
    result: list[tuple[str, str]] = []
    pending: list[str] = []
    index = 0
    while index < len(tokens):
        token = tokens[index]
        if token == "-":
            if not pending or index + 1 >= len(tokens):
                raise AbstractionError("Malformed typed PDDL symbol list")
            type_name = tokens[index + 1]
            result.extend((name, type_name) for name in pending)
            pending = []
            index += 2
        else:
            pending.append(token)
            index += 1
    result.extend((name, default_type) for name in pending)
    return result


def _flatten_typed(symbols: Iterable[tuple[str, str]]) -> list[SExpression]:
    result: list[SExpression] = []
    for name, type_name in symbols:
        result.extend((name, "-", type_name))
    return result


def _domain_types(domain: list[SExpression]) -> dict[str, str]:
    parents = {"object": ""}
    form = _find_form(domain, ":types")
    if form:
        for name, parent in _typed_symbols(form[1:]):
            parents[_normalized(name)] = _normalized(parent)
    return parents


def _is_subtype(child: str, parent: str, parents: dict[str, str]) -> bool:
    current = _normalized(child)
    target = _normalized(parent)
    visited: set[str] = set()
    while current and current not in visited:
        if current == target:
            return True
        visited.add(current)
        current = parents.get(current, "object" if current != "object" else "")
    return False


def _unary_predicates(domain: list[SExpression]) -> set[str]:
    predicates = _find_form(domain, ":predicates")
    if predicates is None:
        return set()
    result = set()
    for declaration in predicates[1:]:
        if not isinstance(declaration, list) or not declaration:
            continue
        arguments = _typed_symbols(declaration[1:])
        if len(arguments) == 1:
            result.add(_normalized(_symbol(declaration[0])))
    return result


def _action_value(
    action: list[SExpression],
    keyword: str,
) -> tuple[int, SExpression]:
    wanted = _normalized(keyword)
    for index, item in enumerate(action[:-1]):
        if isinstance(item, str) and _normalized(item) == wanted:
            return index + 1, action[index + 1]
    raise AbstractionError(f"Action {_symbol(action[1])} has no {keyword}")


def _relax_effect(
    effect: SExpression,
    variables: dict[str, str],
    object_type: str,
    unary_predicates: set[str],
    parents: dict[str, str],
    action_name: str,
    removed: list[RelaxedDelete],
) -> Optional[SExpression]:
    if not isinstance(effect, list) or not effect:
        return effect
    head = _head(effect)

    if head == "and":
        children = []
        for child in effect[1:]:
            transformed = _relax_effect(
                child, variables, object_type, unary_predicates,
                parents, action_name, removed,
            )
            if transformed is not None:
                children.append(transformed)
        return [effect[0], *children] if children else None

    if head == "when" and len(effect) == 3:
        transformed = _relax_effect(
            effect[2], variables, object_type, unary_predicates,
            parents, action_name, removed,
        )
        return [effect[0], effect[1], transformed] if transformed is not None else None

    if head == "forall" and len(effect) == 3 and isinstance(effect[1], list):
        nested_variables = variables.copy()
        nested_variables.update(
            (_normalized(name), type_name)
            for name, type_name in _typed_symbols(effect[1])
        )
        transformed = _relax_effect(
            effect[2], nested_variables, object_type, unary_predicates,
            parents, action_name, removed,
        )
        return [effect[0], effect[1], transformed] if transformed is not None else None

    if head == "not" and len(effect) == 2 and isinstance(effect[1], list):
        literal = effect[1]
        if len(literal) == 2 and _head(literal) in unary_predicates:
            argument = _symbol(literal[1])
            parameter_type = variables.get(_normalized(argument))
            if parameter_type and _is_subtype(object_type, parameter_type, parents):
                removed.append(RelaxedDelete(
                    action=action_name,
                    predicate=_symbol(literal[0]),
                    variable=argument,
                    parameter_type=parameter_type,
                ))
                return None

    return effect


def _relax_domain(
    domain: list[SExpression],
    object_type: str,
) -> tuple[list[SExpression], list[RelaxedDelete]]:
    parents = _domain_types(domain)
    predicates = _unary_predicates(domain)
    removed: list[RelaxedDelete] = []
    for form in domain:
        if not isinstance(form, list) or _head(form) != ":action":
            continue
        action_name = _symbol(form[1])
        _, parameter_form = _action_value(form, ":parameters")
        if not isinstance(parameter_form, list):
            raise AbstractionError(f"Malformed parameters in action {action_name}")
        variables = {
            _normalized(name): type_name
            for name, type_name in _typed_symbols(parameter_form)
        }
        effect_index, effect = _action_value(form, ":effect")
        transformed = _relax_effect(
            effect, variables, object_type, predicates, parents,
            action_name, removed,
        )
        form[effect_index] = transformed if transformed is not None else ["and"]
    return domain, removed


def _replace_arguments(
    expression: SExpression,
    replacements: set[str],
    abstract_name: str,
) -> SExpression:
    if not isinstance(expression, list):
        return expression
    result: list[SExpression] = []
    for index, child in enumerate(expression):
        if index > 0 and isinstance(child, str) and _normalized(child) in replacements:
            result.append(abstract_name)
        elif isinstance(child, list):
            result.append(_replace_arguments(child, replacements, abstract_name))
        else:
            result.append(child)
    return result


def _deduplicate_conjunctions(expression: SExpression) -> SExpression:
    if not isinstance(expression, list):
        return expression
    children = [_deduplicate_conjunctions(child) for child in expression[1:]]
    if _head(expression) != "and":
        return [expression[0], *children] if expression else expression
    seen: set[str] = set()
    unique: list[SExpression] = []
    for child in children:
        key = repr(child).casefold()
        if key not in seen:
            seen.add(key)
            unique.append(child)
    return [expression[0], *unique]


def _validate_initial_state(init: list[SExpression]) -> None:
    numeric: dict[str, str] = {}
    positive: set[str] = set()
    negative: set[str] = set()
    for fact in init[1:]:
        if not isinstance(fact, list) or not fact:
            continue
        if _head(fact) == "=" and len(fact) == 3 and isinstance(fact[1], list):
            fluent = repr(fact[1]).casefold()
            value = repr(fact[2]).casefold()
            if fluent in numeric and numeric[fluent] != value:
                raise AbstractionError(
                    "Object collapse creates conflicting initial values for "
                    f"{_render(fact[1])}"
                )
            numeric[fluent] = value
        elif _head(fact) == "not" and len(fact) == 2:
            negative.add(repr(fact[1]).casefold())
        else:
            positive.add(repr(fact).casefold())
    conflicts = positive & negative
    if conflicts:
        raise AbstractionError("Object collapse creates contradictory initial facts")


def _problem_objects(
    problem: list[SExpression],
) -> tuple[list[SExpression], list[tuple[str, str]]]:
    form = _find_form(problem, ":objects")
    if form is None:
        raise AbstractionError("Problem has no :objects section")
    return form, _typed_symbols(form[1:])


def _prepare_selection(
    problem: list[SExpression], objects: Iterable[str], abstract_name: Optional[str],
) -> tuple[list[SExpression], tuple[str, ...], str, str, set[str]]:
    object_form, declarations = _problem_objects(problem)
    by_name = {_normalized(name): (name, type_name) for name, type_name in declarations}
    requested = tuple(dict.fromkeys(_normalized(name) for name in objects))
    if len(requested) < 2:
        raise AbstractionError("At least two distinct objects must be selected")
    missing = [name for name in requested if name not in by_name]
    if missing:
        raise AbstractionError(f"Unknown problem objects: {', '.join(missing)}")
    types = {_normalized(by_name[name][1]) for name in requested}
    if len(types) != 1:
        raise AbstractionError("Selected objects must have the same declared type")
    object_type = by_name[requested[0]][1]
    chosen_name = abstract_name or f"{object_type}_abs"
    if not re.fullmatch(r"[^\s();]+", chosen_name) or chosen_name.startswith("?"):
        raise AbstractionError(f"Invalid PDDL object name: {chosen_name!r}")
    if _normalized(chosen_name) in by_name and _normalized(chosen_name) not in requested:
        raise AbstractionError(f"Abstract object name already exists: {chosen_name}")

    selected_names = tuple(by_name[name][0] for name in requested)
    new_declarations: list[tuple[str, str]] = []
    inserted = False
    for name, type_name in declarations:
        if _normalized(name) in requested:
            if not inserted:
                new_declarations.append((chosen_name, object_type))
                inserted = True
        else:
            new_declarations.append((name, type_name))
    object_form[:] = [object_form[0], *_flatten_typed(new_declarations)]
    return object_form, selected_names, object_type, chosen_name, set(requested)


def abstract_task(
    domain_text: str,
    problem_text: str,
    objects: Iterable[str],
    abstract_name: Optional[str] = None,
) -> AbstractionResult:
    """Collapse one same-typed object set and relax its unary deletes."""
    domain = _parse(domain_text, "domain")
    problem = _parse(problem_text, "problem")
    _, selected, object_type, chosen_name, replacements = _prepare_selection(
        problem, objects, abstract_name,
    )

    excluded_sections = {"problem", ":domain", ":requirements", ":objects"}
    for section in problem[1:]:
        if not isinstance(section, list) or _head(section) in excluded_sections:
            continue
        for index in range(1, len(section)):
            section[index] = _replace_arguments(section[index], replacements, chosen_name)
            section[index] = _deduplicate_conjunctions(section[index])
        if _head(section) == ":init":
            seen: set[str] = set()
            unique = []
            for fact in section[1:]:
                key = repr(fact).casefold()
                if key not in seen:
                    seen.add(key)
                    unique.append(fact)
            section[:] = [section[0], *unique]
            _validate_initial_state(section)

    domain, removed = _relax_domain(domain, object_type)
    return AbstractionResult(
        domain_text=_dump(domain),
        problem_text=_dump(problem),
        objects=selected,
        object_type=object_type,
        abstract_name=chosen_name,
        removed_deletes=tuple(removed),
    )


def unary_delete_score(domain_text: str, object_type: str) -> int:
    """Count schema-level unary deletes relaxed for ``object_type``."""
    domain = _parse(domain_text, "domain")
    _, removed = _relax_domain(domain, object_type)
    return len(removed)


def _object_type_map(problem_text: str) -> dict[str, tuple[str, str]]:
    problem = _parse(problem_text, "problem")
    _, declarations = _problem_objects(problem)
    return {_normalized(name): (name, type_name) for name, type_name in declarations}


def rank_symmetry_classes(
    domain_text: str,
    problem_text: str,
    classes: Iterable[Iterable[str]],
) -> list[RankedSymmetryClass]:
    """Rank classes by delete score, decreasing size, then object names."""
    declarations = _object_type_map(problem_text)
    ranked: list[RankedSymmetryClass] = []
    scores_by_type: dict[str, int] = {}
    for symmetry_class in classes:
        requested = tuple(sorted(dict.fromkeys(symmetry_class), key=str.casefold))
        if len(requested) < 2:
            continue
        try:
            declared = [declarations[_normalized(name)] for name in requested]
        except KeyError as error:
            raise AbstractionError(
                f"PDDL Symmetries returned unknown object {error.args[0]!r}"
            ) from error
        types = {_normalized(type_name) for _, type_name in declared}
        if len(types) != 1:
            raise AbstractionError("A symmetry class contains objects of different types")
        object_type = declared[0][1]
        normalized_type = _normalized(object_type)
        if normalized_type not in scores_by_type:
            scores_by_type[normalized_type] = unary_delete_score(
                domain_text, object_type,
            )
        ranked.append(RankedSymmetryClass(
            objects=tuple(name for name, _ in declared),
            object_type=object_type,
            unary_delete_score=scores_by_type[normalized_type],
        ))
    ranked.sort(key=lambda item: (
        item.unary_delete_score,
        -len(item.objects),
        tuple(_normalized(name) for name in item.objects),
    ))
    return ranked


def find_symmetric_object_sets(
    domain_path: Union[str, Path],
    problem_path: Union[str, Path],
    time_limit: int = 300,
    translator_path: Union[str, Path] = PDDL_SYMMETRIES_TRANSLATOR,
) -> list[list[str]]:
    """Run the pinned PDDL Symmetries translator and return object classes."""
    translator = Path(translator_path)
    if not translator.is_file():
        raise RuntimeError(
            "PDDL Symmetries is not initialized. Run "
            "'git submodule update --init --recursive'."
        )
    command = [
        sys.executable,
        str(translator),
        str(Path(domain_path).resolve()),
        str(Path(problem_path).resolve()),
        "--compute-symmetries",
        "--only-object-symmetries",
        "--compute-symmetric-object-sets-from-symmetries",
        "--bliss-time-limit", str(time_limit),
        "--stop-after-computing-symmetries",
    ]
    try:
        result = subprocess.run(
            command,
            cwd=translator.parent,
            capture_output=True,
            text=True,
            timeout=time_limit + 30,
        )
    except subprocess.TimeoutExpired as error:
        raise RuntimeError(
            f"PDDL Symmetries exceeded its {time_limit}-second limit"
        ) from error
    if result.returncode != 0:
        diagnostics = "\n".join(
            value.strip() for value in (result.stdout, result.stderr) if value.strip()
        )
        raise RuntimeError(
            f"PDDL Symmetries failed with exit code {result.returncode}:\n{diagnostics}"
        )
    match = re.search(
        r"^Non-trivial symmetric object sets:\s*(.+)$",
        result.stdout,
        flags=re.MULTILINE,
    )
    if not match:
        raise RuntimeError("PDDL Symmetries did not report symmetric object sets")
    try:
        classes = ast.literal_eval(match.group(1))
    except (SyntaxError, ValueError) as error:
        raise RuntimeError("PDDL Symmetries returned malformed object sets") from error
    if not isinstance(classes, list) or not all(
        isinstance(group, list) and all(isinstance(item, str) for item in group)
        for group in classes
    ):
        raise RuntimeError("PDDL Symmetries returned an invalid object-set value")
    return classes
