"""Backup Planner exceptions for HostGuard."""


class PlannerError(Exception):
    """Base exception for backup planning failures."""


class BackupPlanValidationError(PlannerError):
    """Report an invalid backup plan definition."""
