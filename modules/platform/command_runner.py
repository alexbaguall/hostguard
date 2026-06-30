"""Conservative system command execution for HostGuard."""

from collections.abc import Sequence
from dataclasses import dataclass
import logging
import shlex
import subprocess
import time

from modules.core.logger import create_logger

from .exceptions import CommandExecutionError


@dataclass(frozen=True)
class CommandResult:
    """Contain the captured result of one system command."""

    stdout: str
    stderr: str
    exit_code: int
    execution_time: float


class CommandRunner:
    """Execute a command with bounded, captured, non-shell semantics."""

    def __init__(self, logger: logging.Logger | None = None) -> None:
        """Initialize the runner with a HostGuard logger."""
        self.logger = logger or create_logger()

    def run(self, command: Sequence[str]) -> CommandResult:
        """Execute a command and return its captured result."""
        command_args = list(command)
        command_text = shlex.join(command_args)
        self.logger.info("Executing command: %s", command_text)
        started_at = time.monotonic()

        try:
            completed = subprocess.run(
                command_args,
                timeout=30,
                capture_output=True,
                text=True,
                check=False,
            )
        except (OSError, subprocess.SubprocessError) as error:
            execution_time = time.monotonic() - started_at
            self._log_failure(command_text, execution_time, error)
            raise CommandExecutionError(
                f"Command could not be executed: {command_text}"
            ) from None

        execution_time = time.monotonic() - started_at
        self.logger.info(
            "Command completed: command=%s execution_time=%.3fs exit_code=%d",
            command_text,
            execution_time,
            completed.returncode,
        )
        return CommandResult(
            stdout=completed.stdout,
            stderr=completed.stderr,
            exit_code=completed.returncode,
            execution_time=execution_time,
        )

    def _log_failure(
        self,
        command: str,
        execution_time: float,
        error: Exception,
    ) -> None:
        """Log a command failure without logging captured output."""
        self.logger.error(
            "Command failed: command=%s execution_time=%.3fs "
            "exit_code=unavailable error=%s",
            command,
            execution_time,
            type(error).__name__,
        )
