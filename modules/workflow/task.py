"""Abstract workflow task for HostGuard."""

from abc import ABC, abstractmethod


class Task(ABC):
    """Define one executable unit within a workflow stage."""

    name: str
    description: str

    def __init__(self, name: str, description: str) -> None:
        """Initialize task identity and documentation."""
        self.name = name
        self.description = description

    @abstractmethod
    def execute(self) -> None:
        """Execute the task."""
