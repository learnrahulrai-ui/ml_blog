# Rahul's ML Blog

A plain-text machine-learning blog, styled like the linux-kernel mailing list /
kernel.org: pure monospace, ASCII diagrams, authored to a 100-column terminal width.
No JavaScript, no web fonts, no frameworks.

Live: https://learnrahulrai-ui.github.io/ml_blog/

## How it works

- **Source of truth is plain text.** Every page lives as a `.txt` file under `txt/`.
  Write normal text, draw diagrams in ASCII, keep lines within 100 columns.
- **`build.py` wraps each `.txt` in a minimal `<pre>` HTML page** so it renders the same
  in any browser while staying readable piped through `less` in a terminal.
- The generated `.html` files (`index.html`, `about.html`, `archive.html`, `posts/*.html`)
  are committed alongside the sources so GitHub Pages can serve them directly.

## Authoring conventions (inside a `.txt`)

- First line may be `@title Some Page Title` -- used for the HTML `<title>`, then removed.
- Links: `[label](target.txt)` or `[label](https://...)` or `[label](mailto:a@b.c)`.
  A `.txt` target is rewritten to `.html` automatically.
- Callout markers used in posts: `>> NOTE:`, `!! WARN:`, `** KEY:`.
- Everything else is literal text.

## Build

```
python3 build.py
```

Rebuilds all pages from `txt/` into the repo root. Commit both the `.txt` sources and the
generated `.html`.
