"""Collapse same-typed PDDL objects and relax their unary delete effects."""

from __future__ import annotations

import re
from collections.abc import Iterable, Sequence
from dataclasses import dataclass

SExpression = str | list["SExpression"]
ExpressionKey = str | tuple["ExpressionKey", ...]

_PDDL_NAME = re.compile(r"[A-Za-z][A-Za-z0-9_-]*")
_NON_OBJECT_ARGUMENTS = {
    ":metric": frozenset({1}),
    "exists": frozenset({1}),
    "forall": frozenset({1}),
    "is-violated": frozenset({1}),
}


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


@dataclass(frozen=True)
class _Selection:
    objects: tuple[str, ...]
    object_type: str
    abstract_name: str
    replacements: frozenset[str]


def _normalized(value: str) -> str:
    return value.casefold()


def _symbol(value: SExpression) -> str:
    if not isinstance(value, str):
        raise AbstractionError(f"Expected a PDDL symbol, got {value!r}")
    return value


def _expression_key(expression: SExpression) -> ExpressionKey:
    if isinstance(expression, str):
        return _normalized(expression)
    return tuple(_expression_key(item) for item in expression)


def _tokenize(text: str) -> list[str]:
    tokens: list[str] = []
    for line in text.splitlines():
        source = line.split(";", 1)[0]
        tokens.extend(re.findall(r"[()]|[^\s()]+", source))
    return tokens


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
    root = expressions[0]
    if not root or not isinstance(root[0], str) or _normalized(root[0]) != "define":
        raise AbstractionError(f"{label} must start with '(define ...)'")
    return root


def _indent(text: str) -> str:
    return "\n".join(f"  {line}" for line in text.splitlines())


def _render(expression: SExpression) -> str:
    if isinstance(expression, str):
        return expression
    if not expression:
        return "()"
    if all(isinstance(item, str) for item in expression):
        return "(" + " ".join(expression) + ")"
    head, *children = expression
    rendered = [_render(head), *(_indent(_render(child)) for child in children)]
    return "(" + "\n".join(rendered) + "\n)"


def _dump(expression: SExpression) -> str:
    return _render(expression) + "\n"


def _head(expression: SExpression) -> str | None:
    if isinstance(expression, list) and expression and isinstance(expression[0], str):
        return _normalized(expression[0])
    return None


def _find_form(root: Sequence[SExpression], name: str) -> list[SExpression] | None:
    wanted = _normalized(name)
    matches = [child for child in root if isinstance(child, list) and _head(child) == wanted]
    if len(matches) > 1:
        raise AbstractionError(f"Duplicate PDDL section: {name}")
    return matches[0] if matches else None


def _required_form(root: Sequence[SExpression], name: str, label: str) -> list[SExpression]:
    form = _find_form(root, name)
    if form is None:
        raise AbstractionError(f"{label} has no {name} section")
    return form


def _declared_name(root: Sequence[SExpression], section: str, label: str) -> str:
    form = _required_form(root, section, label)
    if len(form) != 2:
        raise AbstractionError(f"Malformed {label.lower()} {section} declaration")
    return _symbol(form[1])


def _typed_symbols(items: Iterable[SExpression], default_type: str = "object") -> list[tuple[str, str]]:
    tokens = list(items)
    result: list[tuple[str, str]] = []
    pending: list[str] = []
    index = 0
    while index < len(tokens):
        token = _symbol(tokens[index])
        if token != "-":
            pending.append(token)
            index += 1
            continue
        if not pending or index + 1 >= len(tokens):
            raise AbstractionError("Malformed typed PDDL symbol list")
        type_name = _symbol(tokens[index + 1])
        result.extend((name, type_name) for name in pending)
        pending.clear()
        index += 2
    result.extend((name, default_type) for name in pending)
    return result


def _declarations(root: Sequence[SExpression], section: str) -> list[tuple[str, str]]:
    form = _find_form(root, section)
    return _typed_symbols(form[1:]) if form is not None else []


def _flatten_typed(declarations: Iterable[tuple[str, str]]) -> list[SExpression]:
    declarations = list(declarations)
    if all(_normalized(type_name) == "object" for _, type_name in declarations):
        return [name for name, _ in declarations]

    result: list[SExpression] = []
    for name, type_name in declarations:
        result.extend((name, "-", type_name))
    return result


def _declaration_map(declarations: Iterable[tuple[str, str]], label: str) -> dict[str, tuple[str, str]]:
    result: dict[str, tuple[str, str]] = {}
    for name, type_name in declarations:
        normalized_name = _normalized(name)
        if normalized_name in result:
            raise AbstractionError(f"Duplicate {label} declaration: {name}")
        result[normalized_name] = (name, type_name)
    return result


