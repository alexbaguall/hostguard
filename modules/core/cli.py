"""Command-line interface for HostGuard."""

import argparse
from collections.abc import Sequence

from modules.inventory import Inventory
from modules.storage import (
    NoStorageAvailable,
    StorageError,
    StorageManager,
)

from .output import OutputManager
from .version import Version


NOT_IMPLEMENTED_MESSAGE = "Module not implemented yet."


def build_parser() -> argparse.ArgumentParser:
    """Build and return the HostGuard argument parser."""
    parser = argparse.ArgumentParser(
        prog="hostguard",
        description="Conservative administration platform for XCP-ng hosts.",
    )
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("version", help="Display the HostGuard version.")
    subparsers.add_parser(
        "inventory",
        help="Display the read-only host inventory.",
    )
    subparsers.add_parser(
        "jobs",
        help="Display active HostGuard jobs.",
    )
    subparsers.add_parser(
        "workflows",
        help="Display available HostGuard workflows.",
    )
    subparsers.add_parser(
        "policies",
        help="Display registered HostGuard policies.",
    )
    subparsers.add_parser(
        "storage",
        help="Display configured storage targets.",
    )
    for command in ("doctor", "backup", "status", "verify", "restore"):
        subparsers.add_parser(
            command,
            help=f"Access the future {command} module.",
        )

    return parser


def main(arguments: Sequence[str] | None = None) -> int:
    """Run the HostGuard command-line interface."""
    parser = build_parser()
    namespace = parser.parse_args(arguments)
    output = OutputManager()

    if namespace.command == "version":
        output.write(Version().value)
        return 0

    if namespace.command == "inventory":
        output.write(format_inventory(Inventory()))
        return 0

    if namespace.command == "jobs":
        output.write("HostGuard Jobs\n\nNo jobs running.")
        return 0

    if namespace.command == "workflows":
        output.write("Available Workflows\n\nNone")
        return 0

    if namespace.command == "policies":
        output.write("Registered Policies\n\nNone")
        return 0

    if namespace.command == "storage":
        try:
            output.write(format_storage(StorageManager()))
        except StorageError:
            output.write(
                "HostGuard Storage\n\nNo storage targets available."
            )
        return 0

    if namespace.command is None:
        parser.print_help()
        return 0

    output.write(NOT_IMPLEMENTED_MESSAGE)
    return 0


def format_inventory(inventory: Inventory) -> str:
    """Format the current inventory for plain-text CLI output."""
    host = inventory.get_host()
    sections = [
        "HostGuard Inventory",
        f"Host:\n{host.hostname}",
        f"Host UUID:\n{host.uuid}",
        f"Platform:\n{host.platform}",
        f"Version:\n{host.version}",
        f"VMs:\n{len(inventory.get_vms())}",
        f"Storages:\n{len(inventory.get_storage())}",
        f"Networks:\n{len(inventory.get_networks())}",
    ]
    if host.uuid == "Unavailable":
        sections.append("Platform unavailable.")
    return "\n\n".join(sections)


def format_storage(manager: StorageManager) -> str:
    """Format discovered storage targets and the selected destination."""
    targets = manager.list_targets()
    try:
        selection = manager.select_target()
    except NoStorageAvailable:
        return "HostGuard Storage\n\nNo storage targets available."

    lines = [
        f"{'ID':<16}{'Mounted':<10}{'Writable':<11}Free",
    ]
    lines.extend(
        f"{target.id:<16}"
        f"{_yes_no(target.mounted):<10}"
        f"{_yes_no(target.writable):<11}"
        f"{_format_bytes(target.free_bytes)}"
        for target in targets
    )
    return "\n\n".join(
        (
            "HostGuard Storage",
            "\n".join(lines),
            f"Selected:\n\n{selection.selected_target.id}",
        )
    )


def _yes_no(value: bool) -> str:
    """Format a boolean for the storage table."""
    return "Yes" if value else "No"


def _format_bytes(value: int) -> str:
    """Format a byte count with a compact binary unit."""
    amount = float(value)
    for unit in ("B", "KB", "MB", "GB"):
        if amount < 1024:
            return f"{amount:.1f} {unit}"
        amount /= 1024
    return f"{amount:.1f} TB"
