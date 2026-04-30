# Game Development Workflow

Use this workflow for gameplay bugs, physics issues, mechanics design, and
implementation work in a game project.

## Steps

1. Reproduce the gameplay symptom.
2. Capture concrete state: input, position, velocity, collision normal, timers.
3. Identify whether the issue is rule logic, physics integration, state machine,
   animation, or input timing.
4. Prefer a small testable module for core mechanics.
5. Use TDD where mechanics can be modeled deterministically.
6. Verify the fix across representative scenes and edge cases.
7. Separate symptom patches from structural fixes.

## Example Verification Matrix

- Flat ground
- 15 degree slope
- 30 degree slope
- 45 degree slope
- Left and right movement
- Jump available on valid ground
- Jump unavailable while airborne

