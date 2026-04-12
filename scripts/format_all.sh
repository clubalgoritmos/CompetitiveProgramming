#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

if ! command -v pre-commit >/dev/null 2>&1; then
  echo "[format] pre-commit is not installed."
  echo "[format] Install it with: pip install pre-commit"
  exit 1
fi

echo "[format] Running pre-commit on all files..."
pre-commit run --all-files

echo "[format] Done."
