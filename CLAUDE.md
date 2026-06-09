# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install dependencies
bundle install

# Run local dev server (live at http://localhost:4000)
bundle exec jekyll serve

# Build static site
bundle exec jekyll build
```

## Architecture

This is a **Jekyll static site** deployed on GitHub Pages at `https://manolosolalinde.github.io/cv/`.

**Content structure:**
- `index.md` — the main CV page (the site's index/homepage). Has `layout: default` frontmatter; the CV body follows.
- `README.md` — developer-facing repo documentation (stack, layout, dev/PDF commands). Not a published site page (no frontmatter).
- `projects/*.md` — individual project detail pages linked from the main CV
- `projects/images/` — screenshots and images referenced by project pages

**Theming:**
- Uses `jekyll-remote-theme` with `jekyll-theme-minimal` as the base
- `_layouts/default.html` — overrides the theme's default layout, injecting `assets/css/main.css` before the theme stylesheet
- `assets/css/main.css` — custom CSS overrides on top of the minimal theme

**Print support:** page breaks are **automatic** — `assets/css/main.css` has a `@media print` block that keeps headings with their content, keeps each entry's title attached to its bullet list, and avoids splitting a paragraph or list across pages. There are no manual break markers (the old `<span class="print-break">` elements were removed). The compiled PDF is also committed as `manuel_solalinde_cv.pdf`.

## Writing a new project page

Each project is one Markdown file in `projects/<name>.md` with YAML frontmatter, optionally linked from `index.md`. The same files are also consumed by the `workwithmanu.com` Gatsby site (see the parent `../CLAUDE.md`), so keep paths relative.

**Frontmatter schema** (copy an existing page like `projects/bkv_sd.md` as a template):

```yaml
---
title: Plunger Optimization App                    # required — display name
description: One-line summary of the project.       # required — used as the card subtitle
image_url: ./images/<name>/cover.png                # required — RELATIVE path to the cover image
image_url_global: https://raw.githubusercontent.com/manolosolalinde/cv/main/projects/images/<name>/cover.png  # optional — absolute raw URL (workwithmanu/external use)
date: 2025-01-30                                     # required — YYYY-MM-DD
order: 1                                             # required — lower sorts first; current/flagship work uses 1
technologies: Python, Streamlit, AWS, ...           # required — comma-separated string
category: Data Science Development                   # required — e.g. Full Stack / Backend / Data Science Development, Scientific Computing
redirect_link: https://example.com                   # optional — external URL; makes the card link out instead of to the detail page
---
```

**Body conventions:**
- Start with `# <Title> - <Org>`, optionally a `Website:` and `Developer:` line, then a short overview paragraph.
- Use `##`/`####` headings for sections (Overview, Applications, Architecture, Screenshots, etc.).
- **Images** live in `projects/images/<name>/` (one subfolder per project) and are referenced with relative `./images/<name>/...` paths. Use the clickable, enlargeable embed pattern:

  ```html
  <a href="./images/<name>/shot.png">
  <img src="./images/<name>/shot.png" alt="click to enlarge"/>
  </a>
  ```

**Link it from `index.md`:** add an entry in the relevant section following the existing format — `**Title** - [project details](./projects/<name>.md) <br>` plus a short description and bullet points. No page-break markers are needed — PDF page breaks are handled automatically by the print CSS.

**After adding a page:** pushing to `main` updates GitHub Pages automatically; `workwithmanu.com` only reflects it after a manual Netlify redeploy (see parent `../CLAUDE.md`).

## Generating the PDF

Requires `weasyprint` (`pip install weasyprint`) and either a local Ruby/Bundler or Docker, then:

```bash
bash generate_pdf.sh
```

What the script does:
- **Builds the site.** Uses local `bundle _2.5.23_ exec jekyll build` if Bundler is present; otherwise builds inside the `ruby:3.3` container, using the gitignored `.docker-gem-cache/` as the persistent bundle path (`BUNDLE_PATH=/usr/local/bundle`). So no local Ruby install is required as long as Docker is available.
- **Picks a WeasyPrint-capable Python.** It probes `python3`/`python3.12`/`python3.11`/`python3.10` for one that can `import weasyprint`, rather than calling the bare `weasyprint` launcher (whose shebang breaks when the system Python changes, e.g. an Ubuntu 3.10→3.12 upgrade).
- **Serves `_site/` on localhost:4000** so root-relative asset paths resolve, then renders.
- **Rewrites internal links to the public site.** Navigation links are rewritten to `https://manolosolalinde.github.io/cv/...` in the PDF, while assets keep loading from the local server — so links work off-machine but locally-edited CSS is still reflected. (The deployed site already serves correct `/cv/...` links, so PDFs generated from it are unaffected.)
