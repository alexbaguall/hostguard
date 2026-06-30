"""Future system command boundary for HostGuard."""

class CommandRunner:
    """Define the boundary for future command execution."""

    def run(self) -> None:
        """Reject command execution until a later implementation."""
        raise NotImplementedError("Command execution is not implemented.")
