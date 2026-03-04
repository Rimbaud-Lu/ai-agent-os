# AI Agent OS

AI Software Factory powered by OpenClaw + Claude Planner + Codex Execution.

## Architecture

User → OpenClaw → Planner → Agent Teams → Execution → Review → Repo Generator

## Features

- Plugin model system
- Multi-agent runtime
- Workflow engine
- Vector RAG
- Repo generator
- Token optimizer
- CLI + Dashboard

## Run

pip install -r requirements.txt
uvicorn openclaw.api.server:app --reload
