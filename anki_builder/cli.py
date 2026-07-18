"""Command line interface for anki-builder."""

import click


@click.command()
@click.version_option()
def main() -> None:
    """Build nice Anki decks."""
    click.echo("anki-builder is ready to build decks.")


if __name__ == "__main__":
    main()
