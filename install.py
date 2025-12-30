#!/usr/bin/env python3
import os
import sys
import subprocess

# Warna ANSI
R = "\033[1;91m"
G = "\033[1;92m"
Y = "\033[1;93m"
C = "\033[1;96m"
W = "\033[1;97m"
D = "\033[0m"

def run_cmd(cmd, shell=True):
    try:
        subprocess.run(cmd, shell=shell, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        print(f"{R}[!] Failed to run: {cmd}{D}")
        sys.exit(1)

def install_for_termux():
    print(f"{Y}[*] Installing for Termux...{D}")
    
    # Update & install sistem
    print(f"{Y}[*] Updating packages...{D}")
    run_cmd("pkg update -y")
    
    print(f"{Y}[*] Installing system tools: git, whois, grep...{D}")
    run_cmd("pkg install -y git whois grep python")

    # Install Python packages
    print(f"{Y}[*] Installing Python dependencies...{D}")
    run_cmd("pip install requests beautifulsoup4 PyPDF2")

    print(f"{G}[✓] Termux installation complete!{D}")

def install_for_linux():
    print(f"{Y}[*] Installing for Linux...{D}")
    print(f"{Y}[i] This assumes you have 'sudo' and internet access.{D}")
    
    # Update (opsional, skip jika tidak mau ganggu sistem)
    print(f"{Y}[*] (Optional) Updating system packages...{D}")
    try:
        subprocess.run("sudo apt update -y", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=60)
    except:
        print(f"{Y}[i] Skipped system update (or failed).{D}")

    # Install whois & git
    print(f"{Y}[*] Installing 'whois', 'git', 'python3-pip'...{D}")
    run_cmd("sudo apt install -y whois git python3-pip")

    # Install Python packages
    print(f"{Y}[*] Installing Python dependencies...{D}")
    run_cmd("pip3 install requests beautifulsoup4 PyPDF2")

    print(f"{G}[✓] Linux installation complete!{D}")

def detect_environment():
    if os.path.exists("/data/data/com.termux"):
        return "termux"
    elif os.path.exists("/usr/bin/apt") or os.path.exists("/etc/debian_version"):
        return "linux"
    else:
        return "unknown"

def main():
    clear = "clear" if os.name != "nt" else "cls"
    os.system(clear)
    
    print(f"{C}============================================{D}")
    print(f"{G}  BLOOD TOOLKIT — INSTALLER (v2.0){D}")
    print(f"{C}============================================{D}")
    print(f"{Y}Detected environment: {detect_environment().upper()}{D}\n")

    print(f"{C}[1]{W} Install for Termux")
    print(f"{C}[2]{W} Install for Linux (Debian/Ubuntu)")
    print(f"{R}[0]{W} Exit\n")

    choice = input(f"{G}Select option (1/2/0): {W}").strip()

    if choice == "1":
        install_for_termux()
    elif choice == "2":
        install_for_linux()
    elif choice == "0":
        print(f"{Y}Installation canceled.{D}")
        sys.exit(0)
    else:
        print(f"{R}[!] Invalid choice.{D}")
        sys.exit(1)

    print(f"\n{C}To run your tool:{D}")
    if detect_environment() == "termux":
        print(f"    {W}python Blood.py{D}")
    else:
        print(f"    {W}python3 Blood.py{D}")

    print(f"\n{G}Installation finished successfully!{D}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}[!] Installation interrupted by user.{D}")
        sys.exit(0)