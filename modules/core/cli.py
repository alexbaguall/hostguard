"""Command-line interface for HostGuard."""

import argparse
from collections.abc import Sequence

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

    if namespace.command is None:
        parser.print_help()
        return 0

    output.write(NOT_IMPLEMENTED_MESSAGE)
    return 0
