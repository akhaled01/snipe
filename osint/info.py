import requests
from bs4 import BeautifulSoup
from osint.utils import generate_pdf
from playwright.sync_api import sync_playwright
from rich.console import Console
from rich.table import Table
import urllib.parse


def _display_table(data: dict) -> None:
    table = Table()
    table.add_column("Property", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")
    for key, value in data.items():
        table.add_row(key.title(), str(value))
    console = Console()
    console.print(table)

def google_dork(full_name):
    query = f'"{full_name}" "phone" "address" filetype:pdf'
    url = "https://www.google.com/search?q=" + urllib.parse.quote(query)
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    links = [
        a["href"].split("/url?q=")[-1].split("&")[0]
        for a in soup.select("a[href]")
        if "url?q=" in a["href"]
    ]
    return links[:5]  # limit to first 5 results


def radaris_lookup(full_name, location=""):
    results = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://radaris.com/")
        page.fill("input[name='q']", full_name)
        if location:
            page.fill("input[name='l']", location)
        page.click("button[type='submit']")
        page.wait_for_timeout(20000)
        content = page.content()
        soup = BeautifulSoup(content, "html.parser")
        entries = soup.find_all("div", class_="profile-section")
        for entry in entries:
            text = entry.get_text(separator="\n")
            if "Phone" in text or "Address" in text:
                results.append(text.strip())
        browser.close()
    return results


def name_to_contact(full_name, location="", gen_pdf=False):
    print(f"[+] Looking up: {full_name} {f'in {location}' if location else ''}")
    google_links = google_dork(full_name)
    # radaris_data = radaris_lookup(full_name, location)

    result = {
        "full_name": full_name,
        "location": location,
        "google_sources": google_links,
        # "radaris_results": radaris_data,
    }

    _display_table(result)

    if gen_pdf:
        generate_pdf(result)

