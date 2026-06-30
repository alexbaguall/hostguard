# Architecture Decision Log

This chronological log summarizes significant project decisions. ADRs remain the authoritative record for decisions that require full context and consequence analysis.

## Milestone 0 — Initial Structure

- Established HostGuard as a conservative XCP-ng/XenServer administration platform rather than a backup script.
- Prohibited automatic dependencies, host configuration changes, and unnecessary functionality.
- Adopted a modular repository structure.

## Sprint 1 — Python Core

- Selected Python 3 and the standard library for the Core.
- Added CLI, version, logger, configuration, runtime, job identity, and lock foundations.
- Recorded the language decision in ADR 0001.

## Sprint 1.1 — Architecture Consolidation

- Introduced the Platform Layer, schemas location, ADR practice, execution context, event interfaces, centralized output, and project principles.

## Sprint 2 — Inventory Boundary

- Made Inventory the intended single source of host information.
- Began with simulated data and typed inventory models.

## Sprint 3 — Platform Abstraction

- Defined the abstract Platform contract, capabilities, platform exceptions, and CommandRunner boundary.
- Required InventoryCollector to receive a Platform.

## Sprint 4 — First Host Communication

- Authorized exactly one read-only XE command: `xe host-list --minimal`.
- Isolated subprocess usage in CommandRunner with timeout, captured output, and error conversion.

## Sprint 5 — Job Engine

- Established in-memory Job states, lifecycle events, manager, and synchronous engine.
- Deferred persistence, queues, and concurrency.

## Sprint 6 — Workflow Engine

- Established abstract Workflow and Task contracts, Stage ordering, registry, and Job Engine integration.
- Deferred all concrete Workflows.

## Sprint 7 — Policy Engine

- Established side-effect-free Policy decisions and typed PolicyResult values.
- Prepared Workflow for policy access without evaluating policies.

## Sprint 8 — Storage Manager

- Authorized read-only filesystem inspection using four standard-library APIs.
- Selected eligible targets by the lowest numeric priority.
- Deferred storage creation, minimum-space policy, and network storage protocols.

## Sprint 9 — Backup Planner

- Established declarative BackupPlan generation with simulated VM data.
- Limited validation to storage readiness.
- Deferred all backup, snapshot, export, manifest, hash, and retention behavior.

## Sprint D1 — Documentation Foundation

- Made repository documentation the permanent project knowledge base.
- Established mandatory AI reading order, status tracking, engineering guidance, operations documentation, and the decision log.
- Froze the existing foundation architecture pending an approved ADR and implementation specification.
