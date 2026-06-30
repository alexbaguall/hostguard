"""Abstract workflow orchestration for HostGuard."""

from abc import ABC, abstractmethod

from modules.jobs import Job

from .stage import Stage


class Workflow(ABC):
    """Define ordered stages executed within a HostGuard job."""

    name: str
    description: str
    stages: list[Stage]
    job: Job | None

    def __init__(
        self,
        name: str,
        description: str,
        stages: list[Stage] | None = None,
        job: Job | None = None,
    ) -> None:
        """Initialize workflow identity, stages, and optional job."""
        self.name = name
        self.description = description
        self.stages = list(stages or [])
        self.job = job

    def add_stage(self, stage: Stage) -> None:
        """Append a stage to this workflow."""
        self.stages.append(stage)

    def run(self) -> None:
        """Validate and execute each stage in insertion order."""
        self.validate()
        for stage in self.stages:
            stage.run()

    @abstractmethod
    def validate(self) -> None:
        """Validate the workflow definition before execution."""
