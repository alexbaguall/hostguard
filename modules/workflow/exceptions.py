"""Workflow-specific exceptions for HostGuard."""


class WorkflowError(Exception):
    """Base exception for workflow orchestration failures."""


class StageError(WorkflowError):
    """Report a failure while running a workflow stage."""


class TaskError(StageError):
    """Report a failure while executing a workflow task."""
