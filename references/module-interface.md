# Module Interface Reference

Prefer deep modules: a small interface hides meaningful behavior.

For each module, state:
- What callers must know
- Inputs and outputs
- Invariants and ordering
- Error behavior
- Side effects
- What can change without editing callers

Do not create a seam only because a second file would look cleaner. Add one when behavior varies, replacement is likely, or the interface creates a useful test surface.
