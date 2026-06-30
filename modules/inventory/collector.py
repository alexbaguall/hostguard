"""Mock data collector for the HostGuard inventory."""

from modules.platform import Platform

from .models import HostInfo, NetworkInfo, StorageRepositoryInfo, VMInfo


class InventoryCollector:
    """Return static inventory data without accessing the host."""

    def __init__(self, platform: Platform) -> None:
        """Initialize the collector with an unused platform boundary."""
        self.platform = platform

    def collect_host(self) -> HostInfo:
        """Return the simulated host information."""
        return HostInfo(
            hostname="localhost",
            platform="Unknown",
            version="Unknown",
        )

    def collect_vms(self) -> list[VMInfo]:
        """Return the simulated virtual machine inventory."""
        return []

    def collect_storage(self) -> list[StorageRepositoryInfo]:
        """Return the simulated storage repository inventory."""
        return []

    def collect_networks(self) -> list[NetworkInfo]:
        """Return the simulated network inventory."""
        return []
