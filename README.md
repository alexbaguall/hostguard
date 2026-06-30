# HostGuard

## Overview

HostGuard is a modular administration platform for XCP-ng and XenServer hosts. It is designed around conservative operations: virtual machines must never be placed at risk, host settings must not be changed, and dependencies must not be installed automatically.

HostGuard uses only tools already available on the system. It is not a backup script.

## Objectives

- Provide a safe foundation for host administration workflows.
- Keep every capability isolated in a dedicated module.
- Prefer explicit, predictable operations over automatic changes.
- Preserve host and virtual machine integrity.
- Avoid external runtime dependencies.

## Architecture Overview

HostGuard separates platform-independent capabilities, shared core infrastructure, and platform integrations. The command-line entry point lives in `bin/`, mutable application data lives in `var/`, and operational records live in `logs/`. This separation prevents higher-level modules from depending directly on a specific virtualization platform.

### Core

`modules/core/` contains shared, platform-independent infrastructure: CLI parsing, configuration access, logging, runtime metadata, job identity, lock state, execution context, events, output, and version access. The Core does not perform host operations.

### Platform Layer

`modules/platform/` is the boundary for hypervisor integrations. The initial `platform/xe/` adapter implements only the explicitly permitted read-only host query. Future integrations may include Proxmox, VMware, or libvirt without requiring VMBackup to know which platform is active.

#### Platform Interface

The abstract `Platform` interface defines host, virtual machine, storage, network, pool, and version queries. Platform adapters must implement this contract, while consumers obtain normalized information exclusively through Inventory.

#### Capabilities

`Capabilities` declares whether a platform supports snapshot, export, import, pool, storage, and network operations. Every capability is `False` in Sprint 3.

#### Command Runner

`CommandRunner` is the single boundary for system command execution. It uses bounded execution, captures output without invoking a shell, and returns a typed result containing stdout, stderr, exit code, and execution time. Execution failures are converted into HostGuard platform exceptions.

#### First Communication with XCP-ng

Sprint 4 permits exactly one read-only host query: `xe host-list --minimal`. `XEPlatform.get_host()` uses this query only to discover the host UUID. No other XE command is implemented or permitted.

If XE is absent, times out, returns an error, or provides no UUID, Inventory reports the platform and Host UUID as unavailable while the application continues normally. Virtual machines, storage repositories, and networks remain simulated and empty.

### Inventory Engine

`modules/inventory/` is the single source of host information for every HostGuard module. Other modules must query Inventory instead of accessing the Platform Layer directly. This boundary keeps consumers platform-independent and ensures that discovery remains read-only.

`InventoryCollector` obtains host identity through the Platform Layer. Virtual machine, storage, and network collections remain static mocks.

### Job Engine

`modules/jobs/` defines the in-memory execution boundary for future HostGuard operations. It contains the Job model, lifecycle status enum, manager, synchronous engine, job events, and a structural event bus. No existing module depends on the Job Engine in Sprint 5.

#### Job Lifecycle

A job is created with a unique identifier and moves through explicit lifecycle states. The current synchronous flow is `CREATED` → `RUNNING` → `SUCCESS` or `FAILED`; a created or running job may also become `CANCELLED`. Timestamps, duration, metadata, and lifecycle events remain in memory only, and every state change is logged.

#### Event Bus

The Job Engine `EventBus` defines `publish()`, `subscribe()`, and `unsubscribe()` interfaces for future event delivery. Subscriber registration and dispatch are intentionally not implemented in Sprint 5.

### Execution Context

`ExecutionContext` is an immutable data structure containing the application version, hostname, environment, working directory, current user, start time, and job ID for one execution. It stores context without performing discovery or host changes.

### Event Driven Design

Future communication between modules will use events through the `Event` and `EventBus` interfaces. This boundary is intentionally unimplemented in Sprint 1.1 and establishes a low-coupling direction for later development.

### Project Principles

[PROJECT_PRINCIPLES.md](PROJECT_PRINCIPLES.md) defines HostGuard's binding safety and operational principles. Virtual machine integrity, auditability, reversibility, conservative failure, and predictable behavior take precedence over automation.

### Architecture Decision Records

Architectural decisions are documented as ADRs in [`docs/adr/`](docs/adr/). These records preserve the context, decision, and consequences of significant technical choices.

## Directory Structure

```text
hostguard/
├── bin/
│   └── hostguard
├── config/
│   └── hostguard.ini
├── modules/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── cli.py
│   │   ├── logger.py
│   │   ├── config.py
│   │   ├── runtime.py
│   │   ├── job.py
│   │   ├── lock.py
│   │   ├── context.py
│   │   ├── events.py
│   │   ├── output.py
│   │   └── version.py
│   ├── platform/
│   │   ├── __init__.py
│   │   ├── platform.py
│   │   ├── command_runner.py
│   │   ├── capabilities.py
│   │   ├── exceptions.py
│   │   └── xe/
│   │       ├── __init__.py
│   │       └── platform.py
│   ├── inventory/
│   │   ├── __init__.py
│   │   ├── inventory.py
│   │   ├── models.py
│   │   └── collector.py
│   ├── jobs/
│   │   ├── __init__.py
│   │   ├── engine.py
│   │   ├── job.py
│   │   ├── status.py
│   │   ├── event.py
│   │   ├── event_bus.py
│   │   └── manager.py
│   ├── vmbackup/
│   ├── backup-agent/
│   ├── doctor/
│   ├── storage/
│   └── monitor/
├── schemas/
│   └── README.md
├── var/
│   ├── cache/
│   ├── jobs/
│   ├── locks/
│   └── run/
├── logs/
├── docs/
│   └── adr/
│       ├── README.md
│       └── 0001-python-core.md
├── tests/
├── PROJECT_PRINCIPLES.md
├── VERSION
├── README.md
├── CHANGELOG.md
├── LICENSE
└── .gitignore
```

## Roadmap

- **Milestone 0:** Establish the project structure and documentation.
- **Sprint 1:** Provide the dependency-free core infrastructure and CLI parser.
- **Sprint 1.1:** Consolidate platform, context, event, output, schema, and architectural decision boundaries.
- **Sprint 2:** Establish a read-only Inventory Engine with simulated data.
- **Sprint 3:** Define virtualization platform abstractions without host communication.
- **Sprint 4:** Add the first bounded, read-only XCP-ng host query.
- **Sprint 5:** Establish the synchronous, in-memory Job Engine.
- **Future milestones:** Define and implement individual modules only after their safety requirements, interfaces, and validation strategies are specified.

Backup, restore, monitoring, host integration, and host modification remain unimplemented.

## Contributing

Contributions should remain small, modular, and conservative. Before submitting a change:

1. Confirm that it does not install dependencies or alter host configuration.
2. Confirm that it cannot place virtual machines at risk.
3. Keep functionality within the appropriate module boundary.
4. Update documentation and tests when the project reaches milestones that include executable behavior.

## License

HostGuard is available under the MIT License. See [LICENSE](LICENSE) for details.

## Current Project Status

HostGuard is at version `0.1.0-dev` and Sprint 5. Its Job Engine provides an isolated, synchronous in-memory lifecycle for future operations. No persistence, queue, concurrency, backup, restore, monitoring, storage, or doctor functionality is implemented.
