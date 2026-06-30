# Changelog

All notable changes to HostGuard will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Initial project directory structure.
- Minimal `hostguard` executable with project and module information.
- Foundational project documentation.
- Version identifier for the `0.1.0-dev` development release.
- Python command-line parser and core infrastructure.
- Configuration, logging, runtime, job, lock, and version components.
- Platform Layer package boundary with an empty XE integration package.
- Schema contract documentation and Architecture Decision Records.
- Project principles defining mandatory safety and operational behavior.
- Execution context, event interfaces, and centralized output structure.
- Read-only Inventory Engine with typed data models and mock collection.
- `inventory` CLI command for displaying simulated inventory information.
- Abstract Platform interface and unimplemented XE adapter.
- Platform capabilities, command runner boundary, and exceptions.
- Bounded command execution with typed captured results and audit logging.
- Read-only XCP-ng host UUID discovery.
- In-memory Job Engine, lifecycle manager, status enum, and job events.
- Structural Job Engine event bus and `jobs` CLI command.
- Abstract Workflow Engine with stage, task, registry, and exceptions.
- Workflow execution support in the Job Engine and `workflows` CLI command.
- Abstract Policy Engine, typed decision results, and policy registry.
- Optional Workflow policy registry integration and `policies` CLI command.
- Read-only storage target discovery, selection, and typed results.
- Multi-target storage configuration and `storage` CLI command.
- Declarative Backup Planner, plan validation, and typed planning results.
- Simulated `plan` CLI command without backup execution.

### Changed

- Routed direct CLI output through `OutputManager`.
- Consolidated the README architecture documentation.
- Injected a Platform into `InventoryCollector` while preserving mock data.
- Added host UUID and graceful platform-unavailable reporting to Inventory.
