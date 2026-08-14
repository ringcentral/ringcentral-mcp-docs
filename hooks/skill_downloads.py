"""Exposes each skill's canonical SKILL.md as a downloadable static asset.

Every skill page links to a "Download SKILL.md" button so visitors can save
the exact source file used by skill-library/<skill-id>/SKILL.md to their own
computer. MkDocs converts any *.md file it finds under docs_dir into a themed
HTML page, so we can't just drop a copy into docs/ with a .md extension --
it would get rendered instead of served raw. Copying it with a .md.txt
extension keeps MkDocs treating it as a plain static file (copied byte-for-
byte, no processing), while the `download="<skill-id>-SKILL.md"` attribute
on each link restores the correct filename when the browser saves it.

This runs on every build/serve, so the copies always match the current
skill-library sources -- nothing here needs to be hand-maintained.
"""
from pathlib import Path
import shutil


def on_pre_build(config):
    project_root = Path(config["config_file_path"]).parent
    skill_library_dir = project_root / "skill-library"
    if not skill_library_dir.exists():
        return

    dest_dir = Path(config["docs_dir"]) / "assets" / "skill-downloads"
    dest_dir.mkdir(parents=True, exist_ok=True)

    for skill_md in sorted(skill_library_dir.glob("*/SKILL.md")):
        skill_id = skill_md.parent.name
        shutil.copyfile(skill_md, dest_dir / f"{skill_id}.md.txt")
