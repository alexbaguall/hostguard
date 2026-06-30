# ADR 0001: Implement the HostGuard Core in Python

- **Status:** Accepted
- **Date:** 2026-06-30

## Context

HostGuard requires a conservative, maintainable core that can coordinate future modules without modifying host configuration or automatically installing dependencies. The core needs clear abstractions for command-line parsing, configuration, logging, runtime metadata, job identity, and execution state.

XCP-ng and XenServer environments commonly provide Python 3, including a mature standard library for these infrastructure concerns. Using the standard library avoids framework coupling and keeps deployment behavior explicit.

## Decision

The HostGuard Core is implemented in Python 3 using only the Python standard library. Core components use type hints, docstrings, small interfaces, and isolated responsibilities.

Platform-specific operations remain outside the Core. They belong behind the Platform Layer and must not leak into platform-independent modules such as VMBackup.

## Consequences

The project gains a readable and modular foundation without third-party runtime dependencies. Python's standard library provides the required primitives while supporting gradual architectural evolution.

Contributors must preserve compatibility with the Python version supported by the target hosts. Any future external dependency requires an explicit architectural decision and must never be installed automatically.
