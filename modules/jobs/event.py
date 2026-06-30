"""Job event model for HostGuard."""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True)
class JobEvent:
    """Represent an auditable event in a job lifecycle."""

    timestamp: datetime
    severity: str
    message: str
    data: dict[str, object] = field(default_factory=dict)
