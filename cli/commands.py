import click

@click.group()
def cli():
    pass

@cli.command()
def ip():
    click.echo('Running IP reconnaissance')

