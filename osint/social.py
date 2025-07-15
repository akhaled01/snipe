from osint.utils import generate_pdf, load_env
from rich.console import Console
from bs4 import BeautifulSoup
from rich.table import Table

import requests
import click
import rich
import os


def _display_table(data: dict) -> None:
    table = Table()
    table.add_column("Property", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")
    for key, value in data.items():
        table.add_row(key.title(), str(value))
    console = Console()
    console.print(table)

def _lookup_reddit(username: str, _detailed: bool) -> bool | None:
    try:
        response = requests.get(f"https://www.reddit.com/user/{username}")
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.find("h1", attrs={"id": "shreddit-forbidden-title"}) is None # If the user is not found, the page will have this element
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            return False
        rich.print(f"Reddit API Error: {e}")
        return None
    except Exception as e:
        rich.print(f"Error: {e}")
        return None

def _lookup_github(username: str, detailed: bool) -> bool | None:
    try:
        response = requests.get(f"https://api.github.com/users/{username}")
        response.raise_for_status()
        data = response.json()
        if detailed:
            rich.print("[bold magenta]Github User Info[/bold magenta]")
            _display_table(data)
        return True
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            return False
        rich.print(f"GitHub API Error: {e}")
        return None
    except Exception as e:
        rich.print(f"Error: {e}")
        return None


def _lookup_twitter(username: str, detailed: bool) -> bool | None:
    try:
        load_env()
        response = requests.get(
            f"https://api.twitter.com/2/users/by/username/{username}",
            headers={
                "Authorization": f"Bearer {os.getenv('TWITTER_API_KEY')}",
            },
        )
        response.raise_for_status()
        data = response.json()
        if detailed:
            if 'errors' in data:
                rich.print("[bold red]Twitter API Error[/bold red]")
                _display_table(data['errors'][0])
                return False
            else:
                rich.print("[bold cyan]Twitter User Info[/bold cyan]")
                _display_table(data)
        return True
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            return False
        rich.print(f"Twitter API Error: {e}")
        return None
    except Exception as e:
        rich.print(f"Error: {e}")
        return None

def _lookup_devto(username: str, detailed: bool) -> bool | None:
    try:
        response = requests.get(f"https://dev.to/{username}")
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.find("img", attrs={"alt": "404 not found"}) is None
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            return False
        rich.print(f"Dev.to API Error: {e}")
        return None
    except Exception as e:
        rich.print(f"Error: {e}")
        return None

def _lookup_instagram(username: str, _detailed: bool) -> bool | None:
    try:
        response = requests.get(f"https://www.instagram.com/{username}")
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        return (
            soup.find("span", string="Sorry, this page isn't available.") is None
        ) # If the user is not found, the page will have this element
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            return False
        rich.print(f"Instagram API Error: {e}")
        return None
    except Exception as e:
        rich.print(f"Error: {e}")
        return None

def lookup_social(username: str, ctx: click.Context, detailed: bool) -> None:
    """
    Lookup social information across multiple platforms.
    Args:
        username (str): Social username to lookup.
        ctx (click.Context): Click context object.
        detailed (bool): Detailed information.
    Returns:
        None
    """
    platforms = {
        "GitHub": _lookup_github,
        "Dev.to": _lookup_devto,
        "Instagram": _lookup_instagram,
        # "Twitter": _lookup_twitter, # this is rate limited, so will stay commented out till audit
        "Reddit": _lookup_reddit,
    }

    results = {}
    pdf_data = {}

    for platform_name, lookup_fn in platforms.items():
        result = lookup_fn(username, detailed)
        if result is True:
            results[platform_name] = "✓ Found"
        elif result is False:
            results[platform_name] = "✗ Not Found"
        elif result is None:
            results[platform_name] = "? Error"
        pdf_data[platform_name] = result

    summary_table = Table(title=f"Social Media Summary for {username}")
    summary_table.add_column("Platform", style="cyan", no_wrap=True)
    summary_table.add_column("Status", style="magenta")

    for platform, status in results.items():
        summary_table.add_row(platform, status)

    console = Console()
    console.print(summary_table)

    if ctx.obj["gen_pdf"]:
        generate_pdf(pdf_data, "social")
