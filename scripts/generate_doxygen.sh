#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

if ! command -v doxygen >/dev/null 2>&1; then
  echo "doxygen is not installed or not on PATH. Install from https://www.doxygen.nl/download.html" >&2
  exit 1
fi

doxygen Doxyfile
echo "Documentation generated: $ROOT/docs/doxygen/html/index.html"
