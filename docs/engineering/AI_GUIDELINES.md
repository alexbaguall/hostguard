# AI Engineering Guidelines

AI tools are collaborators, not sources of project memory. Repository documentation is authoritative.

## Required Preparation

Before modifying any code:

1. Read `AI_CONTEXT.md`.
2. Read `docs/CURRENT_STATUS.md`.
3. Read `docs/ARCHITECTURE.md`.
4. Read `PROJECT_PRINCIPLES.md`.
5. Read `docs/ROADMAP.md`.
6. Read `docs/engineering/CODING_STANDARDS.md`.
7. Read `docs/decisions/DECISION_LOG.md`.
8. Read every ADR in `docs/adr/`.

Then inspect the current Git status and the files in scope. Never assume that earlier conversation context is more current than the repository.

## Change Discipline

- Never alter architecture without an ADR.
- Never create a duplicate module, manager, model, or responsibility.
- Never move code without an explicit technical justification.
- Never expand a Sprint beyond its written acceptance criteria.
- Never bypass Workflow, Job, Inventory, Platform, Policy, or CommandRunner boundaries.
- Never infer authorization for destructive behavior.

## Documentation Discipline

Always update documentation when behavior, contracts, module ownership, safety boundaries, or project status changes. Every Sprint must update `docs/CURRENT_STATUS.md`; roadmap changes belong in `docs/ROADMAP.md`; architecture changes require both an ADR and `docs/ARCHITECTURE.md` updates.

## Verification Discipline

Use read-only inspection first. Validate exact CLI output when specified. Use injected fakes or mocks rather than real host operations unless the specification explicitly authorizes a particular read-only command. Confirm that the working tree contains only intended changes before committing.

## Handling Uncertainty

Stop when requirements would materially change architecture, safety, or external state and the repository does not provide authority. Document assumptions only when they are safe, reversible, and within scope.
