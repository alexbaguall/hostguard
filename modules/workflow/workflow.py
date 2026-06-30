"""Abstract workflow orchestration for HostGuard."""

from abc import ABC, abstractmethod

from modules.jobs import Job
from modules.policy import PolicyManager

from .stage import Stage


class Workflow(ABC):
    """Define ordered stages executed within a HostGuard job."""

    name: str
    description: str
    stages: list[Stage]
    job: Job | None
    policy_manager: PolicyManager | None

    def __init__(
        self,
        name: str,
        description: str,
        stages: list[Stage] | None = None,
        job: Job | None = None,
        policy_manager: PolicyManager | None = None,
    ) -> None:
        """Initialize workflow structure and optional integrations."""
        self.name = name
        self.description = description
        self.stages = list(stages or [])
        self.job = job
        self.policy_manager = policy_manager

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
