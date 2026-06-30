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

### Changed

- Routed direct CLI output through `OutputManager`.
- Consolidated the README architecture documentation.
- Injected a Platform into `InventoryCollector` while preserving mock data.
- Added host UUID and graceful platform-unavailable reporting to Inventory.
