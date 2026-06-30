"""Command-line interface for HostGuard."""

import argparse
from collections.abc import Sequence

from modules.inventory import Inventory

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
