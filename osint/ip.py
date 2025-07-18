from rich.traceback import install
from rich.table import Table
from rich.console import Console
from osint.utils import generate_pdf
import requests
import click
import rich
import re

install()

def _validate_ip_format(ip: str) -> bool:
    pattern = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return bool(re.match(pattern, ip))


def _display_table(data: dict) -> None:
    table = Table(title="IP Information")
    table.add_column("Property", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")
    for key, value in data.items():
        table.add_row(key.title(), str(value))
    console = Console()
    console.print(table)

def lookup_ip(ip: str, ctx: click.Context) -> None:
    """
    Lookup IP information using ipinfo.io API.
    Args:
        ip (str): IP address to lookup.
        ctx (click.Context): Click context object.
    Returns:
        None
    """
    if not _validate_ip_format(ip):
        rich.print(f"Error: Invalid IP address format: {ip}")
        return
    try:
        response = requests.get(f"https://ipinfo.io/{ip}")
        response.raise_for_status()
        data = response.json()
        _display_table(data)
        if ctx.obj['gen_pdf']:
            generate_pdf(data, 'ip')
    except Exception as e:
        rich.print(f"Error: {e}")
        return