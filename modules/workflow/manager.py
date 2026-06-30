"""In-memory workflow registry for HostGuard."""

from .exceptions import WorkflowError
from .workflow import Workflow


class WorkflowManager:
    """Register and retrieve workflow definitions in memory."""

    def __init__(self) -> None:
        """Initialize an empty workflow registry."""
        self._workflows: dict[str, Workflow] = {}

    def register(self, workflow: Workflow) -> None:
        """Register a workflow by its unique name."""
        if workflow.name in self._workflows:
            raise WorkflowError(
                f"Workflow '{workflow.name}' is already registered."
            )
        self._workflows[workflow.name] = workflow

    def get(self, name: str) -> Workflow | None:
        """Return a registered workflow or None."""
        return self._workflows.get(name)

    def list(self) -> list[Workflow]:
        """Return registered workflows in insertion order."""
        return list(self._workflows.values())
