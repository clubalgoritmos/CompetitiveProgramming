#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

if ! command -v pre-commit >/dev/null 2>&1; then
  echo "[check] pre-commit is required."
  echo "[check] Install it with: pip install pre-commit"
  exit 1
fi

echo "[check] Running pre-commit checks on all files..."
pre-commit run --all-files --show-diff-on-failure

echo "[check] Formatting checks passed."
