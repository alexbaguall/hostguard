# HostGuard Project Vision

## What HostGuard Is

HostGuard is a conservative administration platform for XCP-ng and XenServer environments. It is designed to coordinate discovery, decisions, planning, execution lifecycles, and future data-protection operations through explicit architectural boundaries.

The platform serves administrators who value safety, auditability, and predictable behavior over unattended automation.

## Problem Statement

Virtualization administration often grows from isolated scripts with implicit assumptions, weak error boundaries, and platform-specific coupling. Such tools can become difficult to audit and dangerous to extend. HostGuard provides a durable structure in which host communication is isolated, decisions are explicit, operations are planned before execution, and important work is represented by Jobs and Workflows.

## What HostGuard Does Not Intend to Solve

HostGuard is not:

- a general operating system configuration manager;
- an automatic package installer or upgrade service;
- a replacement for XCP-ng or XenServer management tooling;
- an unrestricted remote command runner;
- a generic storage, RAID, NAS, NFS, or SMB manager;
- a guarantee that unsafe operations should continue after uncertainty is detected.

## Version 1.0 Objectives

Version 1.0 should provide a conservative, tested backup lifecycle for supported XCP-ng environments. Before that release, the project must define and validate inventory contracts, backup policies, planning rules, Workflow and Job integration, manifests, integrity checks, operational failure handling, and a bounded restore design.

Version 1.0 must remain usable without automatic dependency installation and must make every important decision auditable.

## Version 2.0 Objectives

Version 2.0 may expand operational maturity through richer scheduling, retention, restore validation, reporting, and multi-host coordination. Its scope must be defined by future specifications and ADRs; no Version 2.0 capability is currently committed.

## Future Objectives

Possible long-term directions include additional virtualization platforms, a web interface, richer event consumers, and broader operational reporting. These are possibilities, not approved features. Platform independence must be preserved through Inventory and Platform boundaries.
