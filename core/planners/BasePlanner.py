"""Domain-specific hooks for the shared abstraction-planning workflow."""

from abc import ABC, abstractmethod

from core.asp import join_asp
from core.execution import get_logger

OCCURRENCE_VALIDATION_CONSTRAINT = ":- occurs(Action, T), not action(Action)."


class BasePlanner(ABC):
    """Base class for domain-specific abstraction mapping and refinement."""

    profile_name = ""
    run_directory = ""
    requires_mapping_arguments = False
    append_concrete_pddl_facts = False

    def validate_configuration(self, abstract_symbol, concrete_objects):
        """Validate domain-specific inputs before planning starts."""
        if self.requires_mapping_arguments and (not abstract_symbol or not concrete_objects):
            raise ValueError(
                "--abstract-symbol and --concrete-objects are required by the " f"{self.profile_name} profile"
            )

    @abstractmethod
    def build_mapping(self, occurrences, abstract_symbol, concrete_objects):
        """Return the concrete mapping for an abstract occurrence sequence."""

    @staticmethod
    def _build_mapping(lines, switch_map, mapping_name):
        logger = get_logger()

        logger.info(f"[MAP] Switches created={len(switch_map)}")
        logger.info("[MAP] Grounded plan:")
        for line in lines:
            logger.info(f"  {line}")
        logger.info(f"[MAP] Mapping implementation={mapping_name}")
        return join_asp(*lines, OCCURRENCE_VALIDATION_CONSTRAINT), switch_map
