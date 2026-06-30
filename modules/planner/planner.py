"""Read-only Backup Planner for HostGuard."""

from dataclasses import replace
from datetime import datetime
import logging
import secrets

from modules.core.logger import create_logger
from modules.storage import StorageTarget

from .backup_plan import BackupPlan
from .validator import BackupPlanValidator


class BackupPlanner:
    """Generate a declarative backup plan without executing it."""

    def __init__(
        self,
        validator: BackupPlanValidator | None = None,
        logger: logging.Logger | None = None,
    ) -> None:
        """Initialize the planner with validation and logging boundaries."""
        self.validator = validator or BackupPlanValidator()
        self.logger = logger or create_logger()

    def plan_backup(
        self,
        vm_name: str,
        storage_target: StorageTarget,
    ) -> BackupPlan:
        """Generate and validate a simulated backup plan."""
        self.logger.info("Planning started")
        try:
            plan = BackupPlan(
                job_id=self._generate_job_id(),
                vm_uuid="Unknown",
                vm_name=vm_name,
                storage_target=storage_target,
                snapshot_required=False,
                estimated_size=0,
                available_space=storage_target.free_bytes,
                export_filename=f"{vm_name}.xva",
                export_directory=storage_target.path,
                retention=0,
                can_execute=False,
            )
            messages = self.validator.validate(plan)
            return replace(
                plan,
                can_execute=not messages,
                validation_messages=messages,
            )
        finally:
            self.logger.info("Planning finished")

    @staticmethod
    def _generate_job_id() -> str:
        """Generate an identifier for the future backup job."""
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        suffix = secrets.token_hex(2).upper()
        return f"HG-{timestamp}-{suffix}"
