import click


@click.command()
@click.option("--count", type=int, default=1)
def cli(count):
    click.echo(count)


cli([], standalone_mode=False)
