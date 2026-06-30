"""Policy decision result for HostGuard."""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class PolicyResult:
    """Represent a policy decision without performing an action."""

    allowed: bool
    reason: str
    metadata: dict[str, object] = field(default_factory=dict)
