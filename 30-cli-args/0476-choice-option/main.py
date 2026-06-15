import click


@click.command()
@click.option("--color", type=click.Choice(["red", "green", "blue"]))
def cli(color):
    click.echo(color)


cli(["--color", "green"], standalone_mode=False)
