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

`modules/platform/` is the boundary for future hypervisor integrations. The initial `platform/xe/` adapter is unimplemented and never executes XE or system commands. Future integrations may include Proxmox, VMware, or libvirt without requiring VMBackup to know which platform is active.

#### Platform Interface

The abstract `Platform` interface defines host, virtual machine, storage, network, pool, and version queries. Platform adapters must implement this contract, while consumers obtain normalized information exclusively through Inventory.

#### Capabilities

`Capabilities` declares whether a platform supports snapshot, export, import, pool, storage, and network operations. Every capability is `False` in Sprint 3.

#### Command Runner

`CommandRunner` reserves a single boundary for future system command execution. Its `run()` method currently raises `NotImplementedError` and does not invoke the operating system.

### Inventory Engine

`modules/inventory/` is the single source of host information for every HostGuard module. Other modules must query Inventory instead of accessing the Platform Layer directly. This boundary keeps consumers platform-independent and ensures that discovery remains read-only.

In Sprint 2, `InventoryCollector` returns static mock data only. It does not inspect the host or communicate with any platform integration.

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

HostGuard is at version `0.1.0-dev` and Sprint 3. Its Platform Layer defines interfaces only, and Inventory continues to expose simulated data. No command execution, host discovery, backup, restore, monitoring, storage, doctor, or platform functionality is implemented.
