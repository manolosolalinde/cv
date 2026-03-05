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
