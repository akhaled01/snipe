# OSINT-Master – Project Plan

## 📌 Overview

**Objective**: Build a multi-functional Open Source Intelligence (OSINT) tool that performs passive reconnaissance on publicly available data, using a CLI interface.

The tool must support queries on:
- Full Names
- IP Addresses
- Usernames
- Domains (and their subdomains)

## 🧰 Tech Stack

- **Language**: Python 3.11+
- **Package Manager**: [uv](https://github.com/astral-sh/uv)
- **CLI Interface**: click
- **Networking / APIs**: requests, httpx
- **Web Scraping**: BeautifulSoup4, playwright (optional)
- **DNS and IP Lookup**: dnspython, ipwhois
- **PDF Generation**: fpdf or pdfkit
- **GUI (Bonus)**: tkinter or PySide6
- **Packaging**: pyinstaller (optional)
- **Testing**: pytest
- **Logging**: logging (built-in)
- **Output Format**: txt, json, pdf

## 🗂 Folder Structure

osintmaster/
├── cli/                 # CLI interface
│   └── main.py
├── core/                # Core feature modules
│   ├── name.py
│   ├── ip.py
│   ├── username.py
│   ├── domain.py
│   └── utils.py
├── gui/                 # GUI app (Bonus)
│   └── app.py
├── output/              # Exported reports
├── tests/               # Unit tests
│   └── test\_\*.py
├── README.md
├── PROJECT\_PLAN.md
├── requirements.txt
└── pyproject.toml       # Optional metadata


## 🧱 Project Phases

### 1. ✅ Initialization
- [ ] Set up project folder
- [ ] Initialize with `uv`
- [ ] Create `requirements.txt` using `uv pip compile`
- [ ] Set up CLI scaffold using `click`

### 2. 🧩 Input Handling
- [ ] Add CLI flags: `-n`, `-i`, `-u`, `-d`, `-o`
- [ ] Implement input validation
- [ ] Handle output file generation

### 3. 🔍 Core Features

#### Full Name
- [ ] Extract first/last name
- [ ] Lookup related data (social profiles, phone, address)

#### IP Address
- [ ] Perform geolocation, ASN lookup
- [ ] Detect abuse history

#### Username
- [ ] Check availability on 5+ platforms
- [ ] Fetch public metadata (bio, followers, activity)

#### Domain & Subdomains
- [ ] Subdomain enumeration
- [ ] Resolve IP and SSL cert details
- [ ] Check for subdomain takeover

### 4. 🧾 Output Management
- [ ] Export all results to `.txt`
- [ ] Create optional JSON export
- [ ] Structure output directory

### 5. 🌟 Bonus Features

#### GUI
- [ ] Design simple GUI using `tkinter` or `PySide6`
- [ ] Interface with core modules
- [ ] Add file input/output in GUI

#### PDF Generation
- [ ] Implement `.pdf` export using `fpdf` or `pdfkit`
- [ ] Style reports professionally

### 6. 🧪 Testing
- [ ] Add tests for all modules using `pytest`
- [ ] Include edge cases and invalid input tests

### 7. 🚦 Finalization
- [ ] Add CLI help message and usage examples
- [ ] Create a clean README.md with:
  - Installation instructions
  - Usage examples
  - API notes (if needed)
  - Ethical/legal disclaimer

### 8. 🧑‍🏫 Roleplay Prep
- [ ] Prepare answers for audit questions:
  - What is subdomain takeover?
  - How to detect and prevent it?
  - Ethical and legal constraints of OSINT
  - Privacy-respecting practices

## ⚖️ Ethical & Legal Checklist

- [ ] Get explicit permission before using real user data
- [ ] Only collect necessary public information
- [ ] Respect platform API terms
- [ ] Follow laws (GDPR, CFAA)
- [ ] Do not store or share sensitive data
- [ ] Use only for educational or internal testing

## 💡 Usage Examples

```bash
$ snipe -n "John Doe" -o result1.txt
$ snipe -i 8.8.8.8 -o result2.txt
$ snipe -u "@johndoe" -o result3.txt
$ snipe -d "example.com" -o result4.txt
```