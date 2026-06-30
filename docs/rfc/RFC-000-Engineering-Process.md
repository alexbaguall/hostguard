# Title

RFC-000: Engineering Process

# Status

Draft

# Authors

HostGuard contributors

# Date

2026-06-30

# Motivation

HostGuard operates near production virtualization infrastructure, where incomplete requirements, implicit decisions, and unreviewed implementation can create unacceptable risk. Conversation history and individual memory are not durable engineering controls.

The project requires one traceable process that forces important questions to be answered before code is written. Every proposed capability must define its purpose, boundaries, architecture, risk, security impact, validation, acceptance conditions, rollback, and documentation changes.

# Objectives

- Establish the mandatory engineering process for the lifetime of HostGuard.
- Require an approved RFC before implementation of any new functionality.
- Define official RFC lifecycle states and delivery stages.
- Standardize the content and reviewability of every RFC.
- Define accountable engineering roles without requiring separate people.
- Require reproducible validation before functionality is considered complete.
- Preserve architectural decisions through ADRs.
- Define release versioning through Semantic Versioning.
- Make the process mandatory for human and AI-assisted contributors.

# Scope

This RFC governs new functionality, behavior changes, architectural changes, operational capabilities, platform commands, security-sensitive work, and releases.

It defines:

- the RFC lifecycle;
- the engineering delivery flow;
- the required RFC document structure;
- approval and implementation gates;
- contributor roles;
- AI preparation requirements;
- test and qualification expectations;
- release versioning;
- rollback and documentation obligations.

Expected impacts are additional design work before implementation, clearer review boundaries, reproducible acceptance evidence, and reduced reliance on undocumented context.

# Non Goals

- Define a specific HostGuard feature.
- Change the current application architecture.
- Change runtime behavior or CLI behavior.
- Select project-management software or hosting platforms.
- Require that each role be assigned to a different person.
- Replace ADRs, coding standards, the Project Manifesto, or project principles.
- Define release dates or delivery estimates.

# Architecture

The RFC process is a governance layer around the existing engineering lifecycle. It does not add an application runtime component.

```text
Idea
  |
  v
RFC Draft
  |
  v
Review
  |
  v
Approval
  |
  +------ architectural change ------> ADR update/creation
  |
  v
Implementation
  |
  v
Automated and/or reproducible testing
  |
  v
Qualification
  |
  v
Merge
  |
  v
Release
```

The corresponding RFC remains the traceable contract throughout implementation, testing, qualification, merge, release, and eventual deprecation.

# Design Decisions

**Official lifecycle states**

```text
Draft
  -> Review
  -> Approved
  -> Implementation
  -> Testing
  -> Released
  -> Deprecated (when necessary)
```

- `Draft`: the proposal is incomplete or awaiting initial review.
- `Review`: the proposal is complete enough for technical and product review.
- `Approved`: scope, design, risks, tests, rollback, and acceptance criteria are authorized.
- `Implementation`: approved work is actively being implemented.
- `Testing`: implementation is complete enough for validation and qualification.
- `Released`: acceptance criteria are satisfied and the capability is released.
- `Deprecated`: the released capability or RFC is retained for history but should no longer guide new use.

Skipping lifecycle states is not permitted. Rejected proposals remain in Git history; a future replacement receives its own RFC or an explicit revision.

**Mandatory RFC sections**

Every RFC must contain exactly these top-level sections and preserve their order:

1. `# Title`
2. `# Status`
3. `# Authors`
4. `# Date`
5. `# Motivation`
6. `# Objectives`
7. `# Scope`
8. `# Non Goals`
9. `# Architecture`
10. `# Design Decisions`
11. `# Risks`
12. `# Security Considerations`
13. `# Test Plan`
14. `# Acceptance Criteria`
15. `# Rollback Strategy`
16. `# Documentation Updates`
17. `# Changelog`

**Implementation gate**

No implementation may begin before the corresponding RFC reaches `Approved`. If implementation discovers a material mismatch in scope, architecture, safety, or acceptance criteria, work must stop and the RFC must return to review.

**Architecture gate**

No architectural change may proceed without an updated or new ADR. RFCs describe proposed work; ADRs preserve accepted architectural decisions and consequences.

**Roles**

