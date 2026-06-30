"""Workflow stage orchestration for HostGuard."""

from dataclasses import dataclass, field

from .exceptions import TaskError
from .task import Task


@dataclass
class Stage:
    """Group ordered tasks into one workflow stage."""

    name: str
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Append a task to this stage."""
        self.tasks.append(task)

    def run(self) -> None:
        """Execute each task in insertion order."""
        for task in self.tasks:
            try:
                task.execute()
            except TaskError:
                raise
            except Exception as error:
                raise TaskError(
                    f"Task '{task.name}' failed in stage '{self.name}'."
                ) from error
