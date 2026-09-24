"""Contrôle local reproductible : liens internes, syntaxe Python, SVG et chapitres."""

import ast
import re
from pathlib import Path
from urllib.parse import unquote
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
errors = []
markdown = list(ROOT.rglob("*.md"))
for path in markdown:
    content = path.read_text(encoding="utf-8")
    for target in re.findall(r"\]\(([^)]+)\)", content):
        if target.startswith(("https://", "http://", "#", "mailto:")):
            continue
        relative = unquote(target.split("#")[0])
        if not (path.parent / relative).exists():
            errors.append(f"{path.name} : cible absente {target}")
    for block in re.findall(r"```python\n(.*?)```", content, re.S):
        try:
            ast.parse(block)
        except SyntaxError as error:
            errors.append(f"{path.name} : bloc Python : {error}")
scripts = list(ROOT.rglob("*.py"))
for path in scripts:
    ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
figures = list((ROOT / "images").glob("*.svg"))
for path in figures:
    ET.parse(path)
chapters = list((ROOT / "chapitres").glob("*.md"))
assert len(chapters) == 14 and len(figures) == 14
for path in chapters:
    content = path.read_text(encoding="utf-8")
    assert "../images/" in content and "## TP " in content, path
if errors:
    raise SystemExit("\n".join(errors))
print(
    f"OK : {len(markdown)} Markdown, {len(scripts)} scripts Python, 14 chapitres, 14 SVG ; liens internes résolus."
)
