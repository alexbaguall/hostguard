# Laboratory Operations

## Purpose

The laboratory environment is the only appropriate place to evaluate incomplete HostGuard foundations. It must use disposable or non-critical infrastructure and must not contain the sole copy of any virtual machine or backup.

## Current Allowed Evaluation

- CLI informational commands.
- Simulated planning.
- Read-only configured storage inspection.
- The permitted `xe host-list --minimal` query.
- In-memory Job, Workflow, Policy, and Planner validation with test doubles.

## Prohibited Evaluation

Do not attempt snapshots, exports, backup execution, restore, retention, cleanup, or unapproved XE commands. These capabilities are not implemented.

## Lab Checklist

1. Read `docs/CURRENT_STATUS.md`.
2. Confirm the Git revision and configuration under test.
3. Confirm that configured storage paths are non-critical.
4. Capture logs and exact CLI output.
5. Stop on unexpected state.
6. Record findings without changing the host through HostGuard.
