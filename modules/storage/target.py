"""Storage target model for HostGuard."""

from dataclasses import dataclass


@dataclass(frozen=True)
class StorageTarget:
    """Describe one read-only view of a configured storage target."""

    id: str
    path: str
    mounted: bool
    exists: bool
    writable: bool
    filesystem: str
    total_bytes: int
    free_bytes: int
    used_bytes: int
    priority: int
    description: str
