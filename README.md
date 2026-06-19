# Python Vulnerability Scanner

A simple Vulnerability Scanner built using Python and the Socket library. This project scans a target host for common open ports, identifies running services, detects basic security risks, and generates a vulnerability report.

## Features

- Scans common ports on a target system
- Identifies running services
- Detects basic vulnerabilities
- Calculates risk level (Low, Medium, High)
- Generates a report file (`report.txt`)
- Beginner-friendly Python project

## Technologies Used

- Python 3
- Socket Programming

## Ports Scanned

| Port | Service |
|--------|---------|
| 21 | FTP |
| 22 | SSH |
| 23 | Telnet |
| 25 | SMTP |
| 53 | DNS |
| 80 | HTTP |
| 110 | POP3 |
| 143 | IMAP |
| 443 | HTTPS |
| 3306 | MySQL |

## Vulnerability Checks

The scanner currently identifies:

- FTP (Port 21)
  - Unencrypted communication

- Telnet (Port 23)
  - Insecure protocol

- MySQL (Port 3306)
  - Database exposed publicly

## Risk Assessment

| Vulnerabilities Found | Risk Level |
|----------------------|------------|
| 0 | Low |
| 1-2 | Medium |
| 3 or more | High |

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/python-vulnerability-scanner.git
```

Navigate to the project folder:

```bash
cd python-vulnerability-scanner
```

## Usage

Run the program:

```bash
python scanner.py
```

Example:

```text
Welcome to Vulnerability Scanner
Enter IP address or website: scanme.nmap.org

Scanning...

Port 22 OPEN
Port 80 OPEN

Services Found

22 - SSH
80 - HTTP

Risk Level: Low

Report saved as report.txt
```

## Output Report

A file named `report.txt` is automatically generated.

Example:

```text
VULNERABILITY REPORT
====================

Target: scanme.nmap.org

Open Ports
22 - SSH
80 - HTTP

Vulnerabilities

Risk Level: Low
```

## Project Structure

```text
Python-Vulnerability-Scanner/
│
├── scanner.py
├── report.txt
└── README.md
```

## Learning Objectives

This project helps understand:

- Socket Programming
- Port Scanning
- Network Services
- Vulnerability Assessment Basics
- File Handling in Python
- Risk Classification

## Disclaimer

This tool is created for educational purposes only. Use it only on systems that you own or have explicit permission to test. Unauthorized scanning of networks may violate laws and regulations.

## Author

**Nagarajan M**

Diploma in Computer Engineering  
Cybersecurity & Python Enthusiast
