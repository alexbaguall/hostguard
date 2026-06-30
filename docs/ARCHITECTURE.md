# HostGuard Architecture

## Architectural Intent

HostGuard uses layered, low-coupling modules to keep platform communication, discovery, decisions, planning, orchestration, and execution state separate. The architecture is conservative by construction: higher-level modules must not bypass lower-level safety boundaries.

## System Context

```text
Administrator
     |
     v
   CLI ---------> Core services
     |
     +----------> Inventory --------> Platform --------> CommandRunner
     |                                  |                    |
     |                                  v                    v
     |                              XEPlatform             XCP-ng
     |
     +----------> Storage Manager
     |
     +----------> Backup Planner
     |
     +----------> Workflow Engine -----> Policy Engine
                        |
                        v
                    Job Engine --------> Events / Logger
```

Only the Platform Layer may describe platform-specific communication. Only `CommandRunner` may call `subprocess`. The sole implemented XE query is read-only:

```text
xe host-list --minimal
```

## Layer Relationships

```text
Presentation
  bin/hostguard
       |
       v
  modules/core/cli.py

Application foundations
  Core | Jobs | Workflow | Policy | Planner

Discovery
  Inventory | Storage

Integration
  Platform -> XEPlatform -> CommandRunner -> XCP-ng
```

Dependencies should point toward stable abstractions. VMBackup and future domain modules must consume Inventory rather than call a platform adapter directly.

## Core

`modules/core/` contains cross-cutting infrastructure:

- CLI parsing and output routing;
- INI configuration loading;
- standard logging;
- runtime metadata and execution context;
- version loading from `VERSION`;
- basic in-memory lock and legacy job identity structures;
- initial event interfaces.

Core does not contain backup behavior or platform commands.

## Platform

`modules/platform/` defines the abstract `Platform` contract, capabilities, platform exceptions, and `CommandRunner`. `CommandRunner` uses bounded `subprocess.run()` execution with captured output, no shell, and converted exceptions.

`modules/platform/xe/` implements only host UUID discovery. All other abstract platform methods reject use with `NotImplementedError`.

## Inventory

`modules/inventory/` is the normalization boundary for host information. It asks a Platform for host identity and returns safe unavailable data when the platform cannot respond. VM, storage repository, and network collections remain empty simulations.

Future modules must not query Platform directly when Inventory owns the information.

## Storage

`modules/storage/` reads configured target paths and inspects them with `os.path.exists()`, `os.path.ismount()`, `os.access()`, and `shutil.disk_usage()`. It never creates directories or writes storage data.

Selection requires an existing, mounted, writable target and chooses the lowest numeric priority. Minimum-space policy is not implemented.

## Planner

`modules/planner/` generates an immutable `BackupPlan` from a VM name and `StorageTarget`. Validation is currently limited to target existence, mount state, write access, and positive available space. Plan fields describing export or retention are declarative placeholders.

The Planner performs no backup action.

## Workflow

`modules/workflow/` defines abstract Workflows and Tasks plus concrete Stage orchestration and an in-memory Workflow registry. A Workflow owns ordered Stages; a Stage owns ordered Tasks.

No concrete Workflow or Task exists. Workflow can hold an optional PolicyManager but does not evaluate policies yet.

## Policy

`modules/policy/` defines side-effect-free Policy contracts, `PolicyResult`, exceptions, and an in-memory registry. Policies answer decisions; they must never execute actions.

No concrete Policy exists.

## Jobs

`modules/jobs/` defines the in-memory Job lifecycle:

```text
CREATED -> RUNNING -> SUCCESS
                  \-> FAILED

CREATED or RUNNING -> CANCELLED
```

The Job Engine accepts the legacy Job/callback form and Workflow objects. For a Workflow without a Job, the engine creates an in-memory Job and runs the Workflow through the existing lifecycle. There is no queue, persistence, threading, or multiprocessing.

## Events

Job lifecycle changes create `JobEvent` records. EventBus interfaces exist, but real subscriber registration and dispatch are intentionally absent. Future Workflows must produce auditable events before operational functionality is accepted.

## Logger

The logger uses Python's `logging` module and writes timestamped records to `logs/hostguard.log`. Command execution logs include the command, duration, and exit code but not complete stdout.

## Configuration

`ConfigurationManager` reads `config/hostguard.ini` and raises an explicit error when it is missing. Storage target definitions use a comma-separated identifier list and per-target path and priority keys.

## CLI

`bin/hostguard` loads the Python CLI. `argparse` owns command parsing, and `OutputManager` owns direct console output. CLI commands must not become alternate paths around Jobs, Workflows, Inventory, Storage, Policy, or Platform boundaries.

## Safety Boundary

```text
Allowed today:
  read configuration
  inspect configured storage paths
  create in-memory models
  execute exactly one read-only XE query

Not implemented:
  snapshot | backup | export | restore | retention | monitoring
```
