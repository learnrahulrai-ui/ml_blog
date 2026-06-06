#!/usr/bin/env python3
"""
Plain-text blog builder.

Source of truth = .txt files under txt/.  Each is wrapped in a minimal <pre>
HTML page so it renders like a kernel.org / LKML plain-text page in any browser,
while staying readable as raw text in a terminal (curl | less).

Conventions inside a .txt file:
  - First line may be:  @title Some Page Title   (used for <title>, then removed)
  - Links:              [label](target.txt)  or  [label](https://...)  or
                        [label](mailto:a@b.c)
                        A .txt target is rewritten to .html automatically.
  - Everything else is literal text. Authored to <= 100 columns.

Run:  python3 build.py
Outputs .html next to where each .txt maps (txt/index.txt -> index.html,
txt/posts/foo.txt -> posts/foo.html).
"""

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "txt"

LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<link rel="stylesheet" href="{css}">
</head>
<body>
<pre>{body}</pre>
</body>
</html>
"""


def render_links(text: str) -> str:
    """Replace [label](target) with <a> tags. .txt targets -> .html."""
    def repl(m: "re.Match[str]") -> str:
        label, target = m.group(1), m.group(2)
        if target.endswith(".txt"):
            target = target[:-4] + ".html"
        return f'<a href="{target}">{label}</a>'
    return LINK_RE.sub(repl, text)


def build_one(txt_path: Path) -> Path:
    raw = txt_path.read_text(encoding="utf-8")
    lines = raw.split("\n")

    title = txt_path.stem
    if lines and lines[0].startswith("@title "):
        title = lines[0][len("@title "):].strip()
        lines = lines[1:]
    body_text = "\n".join(lines)

    # Escape HTML special chars first, then lay links over the escaped text.
    escaped = html.escape(body_text, quote=False)
    body = render_links(escaped)

    rel = txt_path.relative_to(SRC)
    out_path = ROOT / rel.with_suffix(".html")
    depth = len(rel.parts) - 1
    css = ("../" * depth) + "style.css"

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        TEMPLATE.format(title=html.escape(title), css=css, body=body),
        encoding="utf-8",
    )
    return out_path


def main() -> None:
    if not SRC.is_dir():
        raise SystemExit(f"no source dir: {SRC}")
    built = [build_one(p) for p in sorted(SRC.rglob("*.txt"))]
    for p in built:
        print(f"built {p.relative_to(ROOT)}")
    print(f"\n{len(built)} page(s) built.")


if __name__ == "__main__":
    main()
