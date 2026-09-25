# Installing

This repository follows the portable Agent Skills layout.

## Local installation

Copy the repository directory into the skills directory used by your agent, preserving the folder name:

    new-project-architecture/
    └── SKILL.md

The folder name and the name field in SKILL.md must both be new-project-architecture.

## Use

Invoke the skill explicitly when supported:

    $new-project-architecture

Or describe a new project and ask the agent to design the domain model, layers, interfaces, dependencies, and acceptance criteria before coding.

## Compatibility

The core skill uses only SKILL.md, Markdown references, templates, and standard filesystem paths. It does not require an MCP server, a proprietary SDK, or a specific coding agent.
