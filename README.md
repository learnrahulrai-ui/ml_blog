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
- **The `.html` is generated, never committed.** On every push to `main`, a GitHub Actions
  workflow (`.github/workflows/deploy.yml`) runs `python3 build.py` and publishes the result
  to GitHub Pages. You only ever commit `.txt` files; the `.html` is built in the cloud.

## Authoring conventions (inside a `.txt`)

- First line may be `@title Some Page Title` -- used for the HTML `<title>`, then removed.
- Links: `[label](target.txt)` or `[label](https://...)` or `[label](mailto:a@b.c)`.
  A `.txt` target is rewritten to `.html` automatically.
- Callout markers used in posts: `>> NOTE:`, `!! WARN:`, `** KEY:`.
- Everything else is literal text.

## Build

The normal flow is: **edit a `.txt`, commit it, push to `main`.** GitHub Actions builds and
deploys the HTML automatically -- there is nothing to build by hand. You can also trigger a
rebuild manually from the repo's Actions tab ("Deploy to GitHub Pages" -> "Run workflow").

To preview locally before pushing:

```
python3 build.py
```

This rebuilds all pages from `txt/` into the repo root. The generated `.html` is git-ignored,
so it will not show up in `git status` -- it exists only for local preview and is rebuilt
fresh in CI on every push.
