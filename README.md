# anki-builder

A tool for building nice Anki decks.

## GitHub Codespaces setup

Install the project dependencies with Poetry from the repository root:

```bash
poetry install
```

This repository configures Poetry to create the virtual environment at `.venv/`, and VS Code is configured to use `.venv/bin/python` as its Python interpreter. After `poetry install` completes, the Codespaces editor should be able to resolve imports for installed dependencies such as `click`.

Run the CLI with Poetry:

```bash
poetry run anki-builder --help
poetry run anki-builder
```

You can also run the module directly:

```bash
poetry run python -m anki_builder.cli --help
```
