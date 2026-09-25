# Layer and Interface Reference

Use four practical layers:

1. Domain: entities, value concepts, and business rules.
2. Application: user-facing use cases and orchestration.
3. Interface adapters: mapping between application state and UI, storage, or external representations.
4. Frameworks and drivers: UI toolkit, database, network client, OS service, and SDKs.

Dependencies should point toward the domain. Use a small interface at a real seam, and keep concrete adapters outside the domain.
