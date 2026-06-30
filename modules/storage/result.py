"""Storage selection result for HostGuard."""

from dataclasses import dataclass

from .target import StorageTarget


@dataclass(frozen=True)
class StorageSelection:
    """Describe a selected target and the eligible alternatives."""

    selected_target: StorageTarget
    reason: str
    available_targets: list[StorageTarget]
