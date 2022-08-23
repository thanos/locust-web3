"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Locust Web3 Client."""


if __name__ == "__main__":
    main(prog_name="locust-web3")  # pragma: no cover
