# Backup Strategy

## Current State

HostGuard does not execute backups. The existing Backup Planner creates simulated, declarative plans only.

## Strategic Principles

A future backup strategy must:

- protect VM integrity before optimizing completion rate;
- separate discovery, policy, planning, and execution;
- validate storage before any host action;
- make every important operation a Job within a Workflow;
- emit auditable Events for decisions and state transitions;
- define failure cleanup and reversibility before execution;
- verify backup integrity independently of command success;
- treat restore validation as part of backup quality.

## Unspecified Areas

Snapshot behavior, export format, consistency guarantees, retention, compression, manifests, hashes, encryption, scheduling, and remote storage are not specified. See `docs/specifications/BACKUP_WORKFLOW.md`.
