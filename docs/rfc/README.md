# HostGuard Request for Comments

The RFC directory contains the authoritative engineering proposals that govern HostGuard changes. An RFC records motivation, scope, design, risks, tests, acceptance conditions, rollback, and documentation impact before implementation begins.

## Mandatory Rule

No new functionality may be implemented without a corresponding RFC in the `Approved` state. Architectural changes also require updated or new Architecture Decision Records.

Documentation corrections that do not change behavior or architecture may be made without a feature RFC, but they must remain traceable through Git and must not contradict an approved RFC.

## RFC Lifecycle

```text
Draft
  |
  v
Review
  |
  v
Approved
  |
  v
Implementation
  |
  v
Testing
  |
  v
Released
  |
  v
Deprecated (when necessary)
```

Every RFC must state exactly one lifecycle status. A status change must be committed as a reviewable documentation update.

## Engineering Delivery Flow

```text
Idea
  -> RFC Draft
  -> Review
  -> Approval
  -> Implementation
  -> Testing
  -> Qualification
  -> Merge
  -> Release
```

Implementation must not start before approval. Testing and qualification evidence must exist before merge and release.

## Required RFC Structure

Every RFC must contain exactly these top-level sections in this order:

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

## RFC Index

| RFC | Title | Status |
| --- | --- | --- |
| [RFC-000](RFC-000-Engineering-Process.md) | Engineering Process | Draft |
