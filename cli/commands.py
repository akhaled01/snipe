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
@click.option('--gen-pdf', is_flag=True, help='Generate PDF report')
@click.pass_context
def ip(ctx, ip_address, gen_pdf):
    click.echo(f'Running IP reconnaissance for {ip_address}')
    if gen_pdf:
        ctx.obj['gen_pdf'] = True
    lookup_ip(ip_address, ctx)
    if ctx.obj['gen_pdf']:
        click.echo('Generating PDF report...')

@cli.command()
@click.argument('first_name', type=str)
@click.argument('last_name', type=str)
def social(ctx, first_name, last_name):
    click.echo(f'Running social reconnaissance for {first_name} {last_name}')
    if ctx.obj['gen_pdf']:
        click.echo('Generating PDF report...')

@cli.command()
def name():
    click.echo('Running name reconnaissance')

@cli.command()
def server():
    click.echo('Running Api interface')
