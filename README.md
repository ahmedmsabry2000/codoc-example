# Codoc example — messaging API

A small FastAPI messaging app used as a **pre-Codoc baseline**. It is a normal Python package with no Codoc config yet, so you can install Codoc later and see what `codoc init` adds.

## Setup

Requires [uv](https://docs.astral.sh/uv/) and Python 3.12+.

```bash
uv sync
```

## Run

```bash
uv run uvicorn messaging.api:app --reload
```

Or:

```bash
uv run python -m messaging
```

Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for the interactive API.

## API

| Method | Path | Behavior |
|--------|------|----------|
| `POST` | `/conversations` | Create a conversation (`title` optional) |
| `GET` | `/conversations` | List conversations |
| `GET` | `/conversations/{id}` | Get one conversation |
| `POST` | `/conversations/{id}/messages` | Send a message (`sender`, `body`) |
| `GET` | `/conversations/{id}/messages` | List messages in order |

Data lives in memory and resets when the process stops.
