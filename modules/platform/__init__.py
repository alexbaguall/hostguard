"""Platform abstraction interfaces for HostGuard."""

from .capabilities import Capabilities
from .command_runner import CommandResult, CommandRunner
from .exceptions import (
    CommandExecutionError,
    PlatformError,
    UnsupportedPlatformError,
)
from .platform import Platform

__all__ = [
    "Capabilities",
    "CommandExecutionError",
    "CommandResult",
    "CommandRunner",
    "Platform",
    "PlatformError",
    "UnsupportedPlatformError",
]
