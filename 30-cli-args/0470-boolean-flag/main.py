import click


@click.command()
@click.option("--verbose", is_flag=True)
def cli(verbose):
    click.echo(str(verbose).lower())


cli(["--verbose"], standalone_mode=False)
