"""Backup planning result for HostGuard."""

from dataclasses import dataclass, field

from .backup_plan import BackupPlan


@dataclass(frozen=True)
class PlanningResult:
    """Represent the outcome of a backup planning request."""

    success: bool
    plan: BackupPlan | None
    messages: list[str] = field(default_factory=list)
