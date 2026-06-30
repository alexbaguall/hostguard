"""Execution context structures for HostGuard."""

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


@dataclass(frozen=True)
class ExecutionContext:
    """Hold identifying information for a HostGuard execution."""

    application_version: str
    hostname: str
    environment: str
    working_directory: Path
    current_user: str
    start_time: datetime
    job_id: str
