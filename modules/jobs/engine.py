"""Synchronous in-memory Job Engine for HostGuard."""

from collections.abc import Callable
from typing import Protocol, cast

from .job import Job
from .manager import JobManager


JobCallback = Callable[[], object]


class WorkflowRunner(Protocol):
    """Describe the workflow contract consumed by the Job Engine."""

    name: str
    job: Job | None

    def run(self) -> object:
        """Run the workflow stages."""


class JobEngine:
    """Run a job callback or workflow within a job lifecycle."""

    def __init__(self, manager: JobManager | None = None) -> None:
        """Initialize the engine with a job manager."""
        self.manager = manager or JobManager()

    def run(
        self,
        target: Job | WorkflowRunner,
        callback: JobCallback | None = None,
    ) -> Job:
        """Run a legacy job callback or a workflow."""
        if isinstance(target, Job):
            return self._run_job(target, callback)

        workflow = cast(WorkflowRunner, target)
        if workflow.job is None:
            workflow.job = self.manager.create(
                name=workflow.name,
                module="workflow",
                metadata={"workflow": workflow.name},
            )
        return self._run_job(workflow.job, workflow.run)

    def _run_job(
        self,
        job: Job,
        callback: JobCallback | None,
    ) -> Job:
        """Run the existing in-memory job lifecycle."""
        self.manager.start(job)
        try:
            if callback is not None:
                callback()
        except Exception as error:
            self.manager.fail(job, f"Job Failed: {type(error).__name__}")
            raise
        return self.manager.finish(job)
