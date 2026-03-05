#!/bin/bash
set -e
cd "$(dirname "$0")"

if ! command -v weasyprint &> /dev/null; then
  echo "weasyprint not found. Install with: pip install weasyprint"
  exit 1
fi

# Build the Jekyll site
echo "Building Jekyll site..."
PAGES_REPO_NWO=manolosolalinde/cv bundle _2.5.23_ exec jekyll build

# Serve _site/ locally so root-relative asset paths resolve
python3 -m http.server 4000 --directory _site &
SERVER_PID=$!

# Wait for server to be ready
until curl -s http://localhost:4000 > /dev/null; do sleep 1; done

# Generate PDF
echo "Generating PDF..."
weasyprint http://localhost:4000 manuel_solalinde_cv.pdf

kill $SERVER_PID

echo "Done: manuel_solalinde_cv.pdf"
