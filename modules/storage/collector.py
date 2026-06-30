"""Read-only storage target discovery for HostGuard."""

import os
import shutil

from .target import StorageTarget


class StorageCollector:
    """Inspect configured paths using standard read-only filesystem APIs."""

    def collect(
        self,
        target_id: str,
        path: str,
        priority: int,
        description: str = "",
    ) -> StorageTarget:
        """Collect the current state of one configured target."""
        exists = os.path.exists(path)
        mounted = os.path.ismount(path) if exists else False
        writable = os.access(path, os.W_OK) if exists else False
        total_bytes, used_bytes, free_bytes = self._disk_usage(path, exists)
        return StorageTarget(
            id=target_id,
            path=path,
            mounted=mounted,
            exists=exists,
            writable=writable,
            filesystem="Unknown",
            total_bytes=total_bytes,
            free_bytes=free_bytes,
            used_bytes=used_bytes,
            priority=priority,
            description=description,
        )

    @staticmethod
    def _disk_usage(path: str, exists: bool) -> tuple[int, int, int]:
        """Return disk usage or zero values when it is unavailable."""
        if not exists:
            return 0, 0, 0
        try:
            usage = shutil.disk_usage(path)
        except OSError:
            return 0, 0, 0
        return usage.total, usage.used, usage.free
