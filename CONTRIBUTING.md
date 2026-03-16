# Contributing

Contributions are welcome. See the guidelines below before submitting a PR.

## Ground Rules

- Keep changes deterministic and script-first.
- Prefer additive improvements over broad rewrites.
- Preserve CLI stability of `scripts/wan2gp_operator.py`.

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/avalonreset/wan2gp-operator-skill.git
   cd wan2gp-operator-skill
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate     # Windows
   ```

3. Verify scripts compile:
   ```bash
   python -m py_compile scripts/*.py
   ```

## Code Style

- Follow PEP 8 conventions
- Use [Ruff](https://docs.astral.sh/ruff/) for linting: `ruff check .`
- Keep functions focused and small
- Add docstrings to new modules and public functions

## Local Validation

Use the Wan2GP venv when available:

```bash
python -m py_compile scripts/*.py
python scripts/wan2gp_operator.py compose --prompt "smoke test" --quality balanced --duration-seconds 2
```

For run-path updates, always validate:

1. Dry-run path
2. Full run path
3. Failure diagnosis path
4. Evolve path

## Pull Request Process

1. Create a feature branch from `main`
2. Make your changes with clear, focused commits
3. Run `python -m py_compile scripts/*.py` before pushing
4. Open a PR using the [PR template](.github/PULL_REQUEST_TEMPLATE.md)
5. Follow the [Code of Conduct](CODE_OF_CONDUCT.md)

## Pull Request Focus

- Bug + risk first
- Repro command
- Before/after behavior
- Any new defaults and tradeoffs
