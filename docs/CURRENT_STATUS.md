# Current Project Status

## Release Identity

- **Version:** `0.1.0-dev`
- **Milestone:** Project Identity Documentation
- **Last completed Sprint:** Sprint D2 — HostGuard Manifesto
- **Previous Sprint:** Sprint D1 — Engineering Documentation Foundation
- **Previous engineering Sprint:** Sprint 9 — Backup Planner Foundation
- **Next Sprint:** Not yet defined; an approved specification is required

## Implemented Components

- Python 3 CLI and standard-library Core infrastructure.
- Version, configuration, logger, runtime, context, output, and lock foundations.
- Platform abstraction and bounded CommandRunner.
- Read-only XE host UUID query using only `xe host-list --minimal`.
- Inventory host identity with safe unavailable behavior and simulated resource lists.
- Read-only configured storage discovery and priority selection.
- In-memory Job lifecycle, Job events, and structural EventBus.
- Abstract Workflow, Stage, Task, and WorkflowManager.
- Abstract Policy, PolicyResult, and PolicyManager.
- Declarative BackupPlan generation and storage-only validation.
- Engineering documentation and required AI reading path.
- Project Manifesto governing identity and engineering philosophy.
- Draft RFC-000 defining the mandatory engineering process.

## Pending Components

- Real VM, storage repository, network, and pool inventory.
- Concrete Policies, Workflows, and Tasks.
- Backup execution, snapshot, export, compression, retention, and manifests.
- Integrity hashes and backup verification.
- Restore planning, validation, and execution.
- Monitoring, notifications, scheduling, persistence, and Web UI.
- Production qualification and operational support policy.

## Architecture State

The foundation architecture established through Sprint 9 is frozen. Sprints D1 and D2 change documentation only. Architectural changes require an ADR and an approved implementation specification. `HOSTGUARD_MANIFESTO.md` is the prevailing reference when a technical decision is uncertain.

RFC-000 is in `Draft`. New functionality requires a corresponding RFC in `Approved` before implementation begins.

The implemented system is not production-ready for backup or restore. It can inspect configured storage metadata, create simulated plans, and make one permitted read-only XE host query.

## CLI Status

```text
hostguard version       implemented
hostguard inventory     implemented; partially simulated
hostguard storage       implemented; read-only
hostguard plan [VM]     implemented; simulated planning
hostguard jobs          informational only
hostguard workflows     informational only
hostguard policies      informational only

hostguard backup        not implemented
hostguard doctor        not implemented
hostguard status        not implemented
hostguard verify        not implemented
hostguard restore       not implemented
```

## Roadmap Summary

Foundation, read-only host identity, storage discovery, and planning foundations exist. Backup, validation, restore, monitoring, Web UI, and future platform work require separate specifications. See `docs/ROADMAP.md`.

## Update Requirement

This document must be updated at the end of every future Sprint, including documentation-only Sprints.
