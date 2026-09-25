import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
skill = ROOT / "SKILL.md"
text = skill.read_text(encoding="utf-8")
if not text.startswith("---\n"):
    raise SystemExit("SKILL.md must start with YAML frontmatter")
frontmatter = text.split("---\n", 2)
if len(frontmatter) < 3:
    raise SystemExit("SKILL.md frontmatter is not closed")
name = re.search(r"^name:\s*([a-z0-9-]+)\s*$", frontmatter[1], re.M)
description = re.search(r"^description:\s.+$", frontmatter[1], re.M)
if not name or not description:
    raise SystemExit("frontmatter must contain name and description")
if name.group(1) != ROOT.name:
    raise SystemExit("frontmatter name must match the directory")
required = ["## Scope", "## Workflow", "## Output", "## Design rules", "## Completion"]
for heading in required:
    if heading not in text:
        raise SystemExit(f"missing section: {heading}")
if re.search(r"\b(TODO|TBD|FIXME)\b", text, re.I):
    raise SystemExit("unfinished placeholder found")
for relative in ["references/domain-design.md", "references/layer-design.md", "references/module-interface.md", "templates/architecture-brief.md", "templates/acceptance-matrix.md"]:
    if not (ROOT / relative).is_file():
        raise SystemExit(f"missing resource: {relative}")
print("new-project-architecture: valid")
