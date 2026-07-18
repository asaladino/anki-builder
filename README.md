# anki-builder

A tool for building nice Anki decks.

## GitHub Codespaces setup

Install the project dependencies with Poetry from the repository root:

```bash
poetry install
```

This repository configures Poetry to create the virtual environment at `.venv/`. After `poetry install` completes, choose the `.venv/bin/python` interpreter in VS Code/Codespaces so the editor can resolve imports for installed dependencies such as `click`:

1. Open the command palette.
2. Run **Python: Select Interpreter**.
3. Select the interpreter at `.venv/bin/python`.

Run the CLI with Poetry:

```bash
poetry run anki-builder --help
poetry run anki-builder
```

You can also run the module directly:

```bash
poetry run python -m anki_builder.cli --help
```
