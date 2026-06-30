"""Read-only storage discovery and selection for HostGuard."""

from .collector import StorageCollector
from .exceptions import (
    NoStorageAvailable,
    StorageConfigurationError,
    StorageError,
)
from .manager import StorageManager
from .result import StorageSelection
from .selector import StorageSelector
from .target import StorageTarget

__all__ = [
    "NoStorageAvailable",
    "StorageCollector",
    "StorageConfigurationError",
    "StorageError",
    "StorageManager",
    "StorageSelection",
    "StorageSelector",
    "StorageTarget",
]
