# Project Summary

HostGuard is a conservative administration platform for XCP-ng and XenServer hosts. Its purpose is to provide safe, modular infrastructure for inventory, planning, policy decisions, workflows, jobs, storage selection, and future backup operations. It is intended for infrastructure administrators and engineers who require predictable and auditable host operations.

HostGuard is not a backup script. Its defining philosophy is that virtual machine integrity takes precedence over task completion. When state is uncertain, the operation must stop without changing the host.

# Current Project Status

- **Version:** `0.1.0-dev`
- **Current milestone:** Project Identity Documentation (Sprint D2)
- **Architecture:** Frozen at the foundation established through Sprint 9
- **Last completed sprint:** Sprint D2 — HostGuard Manifesto
- **Next sprint:** Not yet defined; implementation requires an approved specification

The project contains architectural foundations and limited read-only discovery. Backup, snapshot, export, restore, monitoring, and concrete workflow or policy implementations do not exist.

# Current Architecture

- **Core:** Shared CLI, configuration, logging, runtime, version, context, output, and basic lock/event structures.
- **Platform:** Abstract virtualization boundary. `XEPlatform` permits only `xe host-list --minimal`.
- **Inventory:** The only intended source of normalized host information for other modules. VM, storage repository, and network inventory remain simulated.
- **Storage:** Read-only discovery and priority-based selection of configured filesystem targets.
- **Planner:** Creates declarative backup plans from a VM name and storage metadata; it executes nothing.
- **Workflow:** Abstract Workflow, Stage, and Task orchestration.
- **Policy:** Abstract side-effect-free business decision contracts and typed results.
- **Jobs:** In-memory lifecycle, events, state transitions, and synchronous execution boundary.
- **Events:** Structural event interfaces exist in Core and the Job Engine; real subscriber dispatch is not implemented.
- **Logger:** Standard-library logging to `logs/hostguard.log` with timestamp and severity.
- **Configuration:** Standard-library INI reader for `config/hostguard.ini`.
- **CLI:** `argparse` entry point in `bin/hostguard`; implemented informational commands are documented in `docs/CURRENT_STATUS.md`.

# Engineering Principles

The following rules are mandatory:

1. Never execute destructive actions without an approved Workflow.
2. Never call `subprocess` directly outside `CommandRunner`.
3. Never execute `xe` outside the Platform Layer.
4. Always preserve low coupling and explicit module boundaries.
5. Use dataclasses for data-only structures when appropriate.
6. Every important operation must create a Job.
7. Every future Workflow must generate auditable Events.
8. Every architectural change requires an ADR.
9. Never install dependencies or perform system upgrades automatically.
10. Abort when safety, state, or intent is uncertain.

# Required Reading Order

Before changing the project, read these sources in order:

1. `AI_CONTEXT.md`
2. `HOSTGUARD_MANIFESTO.md`
3. `docs/CURRENT_STATUS.md`
4. `docs/ARCHITECTURE.md`
5. `PROJECT_PRINCIPLES.md`
6. `docs/ROADMAP.md`
7. `docs/engineering/CODING_STANDARDS.md`
8. `docs/decisions/DECISION_LOG.md`
9. Every ADR in `docs/adr/`
10. The corresponding RFC in `docs/rfc/`

# Development Rules

- Do not create new architecture without demonstrated need and an accepted ADR.
- Do not duplicate responsibilities already owned by another module.
- Do not add code without updating the relevant technical documentation.
- Preserve backward compatibility unless an approved specification explicitly changes it.
- Update `docs/CURRENT_STATUS.md` after every Sprint.
- Keep implementation inside the authorized Sprint scope.
- Treat documentation as an architectural artifact, not optional commentary.
- Use `HOSTGUARD_MANIFESTO.md` as the prevailing identity and engineering philosophy when technical choices are uncertain.
- Begin every implementation by reading an approved corresponding RFC. No new functionality may be implemented without that approval.