def _domain_types(domain: Sequence[SExpression]) -> dict[str, str]:
    parents = {"object": ""}
    for name, parent in _declarations(domain, ":types"):
        normalized_name = _normalized(name)
        if normalized_name in parents:
            raise AbstractionError(f"Duplicate PDDL type: {name}")
        parents[normalized_name] = _normalized(parent)

    for type_name in parents:
        current = type_name
        visited: set[str] = set()
        while current:
            if current in visited:
                raise AbstractionError(f"Cyclic PDDL type hierarchy at {type_name}")
            visited.add(current)
            if current not in parents:
                raise AbstractionError(f"Unknown parent PDDL type: {current}")
            current = parents[current]
    return parents


def _is_subtype(child: str, parent: str, parents: dict[str, str]) -> bool:
    current = _normalized(child)
    target = _normalized(parent)
    while current:
        if current == target:
            return True
        current = parents.get(current, "")
    return False


def _unary_predicates(domain: Sequence[SExpression]) -> set[str]:
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


def _action_field(action: Sequence[SExpression], keyword: str) -> tuple[int, SExpression] | None:
    wanted = _normalized(keyword)
    for index in range(2, len(action)):
        item = action[index]
        if isinstance(item, str) and _normalized(item) == wanted:
            if index + 1 >= len(action):
                action_name = _symbol(action[1]) if len(action) > 1 else "<unknown>"
                raise AbstractionError(f"Action {action_name} has no value for {keyword}")
            return index + 1, action[index + 1]
    return None


def _relax_effect(
    effect: SExpression,
    variables: dict[str, str],
    object_type: str,
    unary_predicates: set[str],
    parents: dict[str, str],
    action_name: str,
    removed: list[RelaxedDelete],
) -> SExpression | None:
    if not isinstance(effect, list) or not effect:
        return effect
    head = _head(effect)

    if head == "and":
        children: list[SExpression] = []
        for child in effect[1:]:
            transformed = _relax_effect(child, variables, object_type, unary_predicates, parents, action_name, removed)
            if transformed is not None:
                children.append(transformed)
        return [effect[0], *children] if children else None

    if head == "when" and len(effect) == 3:
        transformed = _relax_effect(effect[2], variables, object_type, unary_predicates, parents, action_name, removed)
        return [effect[0], effect[1], transformed] if transformed is not None else None

    if head == "forall" and len(effect) == 3 and isinstance(effect[1], list):
        nested_variables = variables | _variable_types(effect[1], parents, f"forall effect in action {action_name}")
        transformed = _relax_effect(
            effect[2], nested_variables, object_type, unary_predicates, parents, action_name, removed
        )
        return [effect[0], effect[1], transformed] if transformed is not None else None

    if head == "not" and len(effect) == 2 and isinstance(effect[1], list):
        literal = effect[1]
        if len(literal) == 2 and _head(literal) in unary_predicates:
            argument = _symbol(literal[1])
            parameter_type = variables.get(_normalized(argument))
            if parameter_type and _is_subtype(object_type, parameter_type, parents):
                removed.append(
                    RelaxedDelete(
                        action=action_name,
                        predicate=_symbol(literal[0]),
                        variable=argument,
                        parameter_type=parameter_type,
                    )
                )
                return None

    return effect


def _variable_types(declarations: Iterable[SExpression], parents: dict[str, str], label: str) -> dict[str, str]:
    result = {_normalized(name): type_name for name, type_name in _typed_symbols(declarations)}
    unknown = sorted({type_name for type_name in result.values() if _normalized(type_name) not in parents})
    if unknown:
        raise AbstractionError(f"Unknown PDDL type {unknown[0]!r} in {label}")
    return result


def _relax_domain(domain: list[SExpression], object_type: str) -> list[RelaxedDelete]:
    parents = _domain_types(domain)
    if _normalized(object_type) not in parents:
        raise AbstractionError(f"Unknown PDDL object type: {object_type}")
    predicates = _unary_predicates(domain)
    removed: list[RelaxedDelete] = []
    for action in domain:
        if not isinstance(action, list) or _head(action) != ":action":
            continue
        if len(action) < 2:
            raise AbstractionError("Action has no name")
        action_name = _symbol(action[1])
        parameter_field = _action_field(action, ":parameters")
        if parameter_field is None:
            parameter_form: SExpression = []
        else:
            _, parameter_form = parameter_field
        if not isinstance(parameter_form, list):
            raise AbstractionError(f"Malformed parameters in action {action_name}")
        variables = _variable_types(parameter_form, parents, f"parameters of action {action_name}")
        effect_field = _action_field(action, ":effect")
        if effect_field is None:
            raise AbstractionError(f"Action {action_name} has no :effect")
        effect_index, effect = effect_field
        transformed = _relax_effect(effect, variables, object_type, predicates, parents, action_name, removed)
        action[effect_index] = transformed if transformed is not None else ["and"]
    return removed


