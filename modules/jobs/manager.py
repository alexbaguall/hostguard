"""In-memory job lifecycle management for HostGuard."""

from datetime import datetime
import logging
import secrets

from modules.core.logger import create_logger

from .event import JobEvent
from .event_bus import EventBus
from .job import Job
from .status import JobStatus


class JobManager:
    """Create jobs and manage their in-memory lifecycle state."""

    def __init__(
        self,
        logger: logging.Logger | None = None,
        event_bus: EventBus | None = None,
    ) -> None:
        """Initialize an empty in-memory job registry."""
        self.logger = logger or create_logger()
        self.event_bus = event_bus or EventBus()
        self.jobs: dict[str, Job] = {}

    def create(
        self,
        name: str,
        module: str,
        metadata: dict[str, object] | None = None,
    ) -> Job:
        """Create and retain a job in the CREATED state."""
        job = Job(
            id=self._generate_id(),
            name=name,
            module=module,
            status=JobStatus.CREATED,
            created_at=self._now(),
            metadata=dict(metadata or {}),
        )
        self.jobs[job.id] = job
        self._record(job, "INFO", "Job Created")
        return job

    def start(self, job: Job) -> Job:
        """Move a created job to the RUNNING state."""
        self._require_status(job, JobStatus.CREATED)
        job.status = JobStatus.RUNNING
        job.started_at = self._now()
        self._record(job, "INFO", "Job Started")
        return job

    def finish(self, job: Job) -> Job:
        """Move a running job to the SUCCESS state."""
        self._require_status(job, JobStatus.RUNNING)
        self._complete(job, JobStatus.SUCCESS)
        self._record(job, "INFO", "Job Finished")
        return job

    def fail(self, job: Job, message: str = "Job Failed") -> Job:
        """Move a running job to the FAILED state."""
        self._require_status(job, JobStatus.RUNNING)
        self._complete(job, JobStatus.FAILED)
        self._record(job, "ERROR", message)
        return job

    def cancel(self, job: Job) -> Job:
        """Move a created or running job to the CANCELLED state."""
        if job.status not in (JobStatus.CREATED, JobStatus.RUNNING):
            raise ValueError(f"Cannot cancel job in state {job.status.value}.")
        self._complete(job, JobStatus.CANCELLED)
        self._record(job, "WARNING", "Job Cancelled")
        return job

    def _complete(self, job: Job, status: JobStatus) -> None:
        """Set terminal state, completion time, and duration."""
        job.status = status
        job.finished_at = self._now()
        if job.started_at is not None:
            job.duration = (
                job.finished_at - job.started_at
            ).total_seconds()

    def _record(self, job: Job, severity: str, message: str) -> None:
        """Record and publish one job lifecycle event."""
        event = JobEvent(
            timestamp=self._now(),
            severity=severity,
            message=message,
            data={"job_id": job.id, "status": job.status.value},
        )
        job.events.append(event)
        self.logger.log(
            getattr(logging, severity),
            "%s: job_id=%s status=%s",
            message,
            job.id,
            job.status.value,
        )
        self.event_bus.publish(event)

    @staticmethod
    def _require_status(job: Job, expected: JobStatus) -> None:
        """Require a job to be in the expected state."""
        if job.status is not expected:
            raise ValueError(
                f"Expected job state {expected.value}, "
                f"found {job.status.value}."
            )

    @staticmethod
    def _generate_id() -> str:
        """Generate an identifier in the HostGuard job format."""
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        suffix = secrets.token_hex(2).upper()
        return f"HG-{timestamp}-{suffix}"

    @staticmethod
    def _now() -> datetime:
        """Return the current timezone-aware local time."""
        return datetime.now().astimezone()
