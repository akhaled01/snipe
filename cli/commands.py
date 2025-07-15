import click
from osint.ip import lookup_ip

@click.group()
@click.option('--gen-pdf', is_flag=True, help='Generate PDF report')
@click.pass_context
def cli(ctx, gen_pdf):
    ctx.ensure_object(dict)
    ctx.obj['gen_pdf'] = gen_pdf

@cli.command()
@click.argument('ip_address', type=str)
@click.pass_context
def ip(ctx, ip_address):
    click.echo(f'Running IP reconnaissance for {ip_address}')
    lookup_ip(ip_address)
    if ctx.obj['gen_pdf']:
        click.echo('Generating PDF report...')

@cli.command()
def domain():
    click.echo('Running subdomain enumeration')

@cli.command()
def social():
    click.echo('Running social reconnaissance')

@cli.command()
def name():
    click.echo('Running name reconnaissance')

@cli.command()
def server():
    click.echo('Running Api interface')
