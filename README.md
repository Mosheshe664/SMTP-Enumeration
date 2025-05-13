# SMTP-Enumeration
This python script automates the process of scanning targets for open SMTP ports and optionally perform enumeration using nmap
Basic Information
Script Name: smtp_scanner.py

Purpose: Scan targets for open SMTP ports and optionally perform enumeration

Requirements:

Python 3.x

Nmap installed on your system

Network connectivity to target systems
Basic Usage
python3 smtp_scanner.py [TARGET] [OPTIONS]
Required Argument
TARGET: Can be any of the following:

Single IP address (e.g., 192.168.1.1)

Hostname (e.g., mail.example.com)

CIDR network range (e.g., 192.168.1.0/24)
