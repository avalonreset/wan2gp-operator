# Wan2GP Operator Wiki: LLM Wiki

Mode: B plus E
Purpose: Persistent development memory for Wan2GP Operator, including code architecture, release decisions, model research, and agent-operated WanGP workflows.
Owner: Benjamin
Created: 2026-05-10

## Structure

```text
obsidian-wiki/
├── .raw/                 # Immutable source snapshots and session notes
├── _templates/           # Note templates
├── attachments/          # Images, PDFs, and local artifacts
├── wiki/
│   ├── index.md          # Master catalog
│   ├── log.md            # Append-only project wiki log
│   ├── hot.md            # Recent context cache
│   ├── overview.md       # Executive summary
│   ├── modules/          # Code and CLI modules
│   ├── flows/            # Operating workflows
│   ├── decisions/        # Architecture and release decisions
│   ├── dependencies/     # External systems and packages
│   ├── entities/         # Projects, tools, models, runtimes
│   ├── concepts/         # Reusable project concepts
│   ├── domains/          # Top-level topic areas
│   ├── sources/          # Summaries of raw inputs
│   ├── questions/        # Filed answers
│   ├── comparisons/      # Model or workflow comparisons
│   └── meta/             # Dashboards and health reports
└── CODEX.md
```

## Conventions

- All notes use YAML frontmatter with `type`, `title`, `created`, `updated`, `tags`, and `status`.
- Wikilinks use Obsidian double-bracket links with unique filenames.
- `.raw/` contains source snapshots and should not be edited after creation.
- `wiki/index.md` is the master catalog and must be updated when pages are added.
- `wiki/log.md` is append-only. New entries go at the top.
- `wiki/hot.md` is rewritten after major changes and kept under roughly 500 words.
- Use callouts for gaps, stale claims, and key insights.

## Operations

- Start context: read `wiki/hot.md`, then `wiki/index.md`.
- Save a decision: create a page in `wiki/decisions/`, update `Decision Log`, `index.md`, `log.md`, and `hot.md`.
- Add a workflow: create or update a page in `wiki/flows/`.
- Add model research: file sources under `.raw/`, summarize under `wiki/sources/`, synthesize under `wiki/domains/Model Research.md` or `wiki/comparisons/`.
- Lint: create a report in `wiki/meta/`.

## Current Focus

The current project direction is agent-operated WanGP: Codex or Claude uses the
operator to install or update WanGP, choose model targets, compose settings,
dry-run, run headless jobs, capture logs, diagnose failures, and retry with
learned compatibility state.
