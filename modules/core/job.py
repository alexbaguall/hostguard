"""In-memory job management for HostGuard."""

from datetime import datetime
import secrets


class JobManager:
    """Create and retain an in-memory identifier for one execution."""

    def __init__(self) -> None:
        """Create a unique identifier for the current execution."""
        self.job_id = self._generate_id()

    @staticmethod
    def _generate_id() -> str:
        """Generate an identifier in the HostGuard job format."""
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        suffix = secrets.token_hex(2).upper()
        return f"HG-{timestamp}-{suffix}"
