# Production Operations

## Production Readiness

HostGuard `0.1.0-dev` is not production-ready for backup, restore, or host administration. It must not be represented as a data-protection solution.

## Current Production Boundary

The code contains limited read-only discovery, but no production support commitment has been defined. Operators must not schedule HostGuard, grant broader privileges, or depend on simulated plans as evidence that a backup can execute.

## Requirements Before Production Use

Production use requires, at minimum:

- approved backup and restore specifications;
- complete automated tests;
- validated manifests and integrity checks;
- failure recovery and rollback procedures;
- permissions and threat-model review;
- compatibility matrix for supported hosts;
- operational logging and retention policy;
- release process and support expectations.

Until these requirements are satisfied, use HostGuard only for controlled engineering evaluation.
