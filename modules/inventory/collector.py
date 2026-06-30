"""Mock data collector for the HostGuard inventory."""

from .models import HostInfo, NetworkInfo, StorageRepositoryInfo, VMInfo


class InventoryCollector:
    """Return static inventory data without accessing the host."""

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
