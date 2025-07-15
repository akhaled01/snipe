from osint.utils import print_ascii_art
from osint.social import lookup_social
from osint.ip import lookup_ip
import click

@click.group()
@click.option('--gen-pdf', is_flag=True, help='Generate PDF report')
@click.pass_context
def cli(ctx, gen_pdf):
    print_ascii_art()
    ctx.ensure_object(dict)
    ctx.obj['gen_pdf'] = gen_pdf

@cli.command()
@click.argument('ip_address', type=str)
@click.option('--gen-pdf', is_flag=True, help='Generate PDF report')
@click.pass_context
def ip(ctx, ip_address, gen_pdf):
    if gen_pdf:
        ctx.obj['gen_pdf'] = True
    lookup_ip(ip_address, ctx)

@cli.command()
@click.option('--gen-pdf', is_flag=True, help='Generate PDF report')
@click.option('--detailed', is_flag=True, help='Detailed information')
@click.argument('username', type=str)
@click.pass_context
def social(ctx, username, gen_pdf, detailed):
    if gen_pdf:
        ctx.obj['gen_pdf'] = True
    lookup_social(username, ctx, detailed)

@cli.command()
@click.option('--gen-pdf', is_flag=True, help='Generate PDF report')
def name(ctx, gen_pdf):
    if gen_pdf:
        ctx.obj['gen_pdf'] = True

@cli.command()
@click.option('--gen-pdf', is_flag=True, help='Generate PDF report')
def server(ctx, gen_pdf):
    if gen_pdf:
        ctx.obj['gen_pdf'] = True
