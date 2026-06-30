# Why HostGuard Exists

HostGuard exists to provide a safe, predictable, and auditable way to administer XCP-ng and XenServer environments. It was not created to become another backup script. Its purpose is to establish a professional administration platform in which discovery, decisions, planning, execution, validation, and recovery follow explicit technical boundaries.

Virtual infrastructure carries operational state that cannot be treated as disposable. Administrative convenience never justifies unnecessary risk to virtual machines, storage, or host availability.

# Mission

Protect virtual infrastructure without compromising availability, integrity, or administrative control.

HostGuard fulfills this mission by making operations explicit, bounded, observable, and safe to reject when required conditions cannot be proven.

# Vision

HostGuard is intended to become a complete platform for administration, backup, validation, recovery, and monitoring of XCP-ng environments. Its long-term scope may expand, but every capability must preserve the same safety model and architectural discipline.

Growth must occur through stable contracts rather than accumulated scripts. New platform integrations, interfaces, and operational features must remain subordinate to predictable behavior and recoverability.

# Core Principles

1. Security takes precedence over speed.
2. Predictability takes precedence over automation.
3. Recovery capability is more important than backup creation.
4. Every important operation must be auditable.
5. Virtual machines must never be placed at unnecessary risk.
6. Architecture must remain as simple as the problem permits.
7. Explicit behavior is preferable to hidden mechanisms.
8. The administrator must never be surprised by an operation.
9. Every backup must be verifiable.
10. Every restore must be testable.
11. Documentation is part of the product.
12. Uncertainty requires refusal, not optimistic execution.

# Engineering Principles

HostGuard uses clean architectural boundaries, low coupling, and single-responsibility components. Modules must own clear concerns and must not bypass abstractions established for safety, auditability, or testability.

The following engineering requirements are mandatory:

- Follow PEP 8 and use type hints throughout Python code.
- Use dataclasses for data-oriented structures when appropriate.
- Provide technical docstrings for modules, classes, and functions.
- Keep functions and classes small enough to review confidently.
- Treat documentation as a required deliverable for every capability.
- Never call `subprocess` outside `CommandRunner`.
- Never execute `xe` outside the Platform Layer.
- Represent every important operation as a Job.
- Require every operational Workflow to generate auditable Events.
- Record every architectural change in an ADR before implementation.
- Preserve compatibility unless an approved specification explicitly changes it.

# Product Philosophy

HostGuard does not aim to compete with broad enterprise management suites. It aims to provide a focused platform with a narrow and understandable operational surface.

The product should remain:

- lightweight enough to understand and deploy deliberately;
- simple enough to audit;
- explicit enough to predict;
- reliable under expected failure conditions;
- conservative around production infrastructure;
- free of unnecessary runtime dependencies.

Feature count is not a measure of product quality. A smaller capability with defined failure behavior is preferable to a broader capability with ambiguous operational consequences.

# Design Philosophy

Interfaces must be small, commands must be explicit, and messages must identify outcomes clearly. Failures should be anticipated and represented through stable exceptions, results, state transitions, and operator-visible records.

HostGuard must not perform destructive operations without explicit authorization and confirmation appropriate to the risk. It must not hide automation behind apparently informational commands. Defaults must be conservative, and side effects must be visible in the design.

No abstraction should obscure which component owns a decision or action. Discovery, policy, planning, workflow orchestration, job state, and platform execution are separate responsibilities.

# Development Philosophy

Code must be written for maintenance over many years. Readability, stable contracts, and documented intent are more valuable than short-term implementation speed.

Every significant decision must be documented. Every capability must have technical documentation, defined safety constraints, and tests when behavior is introduced. Every Sprint must update `docs/CURRENT_STATUS.md`.

Complexity requires evidence. New layers, dependencies, concurrency, persistence, and automation must not be added without a demonstrated requirement and an approved design. Existing responsibilities must be extended deliberately rather than duplicated.

# AI Development Rules

Before modifying code, every AI system must read:

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

An AI system must not alter architecture without documenting and justifying the change through an ADR. It must not remove existing documentation merely because a shorter representation is possible. Repository documentation is authoritative; conversational memory is not.

AI-assisted changes must remain within the approved Sprint, preserve existing work, verify safety constraints, and update project documentation when contracts or status change.

# Production Philosophy

Production environments have absolute priority over convenience, delivery speed, and automation. Every operational capability must be qualified in a controlled laboratory before production use.

Backups must never place virtual machines at unnecessary risk. A completed backup is not successful unless its integrity can be verified and its recovery path can be tested.

Rollback and failure recovery must be considered before an operation is authorized. When rollback is impossible, that limitation must be explicit and accepted before execution. If HostGuard cannot establish that an operation is safe, it must abort.
