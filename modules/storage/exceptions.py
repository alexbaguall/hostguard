"""Storage-specific exceptions for HostGuard."""


class StorageError(Exception):
    """Base exception for storage discovery and selection failures."""


class NoStorageAvailable(StorageError):
    """Report that no configured storage target is eligible."""


class StorageConfigurationError(StorageError):
    """Report invalid or missing storage target configuration."""
