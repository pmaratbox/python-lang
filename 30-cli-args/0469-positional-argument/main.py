import click


@click.command()
@click.argument("name")
def cli(name):
    click.echo(name)


cli(["alice"], standalone_mode=False)
