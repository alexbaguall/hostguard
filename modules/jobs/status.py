"""Job lifecycle states for HostGuard."""

from enum import Enum


class JobStatus(Enum):
    """Represent the current lifecycle state of a job."""

    CREATED = "CREATED"
    QUEUED = "QUEUED"
    RUNNING = "RUNNING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"
