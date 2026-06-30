"""Synchronous in-memory Job Engine for HostGuard."""

from collections.abc import Callable

from .job import Job
from .manager import JobManager


JobCallback = Callable[[], object]


class JobEngine:
    """Run a callback within an in-memory job lifecycle."""

    def __init__(self, manager: JobManager | None = None) -> None:
        """Initialize the engine with a job manager."""
        self.manager = manager or JobManager()

    def run(
        self,
        job: Job,
        callback: JobCallback | None = None,
    ) -> Job:
        """Start a job, run its callback, and record the outcome."""
        self.manager.start(job)
        try:
            if callback is not None:
                callback()
        except Exception as error:
            self.manager.fail(job, f"Job Failed: {type(error).__name__}")
            raise
        return self.manager.finish(job)
