"""Conservative data collector for the HostGuard inventory."""

from modules.platform import Platform, PlatformError

from .models import HostInfo, NetworkInfo, StorageRepositoryInfo, VMInfo


class InventoryCollector:
    """Collect host identity while retaining simulated resource data."""

    def __init__(self, platform: Platform) -> None:
        """Initialize the collector with a platform boundary."""
        self.platform = platform

    def collect_host(self) -> HostInfo:
        """Return host information or a safe unavailable result."""
        try:
            host = self.platform.get_host()
        except (PlatformError, NotImplementedError):
            return HostInfo(
                hostname="localhost",
                platform="Unknown",
                version="Unknown",
                uuid="Unavailable",
            )

        if not isinstance(host, HostInfo):
            return HostInfo(
                hostname="localhost",
                platform="Unknown",
                version="Unknown",
                uuid="Unavailable",
            )
        return host

    def collect_vms(self) -> list[VMInfo]:
        """Return the simulated virtual machine inventory."""
        return []

    def collect_storage(self) -> list[StorageRepositoryInfo]:
        """Return the simulated storage repository inventory."""
        return []

    def collect_networks(self) -> list[NetworkInfo]:
        """Return the simulated network inventory."""
        return []
