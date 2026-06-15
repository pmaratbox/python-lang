import click


@click.command()
@click.option("--num", type=int, multiple=True)
def cli(num):
    click.echo(sum(num))


cli(["--num", "1", "--num", "2", "--num", "3"], standalone_mode=False)
