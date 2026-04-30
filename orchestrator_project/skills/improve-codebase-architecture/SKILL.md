---
name: improve-codebase-architecture
description: Finds opportunities to deepen shallow modules, improve locality, and make the codebase easier to test and navigate. Use for architecture review or refactoring strategy.
---

# Improve Codebase Architecture

Surface deepening opportunities: changes that move complexity behind smaller,
more useful interfaces.

## Vocabulary

- Module: anything with an interface and implementation.
- Interface: everything callers must know to use the module correctly.
- Depth: leverage at the interface.
- Seam: where an interface lives.
- Adapter: a concrete thing satisfying an interface at a seam.
- Locality: change and verification concentrated in one place.

## Process

1. Read domain language and ADRs.
2. Find shallow modules and leaky seams.
3. Apply the deletion test.
4. Present numbered candidates with files, problem, solution, and benefits.
5. Explore one candidate at a time with the user before proposing interfaces.

