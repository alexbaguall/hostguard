"""Unimplemented XE platform adapter for HostGuard."""

from ..platform import Platform


class XEPlatform(Platform):
    """Define the future XE adapter without communicating with a host."""

    def get_host(self) -> object:
        """Reject host discovery until the XE adapter is implemented."""
        raise NotImplementedError("XE host discovery is not implemented.")

    def get_vms(self) -> list[object]:
        """Reject VM discovery until the XE adapter is implemented."""
        raise NotImplementedError("XE VM discovery is not implemented.")

    def get_storage(self) -> list[object]:
        """Reject storage discovery until the XE adapter is implemented."""
        raise NotImplementedError("XE storage discovery is not implemented.")

    def get_networks(self) -> list[object]:
        """Reject network discovery until the XE adapter is implemented."""
        raise NotImplementedError("XE network discovery is not implemented.")

    def get_pool(self) -> object:
        """Reject pool discovery until the XE adapter is implemented."""
        raise NotImplementedError("XE pool discovery is not implemented.")

    def get_version(self) -> str:
        """Reject version discovery until the XE adapter is implemented."""
        raise NotImplementedError("XE version discovery is not implemented.")
