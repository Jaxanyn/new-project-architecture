---
name: new-project-architecture
description: Design a software project's architecture before implementation. Use when starting a new project or when requirements need to become a domain model, layered structure, module interfaces, dependency rules, and acceptance criteria.
---

# New Project Architecture

Turn a new project's requirements into a decision-complete architecture plan before implementation.

## Scope

Use this skill for greenfield projects and early architecture decisions. Do not use it to reconstruct an existing codebase or plan a behavior-preserving migration; use an existing-project refactoring workflow for that.

## Workflow

1. Read the repository rules, README, configuration, and any existing design documents.
2. State the product goal, users, non-goals, constraints, and success criteria.
3. Build the domain model: entities, value concepts, relationships, invariants, and important scenarios.
4. Design layers and dependency direction. Keep domain rules independent from UI, storage, frameworks, and external SDKs.
5. Design deep modules and small interfaces for use cases, repositories, external services, and adapters. Add a seam only when a real change or replacement point exists.
6. Choose one thin vertical slice that proves the architecture from user action through persistence or external integration.
7. Define acceptance scenarios for the happy path, invalid input, empty data, dependency failure, concurrency or stale responses, and rollback where relevant.
8. Produce an implementation plan with independently usable phases. Name file or module targets, public interfaces, risks, and verification for each phase.
9. Stop after the plan. Do not edit implementation files until the user explicitly approves the plan.

## Output

Return these sections:

- Building
- Not building
- Domain model and business rules
- Layer and dependency map
- Module interfaces and adapters
- First vertical slice
- Acceptance matrix
- Phased implementation plan
- Risks, assumptions, and rollback

## Design rules

- Prefer the smallest architecture that supports the stated change axes.
- Keep business rules in the domain or application layer, not in UI event handlers.
- Treat external services and SDKs as replaceable adapters.
- Separate durable business data from rebuildable cache or presentation state.
- Do not introduce microservices, event buses, or new runtimes without a concrete need.
- Record a decision as an ADR only when it is difficult to reverse, surprising later, and based on a real trade-off.

## Optional adapters

For a platform-specific project, load the platform reference only after the domain and dependency design are clear. For high-risk data, authentication, payment, concurrency, or public APIs, add executable specifications and stronger verification.

## Completion

The skill is complete when another engineer can implement the first phase without making architecture decisions again, and the user can see how the plan will be verified.
