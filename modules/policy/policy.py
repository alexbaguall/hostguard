"""Abstract decision policy for HostGuard."""

from abc import ABC, abstractmethod

from .result import PolicyResult


class Policy(ABC):
    """Define a side-effect-free business decision contract."""

    name: str
    description: str

    def __init__(self, name: str, description: str) -> None:
        """Initialize policy identity and documentation."""
        self.name = name
        self.description = description

    @abstractmethod
    def validate(self) -> None:
        """Validate the policy definition before evaluation."""

    @abstractmethod
    def evaluate(self) -> PolicyResult:
        """Return a decision without executing any action."""
