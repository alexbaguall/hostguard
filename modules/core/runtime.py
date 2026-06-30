"""Runtime information collection for HostGuard."""

from datetime import datetime
import getpass
import os
from pathlib import Path
import platform
import socket


class Runtime:
    """Collect immutable information about the current execution."""

    def __init__(self) -> None:
        """Collect runtime information without changing the host."""
        self.application_start_time = datetime.now().astimezone()
        self.hostname = socket.gethostname()
        self.python_version = platform.python_version()
        self.operating_system = platform.platform()
        self.current_user = getpass.getuser()
        self.working_directory = Path.cwd()

    def as_dict(self) -> dict[str, str]:
        """Return runtime information as display-safe strings."""
        return {
            "application_start_time": self.application_start_time.isoformat(),
            "hostname": self.hostname,
            "python_version": self.python_version,
            "operating_system": self.operating_system,
            "current_user": self.current_user,
            "working_directory": os.fspath(self.working_directory),
        }
