#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

echo "[format] Formatting Python with Black..."
if python -m black --version >/dev/null 2>&1; then
  python -m black .
else
  echo "[format] Black is not installed in the current Python environment."
  echo "[format] Install it with: pip install black"
  exit 1
fi

if command -v clang-format >/dev/null 2>&1; then
  echo "[format] Formatting C/C++ with clang-format..."
  while IFS= read -r -d '' file; do
    clang-format -i "$file"
  done < <(find solutions scripts -type f \( -name "*.c" -o -name "*.cc" -o -name "*.cpp" -o -name "*.h" -o -name "*.hpp" \) -print0)
else
  echo "[format] clang-format not found. Skipping C/C++ formatting."
  echo "[format] Install clang-format to enable C/C++ formatting."
fi

echo "[format] Done."
