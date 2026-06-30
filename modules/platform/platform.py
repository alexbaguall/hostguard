"""Abstract virtualization platform interface for HostGuard."""

from abc import ABC, abstractmethod


class Platform(ABC):
    """Define read-only information exposed by a platform adapter."""

    @abstractmethod
    def get_host(self) -> object:
        """Return platform-specific host information."""

    @abstractmethod
    def get_vms(self) -> list[object]:
        """Return platform-specific virtual machine information."""

    @abstractmethod
    def get_storage(self) -> list[object]:
        """Return platform-specific storage information."""

    @abstractmethod
    def get_networks(self) -> list[object]:
        """Return platform-specific network information."""

    @abstractmethod
    def get_pool(self) -> object:
        """Return platform-specific pool information."""

    @abstractmethod
    def get_version(self) -> str:
        """Return the platform version."""
