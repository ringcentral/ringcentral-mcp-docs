"""Exposes each skill's canonical SKILL.md as a downloadable static asset.

Every skill page links to a "Download SKILL.md" button so visitors can save
the exact source file used by skills/<skill-id>/SKILL.md to their own
computer. MkDocs converts any *.md file it finds under docs_dir into a themed
HTML page, so we can't just drop a copy into docs/ with a .md extension --
it would get rendered instead of served raw. Copying it with a .md.txt
extension keeps MkDocs treating it as a plain static file (copied byte-for-
byte, no processing), while the `download="<skill-id>-SKILL.md"` attribute
on each link restores the correct filename when the browser saves it.

This runs on every build/serve, so the copies always match the current
skills sources -- nothing here needs to be hand-maintained.

IMPORTANT: this writes into site_dir (the *build output*), not docs_dir (the
*source*), and does so in on_post_build rather than on_pre_build. `mkdocs
serve` watches docs_dir for changes and rebuilds on every write there. If
this hook wrote its copies into docs_dir instead, every rebuild would
re-touch docs/assets/skill-downloads/*.md.txt, which the watcher would see
as a new change, triggering another rebuild, which touches those files
again -- an infinite restart loop. Writing to site_dir after the build
completes sidesteps that: site_dir is never watched, so these copies can
never trigger a rebuild. Since every skill page links to this asset with a
path that's relative to the built page (e.g.
`../assets/skill-downloads/<skill-id>.md.txt`), the link resolves the same
way regardless of whether the file was copied into docs_dir pre-build or
site_dir post-build -- so nothing else needs to change.
"""
from pathlib import Path
import shutil


def on_post_build(config):
    project_root = Path(config["config_file_path"]).parent
    skill_library_dir = project_root / "skills"
    if not skill_library_dir.exists():
        return

    dest_dir = Path(config["site_dir"]) / "assets" / "skill-downloads"
    dest_dir.mkdir(parents=True, exist_ok=True)

    for skill_md in sorted(skill_library_dir.glob("*/SKILL.md")):
        skill_id = skill_md.parent.name
        shutil.copyfile(skill_md, dest_dir / f"{skill_id}.md.txt")
