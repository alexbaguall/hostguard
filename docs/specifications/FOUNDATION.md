# Foundation Specification

## Scope

The HostGuard foundation was built from Milestone 0 through Sprint 9. It establishes boundaries and limited read-only behavior; it does not provide backup or restore functionality.

## Core Foundation

The project uses Python 3 and standard-library components. Core provides CLI parsing, configuration, logging, version access, runtime metadata, execution context, output routing, and initial lock/event structures.

## Platform and Inventory Foundation

Platform adapters implement an abstract query contract. Command execution is isolated in CommandRunner. XE integration currently permits only `xe host-list --minimal`. Inventory is the intended information source for consumers and safely reports unavailable platform data.

## Execution Foundation

Jobs represent in-memory lifecycle state and audit events. Workflows organize Stages and abstract Tasks and run through the Job Engine. Policies return decisions without executing actions. Real event dispatch, persistence, queues, and concurrency do not exist.

## Storage and Planning Foundation

Storage Manager inspects configured paths with read-only standard-library APIs and selects eligible targets by priority. Backup Planner produces declarative plans and validates only storage readiness. It uses simulated VM identity and performs no backup action.

## Safety Constraints

- No dependency installation or system upgrade.
- No host configuration mutation.
- No snapshot, backup, export, restore, or retention.
- No direct subprocess outside CommandRunner.
- No direct XE outside Platform.
- No platform access by consumers that should use Inventory.

## Documentation Foundation

Sprint D1 makes repository documentation the permanent source of project knowledge. `AI_CONTEXT.md` defines mandatory reading, `docs/CURRENT_STATUS.md` tracks delivery state, and ADRs preserve architectural decisions.
