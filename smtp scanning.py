#!/usr/bin/env python3
import subprocess
import argparse
from ipaddress import ip_network, ip_address

def is_valid_ip(target):
    try:
        ip_address(target)
        return True
    except ValueError:
        return False

def is_valid_cidr(target):
    try:
        ip_network(target, strict=False)
        return True
    except ValueError:
        return False

def run_nmap_scan(target, ports, enum=False):
    print(f"\n[*] Scanning target: {target} for open SMTP ports...")
    
    # Base Nmap command
    command = ['nmap', '-Pn', '-sV', '-p', ports, target]
    
    # Add enumeration options if requested
    if enum:
        command.extend(['--script', 'smtp-commands,smtp-enum-users,smtp-vuln*'])
    
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print(result.stdout)
        
        # Save results to a file
        filename = f"smtp_scan_{target.replace('/', '_')}.txt"
        with open(filename, 'w') as f:
            f.write(result.stdout)
        print(f"[*] Results saved to {filename}")
        
    except subprocess.CalledProcessError as e:
        print(f"[-] Error during Nmap scan: {e.stderr}")
    except Exception as e:
        print(f"[-] An unexpected error occurred: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="SMTP Port Scanner and Enumerator")
    parser.add_argument("target", help="Target IP address, hostname, or CIDR range")
    parser.add_argument("-e", "--enum", action="store_true", 
                        help="Perform SMTP enumeration (commands, users, vulnerabilities)")
    args = parser.parse_args()

    # Validate target
    if not (is_valid_ip(args.target) or is_valid_cidr(args.target)):
        # If not IP/CIDR, assume it's a hostname
        print(f"[*] Assuming {args.target} is a hostname")

    # Common SMTP ports
    smtp_ports = "25,465,587,2525"
    
    # Run the scan
    run_nmap_scan(args.target, smtp_ports, args.enum)

if __name__ == "__main__":
    main()