def _validate_task_pair(domain: Sequence[SExpression], problem: Sequence[SExpression]) -> None:
    domain_name = _declared_name(domain, "domain", "Domain")
    _declared_name(problem, "problem", "Problem")
    problem_domain_name = _declared_name(problem, ":domain", "Problem")
    if _normalized(domain_name) != _normalized(problem_domain_name):
        raise AbstractionError(f"Problem references domain {problem_domain_name!r}, " f"not {domain_name!r}")


def _task_declarations(
    domain: Sequence[SExpression], problem: Sequence[SExpression]
) -> tuple[dict[str, tuple[str, str]], dict[str, tuple[str, str]]]:
    problem_objects = _declaration_map(_declarations(problem, ":objects"), "problem object")
    domain_constants = _declaration_map(_declarations(domain, ":constants"), "domain constant")
    duplicate_names = problem_objects.keys() & domain_constants.keys()
    if duplicate_names:
        duplicate = sorted(duplicate_names)[0]
        raise AbstractionError(f"Object {duplicate!r} is declared in both domain and problem")

    parents = _domain_types(domain)
    declarations = [*problem_objects.values(), *domain_constants.values()]
    for name, type_name in declarations:
        if _normalized(type_name) not in parents:
            raise AbstractionError(f"Object {name!r} uses unknown PDDL type {type_name!r}")
    return problem_objects, domain_constants


def _prepare_selection(
    domain: Sequence[SExpression], problem: list[SExpression], objects: Iterable[str], abstract_name: str | None
) -> _Selection:
    object_form = _required_form(problem, ":objects", "Problem")
    object_declarations = _typed_symbols(object_form[1:])
    problem_objects, domain_constants = _task_declarations(domain, problem)

    requested = tuple(dict.fromkeys(_normalized(name) for name in objects))
    if len(requested) < 2:
        raise AbstractionError("At least two distinct objects must be selected")
    missing = [name for name in requested if name not in problem_objects]
    if missing:
        raise AbstractionError(f"Unknown problem objects: {', '.join(missing)}")

    selected_types = {_normalized(problem_objects[name][1]) for name in requested}
    if len(selected_types) != 1:
        raise AbstractionError("Selected objects must have the same declared type")
    object_type = problem_objects[requested[0]][1]
    chosen_name = abstract_name or f"{object_type}_abs"
    if _PDDL_NAME.fullmatch(chosen_name) is None:
        raise AbstractionError(f"Invalid PDDL object name: {chosen_name!r}")
    normalized_abstract_name = _normalized(chosen_name)
    if normalized_abstract_name in domain_constants:
        raise AbstractionError(f"Abstract object name is a domain constant: {chosen_name}")
    if normalized_abstract_name in problem_objects and normalized_abstract_name not in requested:
        raise AbstractionError(f"Abstract object name already exists: {chosen_name}")

    selected_names = tuple(problem_objects[name][0] for name in requested)
    new_declarations: list[tuple[str, str]] = []
    inserted = False
    for name, type_name in object_declarations:
        if _normalized(name) in requested:
            if not inserted:
                new_declarations.append((chosen_name, object_type))
                inserted = True
        else:
            new_declarations.append((name, type_name))
    object_form[:] = [object_form[0], *_flatten_typed(new_declarations)]
    return _Selection(
        objects=selected_names, object_type=object_type, abstract_name=chosen_name, replacements=frozenset(requested)
    )


def _unique(expressions: Iterable[SExpression]) -> list[SExpression]:
    result: list[SExpression] = []
    seen: set[ExpressionKey] = set()
    for expression in expressions:
        key = _expression_key(expression)
        if key not in seen:
            seen.add(key)
            result.append(expression)
    return result


def _rewrite_expression(expression: SExpression, selection: _Selection) -> SExpression:
    if not isinstance(expression, list) or not expression:
        return expression
    rewritten: list[SExpression] = [expression[0]]
    head = _head(expression)
    protected = _NON_OBJECT_ARGUMENTS.get(head, frozenset())
    if head == "preference" and len(expression) == 3:
        protected = frozenset({1})
    for index, child in enumerate(expression[1:], start=1):
        if index in protected:
            rewritten.append(child)
        elif isinstance(child, str):
            rewritten.append(selection.abstract_name if _normalized(child) in selection.replacements else child)
        else:
            rewritten.append(_rewrite_expression(child, selection))
    if _is_false_inequality(rewritten) and not _is_false_inequality(expression):
        raise AbstractionError("Object collapse creates a false '(not (= object object))' constraint")
    if _head(rewritten) == "and":
        return [rewritten[0], *_unique(rewritten[1:])]
    return rewritten


