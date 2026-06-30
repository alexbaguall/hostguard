"""Read-only backup plan validation for HostGuard."""

from .backup_plan import BackupPlan


class BackupPlanValidator:
    """Validate only storage readiness for a backup plan."""

    def validate(self, plan: BackupPlan) -> list[str]:
        """Return all storage validation messages for the plan."""
        messages: list[str] = []
        target = plan.storage_target
        if not target.exists:
            messages.append("Storage target does not exist.")
        if not target.mounted:
            messages.append("Storage target is not mounted.")
        if not target.writable:
            messages.append("Storage target is not writable.")
        if plan.available_space <= 0:
            messages.append("Storage target has no available space.")
        return messages
