# Testing Strategy

## Current State

The repository contains test directory placeholders but no committed automated test suite. Manual validation has used injected collaborators and in-memory data.

## Testing Priorities

1. Pure model and validator tests.
2. Job and Workflow lifecycle tests.
3. Policy decision contract tests.
4. Storage discovery tests with mocked filesystem APIs.
5. Planner tests with simulated targets.
6. CommandRunner tests with mocked `subprocess.run`.
7. XE adapter parsing and failure conversion tests.
8. Exact CLI output and exit-code tests.

## Safety Requirements

Automated tests must not contact a real host by default. Platform, command, filesystem, and time boundaries should be injected or patched. Any integration test that invokes XE must be separately marked, explicitly authorized, and limited to approved read-only commands.

## Acceptance Discipline

Each Sprint should add tests proportional to its behavior. Tests must cover safe failure paths, not only successful paths. A passing test suite never authorizes functionality outside the current specification.
