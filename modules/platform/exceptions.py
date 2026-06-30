"""Platform-specific exceptions for HostGuard."""


class PlatformError(Exception):
    """Base exception for platform integration failures."""


class CommandExecutionError(PlatformError):
    """Report a failure while executing a platform command."""


class UnsupportedPlatformError(PlatformError):
    """Report that a virtualization platform is unsupported."""
