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

HostGuard follows a modular architecture. The command-line entry point lives in `bin/`, while independent capabilities live in `modules/`. Mutable process state is separated into `runtime/`, operational records into `logs/`, and persistent project data into `data/`.

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
├── modules/
│   ├── vmbackup/
│   ├── backup-agent/
│   ├── doctor/
│   ├── storage/
│   ├── xe/
│   └── monitor/
├── runtime/
│   ├── jobs/
│   ├── locks/
│   └── pid/
├── logs/
├── data/
│   ├── manifests/
│   ├── history/
│   └── cache/
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
- **Future milestones:** Define and implement individual modules only after their safety requirements, interfaces, and validation strategies are specified.

Backup, restore, monitoring, configuration parsing, and host modification are outside the scope of Milestone 0.

## Contributing

Contributions should remain small, modular, and conservative. Before submitting a change:

1. Confirm that it does not install dependencies or alter host configuration.
2. Confirm that it cannot place virtual machines at risk.
3. Keep functionality within the appropriate module boundary.
4. Update documentation and tests when the project reaches milestones that include executable behavior.

## License

HostGuard is available under the MIT License. See [LICENSE](LICENSE) for details.

## Current Project Status

HostGuard is at version `0.1.0-dev` and Milestone 0. The repository currently contains project scaffolding only. Backup, restore, monitoring, parsing, configuration, and host administration functionality have not been implemented.