def _is_false_inequality(expression: SExpression) -> bool:
    if not isinstance(expression, list):
        return False
    if _head(expression) == "not" and len(expression) == 2:
        equality = expression[1]
        if isinstance(equality, list) and _head(equality) == "=" and len(equality) == 3:
            return _expression_key(equality[1]) == _expression_key(equality[2])
    return False


def _validate_initial_state(init: Sequence[SExpression]) -> None:
    numeric: dict[ExpressionKey, ExpressionKey] = {}
    positive: set[ExpressionKey] = set()
    negative: set[ExpressionKey] = set()
    for fact in init[1:]:
        if not isinstance(fact, list) or not fact:
            continue
        if _head(fact) == "=" and len(fact) == 3 and isinstance(fact[1], list):
            fluent = _expression_key(fact[1])
            value = _expression_key(fact[2])
            if fluent in numeric and numeric[fluent] != value:
                raise AbstractionError("Object collapse creates conflicting initial values for " f"{_render(fact[1])}")
            numeric[fluent] = value
        elif _head(fact) == "not" and len(fact) == 2:
            negative.add(_expression_key(fact[1]))
        else:
            positive.add(_expression_key(fact))
    if positive & negative:
        raise AbstractionError("Object collapse creates contradictory initial facts")


def _rewrite_problem(problem: list[SExpression], selection: _Selection) -> None:
    excluded_sections = {"problem", ":domain", ":requirements", ":objects"}
    for index, section in enumerate(problem[1:], start=1):
        if not isinstance(section, list) or _head(section) in excluded_sections:
            continue
        rewritten = _rewrite_expression(section, selection)
        if _head(rewritten) == ":init":
            rewritten = [rewritten[0], *_unique(rewritten[1:])]
            _validate_initial_state(rewritten)
        problem[index] = rewritten


def abstract_task(
    domain_text: str, problem_text: str, objects: Iterable[str], abstract_name: str | None = None
) -> AbstractionResult:
    """Collapse one same-typed object set and relax its unary deletes."""
    domain = _parse(domain_text, "domain")
    problem = _parse(problem_text, "problem")
    _validate_task_pair(domain, problem)
    selection = _prepare_selection(domain, problem, objects, abstract_name)
    _rewrite_problem(problem, selection)
    removed = _relax_domain(domain, selection.object_type)
    return AbstractionResult(
        domain_text=_dump(domain),
        problem_text=_dump(problem),
        objects=selection.objects,
        object_type=selection.object_type,
        abstract_name=selection.abstract_name,
        removed_deletes=tuple(removed),
    )


def unary_delete_score(domain_text: str, object_type: str) -> int:
    """Count schema-level unary deletes relaxed for ``object_type``."""
    domain = _parse(domain_text, "domain")
    return len(_relax_domain(domain, object_type))


def rank_symmetry_classes(
    domain_text: str, problem_text: str, classes: Iterable[Iterable[str]]
) -> list[RankedSymmetryClass]:
    """Rank abstractable classes by delete score, size, then object names."""
    domain = _parse(domain_text, "domain")
    problem = _parse(problem_text, "problem")
    _validate_task_pair(domain, problem)
    problem_objects, domain_constants = _task_declarations(domain, problem)
    constant_names = set(domain_constants)
    known_names = set(problem_objects) | constant_names

    ranked: list[RankedSymmetryClass] = []
    scores_by_type: dict[str, int] = {}
    seen_classes: set[frozenset[str]] = set()
    for symmetry_class in classes:
        requested = tuple(sorted(dict.fromkeys(_normalized(name) for name in symmetry_class)))
        class_key = frozenset(requested)
        if len(class_key) < 2 or class_key in seen_classes:
            continue
        seen_classes.add(class_key)
        unknown = class_key - known_names
        if unknown:
            raise AbstractionError(f"PDDL Symmetries returned unknown object {sorted(unknown)[0]!r}")
        if class_key & constant_names:
            continue

        declared = [problem_objects[name] for name in requested]
        types = {_normalized(type_name) for _, type_name in declared}
        if len(types) != 1:
            raise AbstractionError("A symmetry class contains objects of different types")
        object_type = declared[0][1]
        normalized_type = _normalized(object_type)
        if normalized_type not in scores_by_type:
            scores_by_type[normalized_type] = unary_delete_score(domain_text, object_type)
        ranked.append(
            RankedSymmetryClass(
                objects=tuple(name for name, _ in declared),
                object_type=object_type,
                unary_delete_score=scores_by_type[normalized_type],
            )
        )

    ranked.sort(
        key=lambda item: (
            item.unary_delete_score,
            -len(item.objects),
            tuple(_normalized(name) for name in item.objects),
        )
    )
    return ranked
