"""Declarative backup plan model for HostGuard."""

from dataclasses import dataclass, field

from modules.storage import StorageTarget


@dataclass(frozen=True)
class BackupPlan:
    """Describe a potential backup without executing any operation."""

    job_id: str
    vm_uuid: str
    vm_name: str
    storage_target: StorageTarget
    snapshot_required: bool
    estimated_size: int
    available_space: int
    export_filename: str
    export_directory: str
    retention: int
    can_execute: bool
    validation_messages: list[str] = field(default_factory=list)
