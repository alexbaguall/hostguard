"""Output abstraction for HostGuard."""

import sys
from typing import TextIO


class OutputManager:
    """Write CLI output through a single presentation boundary."""

    def __init__(self, stream: TextIO | None = None) -> None:
        """Initialize output with stdout or an injected text stream."""
        self.stream = stream or sys.stdout

    def write(self, message: str) -> None:
        """Write one plain-text message to the configured stream."""
        print(message, file=self.stream)
