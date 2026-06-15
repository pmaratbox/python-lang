import click


@click.group()
def cli():
    pass


@cli.command()
@click.argument("a", type=int)
@click.argument("b", type=int)
def add(a, b):
    click.echo(a + b)


cli(["add", "2", "3"], standalone_mode=False)
