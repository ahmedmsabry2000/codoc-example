"""Emit an auto-generated API reference page for messaging.api."""

from pathlib import Path
import ast
import os

root = Path(os.environ["CODOC_ROOT"])
scope = Path(os.environ["CODOC_SCOPE_DIR"])
api_path = root / scope / "api.py"
tree = ast.parse(api_path.read_text(encoding="utf-8"))
routes: list[tuple[str, str]] = []
for node in tree.body:
    if not isinstance(node, ast.FunctionDef):
        continue
    for deco in node.decorator_list:
        if not isinstance(deco, ast.Call):
            continue
        if not isinstance(deco.func, ast.Attribute):
            continue
        method = deco.func.attr.upper()
        if not deco.args:
            continue
        arg = deco.args[0]
        if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
            routes.append((method, arg.value))
print("# API reference")
print()
print("Auto-generated from `messaging.api`.")
print()
if routes:
    print("| Method | Path |")
    print("| --- | --- |")
    for method, path in routes:
        print(f"| `{method}` | `{path}` |")
else:
    print("No routes found.")
