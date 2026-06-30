"""Policy-specific exceptions for HostGuard."""


class PolicyError(Exception):
    """Base exception for policy decision failures."""


class PolicyValidationError(PolicyError):
    """Report an invalid policy definition or evaluation context."""
