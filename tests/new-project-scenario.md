# Real-world validation: new project

## Scenario
Design a local single-user travel planning application before implementation.

## Expected result
The Skill must produce a decision-complete plan containing:

- Product goal, non-goals, constraints, and success criteria.
- Trip, TripDay, Place, Stop, Route, and Accommodation domain concepts.
- Business rules for ordering, date changes, durable data, and rebuildable route cache.
- Domain, application, adapter, and infrastructure layers with inward dependencies.
- Small interfaces for trip persistence, place search, route planning, backup, and navigation.
- A first vertical slice: create a trip, persist it, reload it, and render it.
- Acceptance scenarios for normal input, invalid input, empty state, adapter failure, stale responses, and rollback.
- Independently usable implementation phases.

## Boundary checks
- No implementation files are edited during planning.
- No database, UI framework, or map SDK is placed in the domain layer.
- No microservice or new runtime is introduced without a concrete requirement.

## Result
The current SKILL.md includes the required greenfield trigger, domain modeling, layer and interface design, vertical slice, acceptance matrix, phased plan, and stop-before-code behavior. Contract checks and quick_validate.py passed.
