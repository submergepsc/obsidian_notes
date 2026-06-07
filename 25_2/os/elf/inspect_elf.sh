#!/usr/bin/env bash
set -euo pipefail
target="${1:-hello_elf}"
if [[ ! -f "$target" ]]; then
    echo "missing ELF file: $target" >&2
    echo "run: make" >&2
    exit 1
fi
echo "== file =="
file "$target"
echo
echo "== ELF header =="
readelf -h "$target"
echo
echo "== Section headers =="
readelf -S "$target" | sed -n '1,45p'
echo
echo "== Symbols about main/add/message/global_counter =="
readelf -s "$target" | grep -E ' main$| add$| message$| global_counter$' || true
echo
echo "== Disassembly around main =="
objdump -d "$target" | sed -n '/<main>:/,+35p'
