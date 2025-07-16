from osint.utils import generate_pdf, gen_rand_phone, gen_rand_address
from rich.console import Console
from rich.table import Table


def _display_table(data: dict) -> None:
    table = Table()
    table.add_column("Property", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")
    for key, value in data.items():
        table.add_row(key.title(), str(value))
    console = Console()
    console.print(table)


def name_to_contact(full_name, gen_pdf=False):
    print(f"[+] Looking up: {full_name}")

    result = {
        "first_name": full_name.split(" ")[0],
        "last_name": full_name.split(" ")[1],
        "phone": gen_rand_phone(),
        "address": gen_rand_address(),
    }

    _display_table(result)

    if gen_pdf:
        generate_pdf(result)
