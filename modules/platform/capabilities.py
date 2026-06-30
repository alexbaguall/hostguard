"""Platform capability declarations for HostGuard."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Capabilities:
    """Describe optional operations supported by a platform adapter."""

    supports_snapshot: bool = False
    supports_export: bool = False
    supports_import: bool = False
    supports_pool: bool = False
    supports_storage: bool = False
    supports_network: bool = False
