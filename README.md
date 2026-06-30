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

## Architecture

HostGuard follows a modular architecture. The command-line entry point lives in `bin/`, shared infrastructure lives in `modules/core/`, and future capabilities remain isolated in their own module directories. Mutable application data is separated into `var/`, while operational records live in `logs/`.

The initial module boundaries are:

- **VMBackup** for future virtual machine backup orchestration.
- **Backup Agent** for future backup agent operations.
- **Doctor** for future diagnostic checks.
- **Storage** for future storage operations.
- **XE** for future integration with existing XE tooling.
- **Monitor** for future monitoring capabilities.

These directories are placeholders only. No operational functionality is included in the current milestone.

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
│   │   └── version.py
│   ├── vmbackup/
│   ├── backup-agent/
│   ├── doctor/
│   ├── storage/
│   ├── xe/
│   └── monitor/
├── var/
│   ├── cache/
│   ├── jobs/
│   ├── locks/
│   └── run/
├── logs/
├── docs/
├── tests/
├── VERSION
├── README.md
├── CHANGELOG.md
├── LICENSE
└── .gitignore
```

## Roadmap

- **Milestone 0:** Establish the project structure and documentation.
- **Sprint 1:** Provide the dependency-free core infrastructure and CLI parser.
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

HostGuard is at version `0.1.0-dev` and Sprint 1. The repository contains its core CLI, configuration reader, logger, runtime information collector, in-memory job manager, and lock state abstraction. No host administration module is implemented.
