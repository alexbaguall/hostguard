"""Storage target selection for HostGuard."""

from collections.abc import Iterable

from .exceptions import NoStorageAvailable
from .result import StorageSelection
from .target import StorageTarget


class StorageSelector:
    """Select the highest-priority eligible storage target."""

    def select(
        self,
        targets: Iterable[StorageTarget],
    ) -> StorageSelection:
        """Select the eligible target with the lowest priority value."""
        available = sorted(
            (
                target
                for target in targets
                if target.exists and target.mounted and target.writable
            ),
            key=lambda target: target.priority,
        )
        if not available:
            raise NoStorageAvailable("No storage targets available.")
        return StorageSelection(
            selected_target=available[0],
            reason="Selected the eligible target with the lowest priority.",
            available_targets=available,
        )
