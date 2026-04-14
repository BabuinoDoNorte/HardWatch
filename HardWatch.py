import subprocess
import os
import sys

RED   = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"
RESET = "\033[0m"

passed = 0 
failed = 0
warning = 0

def report (status, message):
    global passed, failed, warning 
    if status == "ok":
        print(f"  {GREEN}[✓]{RESET} {message}")
        passed += 1
    elif status == "fail":
        print(f"  {RED}[✗]{RESET} {message}")
        failed += 1
    elif status == "warn":
        print(f"  {YELLOW}[!]{RESET} {message}")
        warning += 1

def selection(title):
    print(f"\n{CYAN}{BOLD}[ {title} ]{RESET}")
    print("─" * 45)

def run(command):
    """Run a shell command and return its stdout as a string"""
    try:
        result = subprocess.run(
            command, shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout.strip()
    except Exception:
        return ""
    
def file_contains(filepath, text):
    """Chech if a file contains a specific string."""
    try:
        with open(filepath, "r") as f:
            return text in f.read()
    except FileNotFoundError:
        return None
    
def banner ():
    print(f"""
{GREEN}╔══════════════════════════════════════════╗
║      HardWatch — Hardening Checker       ║
║      Blue Team Security Tool             ║
╚══════════════════════════════════════════╝{RESET}
""")