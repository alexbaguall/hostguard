"""Public read-only inventory service for HostGuard."""

from .collector import InventoryCollector
from .models import HostInfo, NetworkInfo, StorageRepositoryInfo, VMInfo


class Inventory:
    """Provide inventory information through a collector boundary."""

    def __init__(self, collector: InventoryCollector | None = None) -> None:
        """Initialize the inventory with a collector."""
        self.collector = collector or InventoryCollector()

    def get_host(self) -> HostInfo:
        """Return host information."""
        return self.collector.collect_host()

    def get_vms(self) -> list[VMInfo]:
        """Return virtual machine information."""
        return self.collector.collect_vms()

    def get_storage(self) -> list[StorageRepositoryInfo]:
        """Return storage repository information."""
        return self.collector.collect_storage()

    def get_networks(self) -> list[NetworkInfo]:
        """Return network information."""
        return self.collector.collect_networks()
