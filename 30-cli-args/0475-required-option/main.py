import click


@click.command()
@click.option("--id", "id_", type=int, required=True)
def cli(id_):
    click.echo(id_)


cli(["--id", "42"], standalone_mode=False)
