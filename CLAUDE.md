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
- `README.md` — the main CV page (rendered as the site's index by GitHub Pages)
- `projects/*.md` — individual project detail pages linked from the main CV
- `projects/images/` — screenshots and images referenced by project pages

**Theming:**
- Uses `jekyll-remote-theme` with `jekyll-theme-minimal` as the base
- `_layouts/default.html` — overrides the theme's default layout, injecting `assets/css/main.css` before the theme stylesheet
- `assets/css/main.css` — custom CSS overrides on top of the minimal theme

**Print support:** `README.md` uses `<span class="print-break">` elements (hidden on screen) to control page breaks when printing/saving as PDF. The compiled PDF is also committed as `manuel_solalinde_cv.pdf`.

## Writing a new project page

Each project is one Markdown file in `projects/<name>.md` with YAML frontmatter, optionally linked from `README.md`. The same files are also consumed by the `workwithmanu.com` Gatsby site (see the parent `../CLAUDE.md`), so keep paths relative.

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

**Link it from `README.md`:** add an entry in the relevant section following the existing format — `**Title** - [project details](./projects/<name>.md) <br>` plus a short description and bullet points. Insert `<span class="print-break"></span>` between entries where a PDF page break is wanted.

**After adding a page:** pushing to `main` updates GitHub Pages automatically; `workwithmanu.com` only reflects it after a manual Netlify redeploy (see parent `../CLAUDE.md`).

## Generating the PDF

Requires `weasyprint` (`pip install weasyprint`), then:

```bash
bash generate_pdf.sh
```

The script runs `jekyll build`, serves `_site/` on localhost:4000 (needed so root-relative asset paths resolve), runs WeasyPrint against it, then stops the server. Bundler 2.5.23 is required (`gem install bundler -v 2.5.23`).
