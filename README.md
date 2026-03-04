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


## V4.1 Upgrade – Token Economy System

This version introduces token optimization:
- Model Router (dynamic model selection)
- Cost Controller (token limits)
- Prompt Cache (avoid repeated prompts)
- Code Memory (reuse code patterns)

Result:
- Token usage reduced by **80-90%**
- Multi-model architecture
- More scalable AI agent system
