"""In-memory policy registry for HostGuard."""

from .exceptions import PolicyError
from .policy import Policy


class PolicyManager:
    """Register and retrieve policy definitions in memory."""

    def __init__(self) -> None:
        """Initialize an empty policy registry."""
        self._policies: dict[str, Policy] = {}

    def register(self, policy: Policy) -> None:
        """Register a policy by its unique name."""
        if policy.name in self._policies:
            raise PolicyError(
                f"Policy '{policy.name}' is already registered."
            )
        self._policies[policy.name] = policy

    def get(self, name: str) -> Policy | None:
        """Return a registered policy or None."""
        return self._policies.get(name)

    def list(self) -> list[Policy]:
        """Return registered policies in insertion order."""
        return list(self._policies.values())
