#!/bin/bash
set -e

if ! command -v wkhtmltopdf &> /dev/null; then
  echo "wkhtmltopdf not found. Install with: sudo apt install wkhtmltopdf"
  exit 1
fi

# Start Jekyll server in background
bundle exec jekyll serve --detach

# Wait for server to be ready
echo "Waiting for Jekyll server..."
until curl -s http://localhost:4000 > /dev/null; do sleep 1; done

# Generate PDF
wkhtmltopdf \
  --print-media-type \
  --no-background \
  --margin-top 10 \
  --margin-bottom 10 \
  --margin-left 10 \
  --margin-right 10 \
  http://localhost:4000 \
  manuel_solalinde_cv.pdf

echo "PDF saved to manuel_solalinde_cv.pdf"

# Stop Jekyll server
pkill -f "jekyll serve" || true
