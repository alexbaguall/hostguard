"""Conservative XE platform adapter for HostGuard."""

import logging

from modules.inventory.models import HostInfo

from ..command_runner import CommandRunner
from ..exceptions import CommandExecutionError
from ..platform import Platform


class XEPlatform(Platform):
    """Expose the explicitly permitted read-only XE host query."""

    def __init__(
        self,
        runner: CommandRunner | None = None,
        logger: logging.Logger | None = None,
    ) -> None:
        """Initialize the adapter with an injectable command runner."""
        self.runner = runner or CommandRunner(logger)

    def get_host(self) -> HostInfo:
        """Return host information from the permitted XE query."""
        result = self.runner.run(("xe", "host-list", "--minimal"))
        if result.exit_code != 0:
            raise CommandExecutionError(
                f"XE host query failed with exit code {result.exit_code}."
            )

        uuid = result.stdout.strip().split(",", maxsplit=1)[0].strip()
        if not uuid:
            raise CommandExecutionError("XE host query returned no UUID.")

        return HostInfo(
            hostname="localhost",
            platform="XCP-ng",
            version="Unknown",
            uuid=uuid,
        )

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
