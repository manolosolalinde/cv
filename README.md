# cv

Jekyll source for Manuel Solalinde's CV, deployed on GitHub Pages.

**Live site:** https://manolosolalinde.github.io/cv/

The CV homepage lives in [`index.md`](./index.md); individual project detail pages live in
[`projects/`](./projects). The same `projects/*.md` files are also consumed by the
[workwithmanu.com](https://workwithmanu.com) portfolio (a separate Gatsby site), so project
image paths are kept **relative** (`./images/...`) — see the parent `../CLAUDE.md` for how
that cross-repo pipeline works.

## Stack

- **Jekyll** static site with `jekyll-remote-theme` on top of `jekyll-theme-minimal`.
- **GitHub Pages** builds and deploys automatically on every push to `main`.

## Repo layout

| Path | Purpose |
| --- | --- |
| `index.md` | The CV homepage (site index). |
| `projects/*.md` | One Markdown file per project, linked from `index.md`. |
| `projects/images/` | Screenshots referenced by project pages. |
| `_layouts/default.html` | Theme layout override (injects `main.css`). |
| `assets/css/main.css` | Custom CSS, including the `@media print` rules for the PDF. |
| `generate_pdf.sh` | Builds the site and renders `manuel_solalinde_cv.pdf` via WeasyPrint. |
| `manuel_solalinde_cv.pdf` | The committed, generated PDF of the CV. |
| `_config.yml` | Jekyll config (theme, site title, description, plugins). |

## Local development

```bash
bundle install
bundle exec jekyll serve   # live at http://localhost:4000
```

To build the static site without serving:

```bash
bundle exec jekyll build   # output in _site/
```

## Generating the PDF

Requires `weasyprint` (`pip install weasyprint`) and either a local Ruby/Bundler or Docker:

```bash
bash generate_pdf.sh
```

The script builds the site (locally or in a `ruby:3.3` container), serves `_site/` on
`localhost:4000` so asset paths resolve, rewrites internal navigation links to the public
GitHub Pages URLs, and renders `manuel_solalinde_cv.pdf`.

## Adding or editing content

See [`CLAUDE.md`](./CLAUDE.md) for the project-page frontmatter schema, image conventions,
and how page breaks are handled in print/PDF.
