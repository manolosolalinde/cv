#!/bin/bash
set -e
cd "$(dirname "$0")"

# Public base URL of the deployed CV (GitHub Pages). Internal navigation links
# in the PDF are rewritten to this so they work for anyone opening the file,
# instead of pointing at the local build server.
SITE_URL="https://manolosolalinde.github.io/cv"

# --- Locate a Python that can import WeasyPrint ---
# We render via the Python API (not the CLI) so we can rewrite links first.
# The bare `weasyprint` launcher can also break if the system python it points
# at changes (e.g. an Ubuntu upgrade from 3.10 -> 3.12), so probe explicitly.
PY=""
for py in python3 python3.12 python3.11 python3.10; do
  if command -v "$py" &> /dev/null && "$py" -c "import weasyprint" &> /dev/null; then
    PY="$py"
    break
  fi
done
if [ -z "$PY" ]; then
  echo "WeasyPrint (Python module) not found. Install with: pip install weasyprint"
  exit 1
fi

# --- Build the Jekyll site ---
# Prefer a local Ruby/Bundler (GitHub-Pages-style setup). If none is present,
# build inside the ruby:3.3 container using the gitignored .docker-gem-cache as
# the persistent bundle path (BUNDLE_PATH=/usr/local/bundle).
echo "Building Jekyll site..."
if command -v bundle &> /dev/null; then
  PAGES_REPO_NWO=manolosolalinde/cv bundle _2.5.23_ exec jekyll build
elif command -v docker &> /dev/null; then
  docker run --rm \
    -v "$PWD":/srv/jekyll \
    -v "$PWD/.docker-gem-cache":/usr/local/bundle \
    -w /srv/jekyll \
    -e PAGES_REPO_NWO=manolosolalinde/cv \
    ruby:3.3 sh -c '
      git config --global --add safe.directory /srv/jekyll
      gem install bundler -v 2.5.23 --conservative --no-document
      bundle _2.5.23_ check || bundle _2.5.23_ install
      bundle _2.5.23_ exec jekyll build
    '
else
  echo "Need either 'bundle' (Ruby) or 'docker' to build the site."
  exit 1
fi

# Serve _site/ locally so root-relative asset paths resolve
python3 -m http.server 4000 --directory _site &
SERVER_PID=$!
trap 'kill $SERVER_PID 2>/dev/null' EXIT

# Wait for server to be ready
until curl -s http://localhost:4000 > /dev/null; do sleep 1; done

# Generate PDF.
# Assets are loaded from the local server (so locally-edited CSS/page breaks are
# reflected), but internal navigation links are rewritten to the public
# GitHub Pages URLs so they work outside this machine. The deployed site already
# serves correct /cv/... links, so PDFs generated from it are unaffected.
echo "Generating PDF..."
SITE_URL="$SITE_URL" "$PY" - <<'PYEOF'
import os, re, urllib.request
from weasyprint import HTML

local = "http://localhost:4000/"
prod = os.environ["SITE_URL"].rstrip("/")  # e.g. https://manolosolalinde.github.io/cv

html = urllib.request.urlopen(local).read().decode("utf-8")

# Root-relative refs that are ASSETS stay local (served by localhost); everything
# else root-relative is internal navigation and is pointed at the public site.
ASSET = re.compile(r'^/(?:cv/)?(?:assets/|fonts/|favicon\.ico)')

def rewrite(m):
    attr, url = m.group(1), m.group(2)
    if ASSET.match(url):
        return m.group(0)                      # keep loading from local server
    path = url[3:] if url.startswith("/cv/") else url   # normalize any /cv prefix
    return f'{attr}="{prod}{path}"'

html = re.sub(r'(href|src)="(/[^"]*)"', rewrite, html)

HTML(string=html, base_url=local).write_pdf("manuel_solalinde_cv.pdf")
print("Done: manuel_solalinde_cv.pdf")
PYEOF

kill $SERVER_PID
