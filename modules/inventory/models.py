"""Data models for the HostGuard inventory."""

from dataclasses import dataclass


@dataclass(frozen=True)
class HostInfo:
    """Represent read-only host identity information."""

    hostname: str
    platform: str
    version: str
    uuid: str = "Unavailable"


@dataclass(frozen=True)
class PoolInfo:
    """Represent future read-only pool information."""


@dataclass(frozen=True)
class VMInfo:
    """Represent future read-only virtual machine information."""


@dataclass(frozen=True)
class StorageRepositoryInfo:
    """Represent future read-only storage repository information."""


@dataclass(frozen=True)
class NetworkInfo:
    """Represent future read-only network information."""


@dataclass(frozen=True)
class PBDInfo:
    """Represent future read-only physical block device information."""
