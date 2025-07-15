from datetime import datetime
from fpdf import FPDF
import dotenv
import os

def create_report_dir() -> None:
    if not os.path.exists("reports"):
        os.makedirs("reports")

def generate_pdf(data: dict, command: str) -> None:
    create_report_dir()
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 12)
    for key, value in data.items():
        pdf.cell(200, 10, txt = f"{key}: {value}", ln = True)
    pdf.output(f"reports/{command}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.pdf")


def load_env() -> None:
    dotenv.load_dotenv()


def print_ascii_art() -> None:
    print("""
                      ░██                      
                                                
 ░███████  ░████████  ░██░████████   ░███████  
░██        ░██    ░██ ░██░██    ░██ ░██    ░██ 
 ░███████  ░██    ░██ ░██░██    ░██ ░█████████ 
       ░██ ░██    ░██ ░██░███   ░██ ░██        
 ░███████  ░██    ░██ ░██░██░█████   ░███████  
                         ░██                   
                         ░██                   
                                                """)