# HostGuard Roadmap

This roadmap describes architectural phases, not delivery dates. A phase does not authorize implementation; every Sprint still requires an explicit specification.

## Foundation

**Status:** Established.

Core, Platform, Inventory, Jobs, Workflow, Policy, event, configuration, logging, CLI, and documentation boundaries exist. Remaining foundation work should focus on tests, contract refinement, and accepted ADRs rather than reorganizing modules.

## Storage

**Status:** Read-only foundation established.

Configured local paths can be inspected and selected by availability and priority. Future work may define capacity policies and supported storage classes. HostGuard must not become a general storage configuration tool.

## Planning

**Status:** Simulated foundation established.

BackupPlan generation and storage readiness validation exist. Future work must add normalized VM inventory, policy evaluation, size estimation, and approved plan contracts before execution.

## Backup

**Status:** Not implemented.

This phase must specify safe Workflow stages, snapshot policy, export behavior, cancellation, cleanup, manifests, failure recovery, and audit events. No backup operation is authorized today.

## Validation

**Status:** Not implemented.

Future validation may include manifest contracts, integrity hashes, independent verification, and recovery-readiness reporting. Validation must not silently mutate backup data.

## Restore

**Status:** Not implemented.

Restore requires a dedicated safety model, dry-run planning, conflict detection, reversibility analysis, and explicit operator confirmation. Backup implementation does not imply restore authorization.

## Monitoring

**Status:** Not implemented.

Monitoring may consume events and report health without altering hosts. Scheduling, alert transport, persistence, and escalation behavior require separate decisions.

## Web UI

**Status:** Not implemented.

A future UI must remain a presentation layer over existing application boundaries. It must not call XE, storage APIs, or destructive operations directly.

## Future

Potential work includes additional virtualization platforms, richer reporting, multi-host coordination, and API surfaces. These items are exploratory and require ADRs before they influence architecture.
