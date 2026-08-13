"""Domain-specific hooks for the shared abstraction-planning workflow."""
from abc import ABC, abstractmethod

from core.asp import write_asp_program
from core.execution import get_logger


class AbstractPlanner(ABC):
    """Base class for domain-specific abstraction mapping and refinement."""

    profile_name = ""
    run_directory = ""
    requires_mapping_arguments = False
    append_concrete_pddl_facts = False

    def validate_configuration(self, abstract_symbol, concrete_objects):
        """Validate domain-specific inputs before planning starts."""
        if self.requires_mapping_arguments and (
            not abstract_symbol or not concrete_objects
        ):
            raise ValueError(
                "--abstract-symbol and --concrete-objects are required by the "
                f"{self.profile_name} profile"
            )

    @abstractmethod
    def build_mapping(self, occurs_path, map_path, abstract_symbol, concrete_objects):
        """Write the concrete mapping for an abstract occurrence sequence."""

    @staticmethod
    def _write_mapping(map_path, lines, switch_map, mapping_name):
        logger = get_logger()
        write_asp_program(map_path, lines)
        logger.info(f"[MAP] Switches created={len(switch_map)}")
        logger.info(f"[FILES] wrote {map_path}")
        logger.info("[MAP] Grounded plan:")
        for line in lines:
            logger.info(f"  {line}")
        logger.info(f"[MAP] Mapping implementation={mapping_name}")
        return switch_map
