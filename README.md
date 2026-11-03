# Codoc example — messaging API

A small FastAPI messaging app dogfooding [Codoc](https://github.com/ahmedmsabry2000/codoc): one `codoc.yaml`, a nested `src/messaging/codoc.spec.yaml`, and manual / hybrid / auto-generated pages under `docs/`.

Clone: `https://github.com/ahmedmsabry2000/codoc-example`

## Setup

Requires [uv](https://docs.astral.sh/uv/) and Python 3.12+.

```bash
git clone https://github.com/ahmedmsabry2000/codoc-example.git
cd codoc-example
uv sync
# Install Codoc into this venv (editable sibling or PyPI when published):
uv pip install -e ../codoc
uv pip install zensical
```

## App

```bash
uv run uvicorn messaging.api:app --reload
```

Open http://127.0.0.1:8000/docs for the interactive API.

## Docs with Codoc

```bash
uv run codoc status
uv run codoc generate
uv run codoc validate
uv run codoc build
uv run codoc serve
```

Serve prints a local URL (default http://localhost:8000/). Stop with `uv run codoc clean`.

| Page | Type | Path |
|------|------|------|
| Index | manual | `docs/index.md` |
| Messaging guide | hybrid | `docs/guides/messaging.md` |
| Package overview | auto-generated | `docs/package.md` |
| API reference | auto-generated | `docs/reference/api.md` |

Parse/inject scripts live under `.codoc/scripts/`.
