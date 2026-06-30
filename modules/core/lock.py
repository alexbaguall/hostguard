"""In-memory execution lock state for HostGuard."""


class LockManager:
    """Track whether an execution is active in the current process."""

    def __init__(self) -> None:
        """Initialize the manager with no active execution."""
        self._execution_in_progress = False

    def is_execution_in_progress(self) -> bool:
        """Return whether an execution is currently marked as active."""
        return self._execution_in_progress

    def set_execution_in_progress(self, active: bool) -> None:
        """Update the in-memory execution state."""
        self._execution_in_progress = active