- `Product Owner`: defines priorities, product intent, and acceptance expectations.
- `Architect`: protects module boundaries, evaluates architecture, and owns ADR requirements.
- `Developer`: implements only the approved scope and provides technical evidence.
- `Reviewer`: performs independent technical and scope review.
- `Tester`: validates acceptance criteria and qualification evidence.

One person may hold multiple roles. Role combination does not remove any review, test, or documentation obligation.

**AI requirements**

Before changing code, an AI system must read:

1. `AI_CONTEXT.md`
2. `HOSTGUARD_MANIFESTO.md`
3. `docs/CURRENT_STATUS.md`
4. `docs/ARCHITECTURE.md`
5. `docs/ROADMAP.md`
6. `PROJECT_PRINCIPLES.md`
7. every ADR in `docs/adr/`
8. the corresponding RFC

AI systems must not alter architecture without justification and an ADR. They must not remove documentation without explicit justification. Repository content is authoritative over conversational memory.

**Testing**

Every RFC must define how its implementation will be tested. Automated tests are preferred. When automation is not feasible, the RFC must define manual tests that another contributor can reproduce. No functionality is complete without validation against its acceptance criteria.

**Releases**

HostGuard follows Semantic Versioning. Development maturity may be expressed with prerelease identifiers, for example:

- `0.1.0-alpha`
- `0.2.0-alpha`
- `0.5.0-beta`
- `1.0.0`

Version changes must describe compatibility impact and must not imply production readiness without qualification evidence.

# Risks

- Process overhead may be disproportionate for very small changes.
- Poorly written RFCs may create procedural compliance without useful engineering clarity.
- Lifecycle status may become stale if owners do not update the RFC.
- Combined roles may reduce independence of review.
- Implementation may drift from the approved RFC.

These risks are mitigated through concise scope, explicit acceptance criteria, reviewable status changes, reproducible tests, ADR enforcement, and documentation updates.

# Security Considerations

The RFC gate reduces the risk of unauthorized platform commands, destructive behavior, hidden dependencies, and unreviewed privilege changes. Every security-sensitive RFC must document permissions, trust boundaries, command execution, data exposure, logging, failure behavior, and rollback.

Approval does not replace security review. Uncertainty about host safety, virtual machine integrity, storage integrity, or operator intent requires the proposal or implementation to stop.

# Test Plan

RFC-000 is a documentation-only change. Validation consists of:

1. Confirming `docs/rfc/README.md` and this RFC exist.
2. Confirming this RFC contains exactly the required top-level sections in the required order.
3. Confirming all official lifecycle states are documented.
4. Confirming the engineering flow, roles, AI rules, testing policy, and Semantic Versioning examples are present.
5. Confirming README links resolve.
6. Confirming `AI_CONTEXT.md` requires the corresponding RFC before implementation.
7. Confirming no application code, configuration, architecture, or behavior changed.

# Acceptance Criteria

- `docs/rfc/` exists.
- `docs/rfc/README.md` documents the RFC process and index.
- `docs/rfc/RFC-000-Engineering-Process.md` exists with status `Draft`.
- The lifecycle and engineering delivery flow are explicit.
- The mandatory RFC structure is documented exactly.
- Product Owner, Architect, Developer, Reviewer, and Tester roles are defined.
- AI preparation and restriction rules are documented.
- Testing and release versioning requirements are documented.
- README contains an Engineering Process section linking to `docs/rfc/`.
- `AI_CONTEXT.md` requires reading the corresponding RFC before implementation.
- No runtime behavior or application architecture changes.

# Rollback Strategy

Because this RFC changes documentation only, rollback requires reverting the documentation commit. A rollback must explain why the engineering process is being withdrawn and must restore all affected references consistently.

Rollback must not be used to bypass review for an implementation already governed by an approved RFC. Once other RFCs depend on RFC-000, replacing this process requires a new governance RFC and preservation of historical records.

# Documentation Updates

This RFC creates:

- `docs/rfc/README.md`
- `docs/rfc/RFC-000-Engineering-Process.md`

It updates:

- `README.md`
- `AI_CONTEXT.md`
- `HOSTGUARD_MANIFESTO.md`
- `docs/CURRENT_STATUS.md`
- `docs/engineering/AI_GUIDELINES.md`
- `docs/decisions/DECISION_LOG.md`
- `CHANGELOG.md`

# Changelog

- 2026-06-30: Initial Draft defining the HostGuard engineering process.
