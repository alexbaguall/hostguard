"""In-memory job model for HostGuard."""

from dataclasses import dataclass, field
from datetime import datetime

from .event import JobEvent
from .status import JobStatus


@dataclass
class Job:
    """Represent one in-memory HostGuard job."""

    id: str
    name: str
    module: str
    status: JobStatus
    created_at: datetime
    started_at: datetime | None = None
    finished_at: datetime | None = None
    duration: float | None = None
    metadata: dict[str, object] = field(default_factory=dict)
    events: list[JobEvent] = field(default_factory=list)
