# HostGuard Coding Standards

## Python and PEP 8

HostGuard uses Python 3 and the standard library unless an ADR explicitly approves otherwise. Code must follow PEP 8 naming, layout, import ordering, and readability guidance.

## Type Hints

All function parameters and return values must be typed. Public attributes and data contracts must have explicit types. Avoid `Any` when a stable boundary can be expressed.

## Dataclasses

Use dataclasses for data-oriented models with little or no behavior. Prefer frozen dataclasses for value objects when mutation is unnecessary. Do not force domain services into dataclasses.

## Docstrings

Every module, class, and function must have a concise technical docstring. Docstrings explain contracts and safety boundaries; they should not restate implementation line by line.

## Small Functions

Functions should normally remain below 40 lines and have one responsibility. Extract named helpers when validation, formatting, error conversion, or side effects begin to mix.

## Small Classes

Classes should normally remain below approximately 250 lines. Split classes by responsibility, not merely to satisfy a line count.

## Clean Architecture

Presentation, orchestration, decisions, discovery, and platform integration must remain separate. Higher-level modules depend on stable interfaces rather than concrete host commands.

## Low Coupling

Avoid hidden global state, circular ownership, and cross-module knowledge. Inject collaborators when a component must be testable without contacting a host or filesystem.

## No Direct Subprocess

Only `modules/platform/command_runner.py` may import and call `subprocess`. Every call must use bounded execution, captured output, `shell=False` semantics, and HostGuard exceptions.

## No Direct XE

XE commands belong only in `modules/platform/xe/`. Other modules obtain host information through Inventory. Any new XE command requires a dedicated Sprint specification and safety review.

## Compatibility and Scope

Preserve existing CLI behavior and public contracts unless a specification explicitly changes them. Never implement adjacent functionality merely because it appears useful.

## Verification

Tests and validation must avoid destructive host operations. Use dependency injection and in-memory substitutes for Platform, storage, Policy, Workflow, and command boundaries.
