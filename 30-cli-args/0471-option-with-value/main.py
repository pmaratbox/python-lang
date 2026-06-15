import click


@click.command()
@click.option("--name")
def cli(name):
    click.echo(name)


# Parse a hardcoded argv list (not real process args) for deterministic output.
cli(["--name", "alice"], standalone_mode=False)
