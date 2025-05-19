# SMTP-Enumeration
This python script automates the process of scanning targets for open SMTP ports and optionally perform enumeration using nmap

How to Run the SMTP Scanner Script

Filename: smtp_scanner.py
Purpose: Scan a target IP, hostname, or CIDR range for open SMTP ports (25, 465, 587, 2525), and optionally enumerate services and users using Nmap scripts.

---

Prerequisites

1. Python 3 installed
2. Nmap installed and accessible from the command line.
   - On Debian/Ubuntu:  
     sudo apt install nmap
3. The script file should be saved as smtp_scanner.py (or your preferred name).

---

Basic Usage

python3 smtp_scanner.py (target)

- Replace (target) with:
  - An IP address (e.g., 192.168.1.10)
  - A CIDR range (e.g., 192.168.1.0/24)
  - A hostname (e.g., mail.example.com)

---

With Enumeration Enabled

Use the -e or --enum flag to run additional Nmap scripts for SMTP enumeration:

python3 smtp_scanner.py <target> -e

This will include:
- SMTP command enumeration
- User enumeration
- Known vulnerability checks

---

Output

- Results are printed to the terminal.
- A copy of the output is saved to a file named:
  smtp_scan_<target>.txt
  For example, smtp_scan_192.168.1.10.txt

---

Examples

1. Scan a single IP:
   python3 smtp_scanner.py 192.168.1.10

2. Scan with enumeration:
   python3 smtp_scanner.py 192.168.1.10 --enum

3. Scan a CIDR range:
   python3 smtp_scanner.py 10.0.0.0/24

4. Scan a hostname:
   python3 smtp_scanner.py smtp.example.com -e
