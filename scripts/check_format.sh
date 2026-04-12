#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

echo "[check] Checking Python format with Black..."
if python -m black --version >/dev/null 2>&1; then
  python -m black --check .
else
  echo "[check] Black is required for Python checks."
  echo "[check] Install it with: pip install black"
  exit 1
fi

if ! command -v clang-format >/dev/null 2>&1; then
  echo "[check] clang-format is required for C/C++ checks."
  exit 1
fi

echo "[check] Checking C/C++ format with clang-format..."
mapfile -d '' files < <(find solutions scripts -type f \( -name "*.c" -o -name "*.cc" -o -name "*.cpp" -o -name "*.h" -o -name "*.hpp" \) -print0)

if [ "${#files[@]}" -gt 0 ]; then
  clang-format --dry-run --Werror "${files[@]}"
fi

echo "[check] Formatting checks passed."
