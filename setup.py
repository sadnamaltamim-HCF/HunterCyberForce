#!/usr/bin/env python3
# ================================================================
#   HUNTER CYBER FORCE — Setup Tool
#   Author  : HCF Team
#   Version : 2.0
#   GitHub  : github.com/sadnamaltamim-HCF/HunterCyberForce
# ================================================================

import os
import sys
import time
import subprocess

# ── Colors ───────────────────────────────────────────────────────
R  = "\033[0;31m"
G  = "\033[0;32m"
Y  = "\033[1;33m"
C  = "\033[0;36m"
W  = "\033[1;37m"
B  = "\033[0;34m"
RS = "\033[0m"

# ── Banner ───────────────────────────────────────────────────────
def banner():
    os.system("clear")
    print(R + """
  ██╗  ██╗ ██████╗███████╗
  ██║  ██║██╔════╝██╔════╝
  ███████║██║     █████╗  
  ██╔══██║██║     ██╔══╝  
  ██║  ██║╚██████╗██║     
  ╚═╝  ╚═╝ ╚═════╝╚═╝    """ + RS)
    print(C + "  ══ HUNTER CYBER FORCE ══" + RS)
    print(Y + "  [*] Setup Tool v2.0" + RS)
    print(Y + "  [*] github.com/sadnamaltamim-HCF/HunterCyberForce" + RS)
    print()

# ── Run command ──────────────────────────────────────────────────
def run(cmd):
    result = subprocess.run(cmd, shell=True,
                            stdout=subprocess.DEVNULL,
                            stderr=subprocess.DEVNULL)
    return result.returncode == 0

# ── Install with status ──────────────────────────────────────────
def install(name, cmd):
    print(Y + f"  [*] Installing {name}..." + RS, end="", flush=True)
    if run(cmd):
        print("\r" + G + f"  [✓] {name} installed!       " + RS)
    else:
        print("\r" + R + f"  [✗] {name} failed — retry manually" + RS)
    time.sleep(0.3)

# ── Progress bar ─────────────────────────────────────────────────
def progress(label, total=30):
    print(C + f"\n  [~] {label}" + RS)
    bar = ""
    for i in range(total):
        bar += "█"
        print(f"\r  [{bar:<{total}}] {int((i+1)/total*100)}%", end="", flush=True)
        time.sleep(0.05)
    print()

# ── Steps ────────────────────────────────────────────────────────
def step_update():
    print(W + "\n  ━━━ [1/6] System Update ━━━" + RS)
    install("pkg update", "pkg update -y")
    install("pkg upgrade", "pkg upgrade -y")

def step_basic():
    print(W + "\n  ━━━ [2/6] Basic Packages ━━━" + RS)
    pkgs = [
        ("Python3",     "pkg install python -y"),
        ("Python2",     "pkg install python2 -y"),
        ("Git",         "pkg install git -y"),
        ("Curl",        "pkg install curl -y"),
        ("Wget",        "pkg install wget -y"),
        ("Nano",        "pkg install nano -y"),
        ("Vim",         "pkg install vim -y"),
        ("Zip/Unzip",   "pkg install zip unzip -y"),
        ("Tar",         "pkg install tar -y"),
        ("Htop",        "pkg install htop -y"),
        ("Tree",        "pkg install tree -y"),
        ("OpenSSH",     "pkg install openssh -y"),
        ("Nodejs",      "pkg install nodejs -y"),
        ("Ruby",        "pkg install ruby -y"),
        ("PHP",         "pkg install php -y"),
        ("Perl",        "pkg install perl -y"),
        ("FFmpeg",      "pkg install ffmpeg -y"),
        ("Termux-API",  "pkg install termux-api -y"),
    ]
    for name, cmd in pkgs:
        install(name, cmd)

def step_pip():
    print(W + "\n  ━━━ [3/6] Python Libraries ━━━" + RS)
    libs = [
        ("Requests",    "pip install requests"),
        ("Colorama",    "pip install colorama"),
        ("Pyfiglet",    "pip install pyfiglet"),
        ("Rich",        "pip install rich"),
        ("Paramiko",    "pip install paramiko"),
        ("Scapy",       "pip install scapy"),
        ("BeautifulSoup","pip install beautifulsoup4"),
        ("Urllib3",     "pip install urllib3"),
        ("Tabulate",    "pip install tabulate"),
        ("Tqdm",        "pip install tqdm"),
    ]
    for name, cmd in libs:
        install(name, cmd)

def step_security():
    print(W + "\n  ━━━ [4/6] Security Tools ━━━" + RS)
    tools = [
        ("Nmap",        "pkg install nmap -y"),
        ("Hydra",       "pkg install hydra -y"),
        ("SQLMap",      "pip install sqlmap"),
        ("Nikto",       "git clone https://github.com/sullo/nikto ~/tools/nikto"),
        ("WhatWeb",     "gem install whatweb"),
    ]
    for name, cmd in tools:
        install(name, cmd)

def step_zsh():
    print(W + "\n  ━━━ [5/6] Zsh + Oh-My-Zsh ━━━" + RS)
    install("Zsh", "pkg install zsh -y")
    install("Oh-My-Zsh", 'export RUNZSH=no; export CHSH=no; sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended')
    install("zsh-autosuggestions", "git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions")
    install("zsh-syntax-highlighting", "git clone https://github.com/zsh-users/zsh-syntax-highlighting ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting")
    run("sed -i 's/plugins=(git)/plugins=(git zsh-autosuggestions zsh-syntax-highlighting)/' ~/.zshrc")

def step_finalize():
    print(W + "\n  ━━━ [6/6] Finalizing ━━━" + RS)
    # Storage permission
    install("Storage Permission", "termux-setup-storage")
    # SSH Key
    if not os.path.exists(os.path.expanduser("~/.ssh/id_rsa")):
        install("SSH Key", 'ssh-keygen -t rsa -b 4096 -C "hcf-member" -f ~/.ssh/id_rsa -N ""')
    # Set zsh default
    install("Default Shell → Zsh", "chsh -s zsh")
    # Banner/MOTD
    motd_path = os.path.expanduser("~/.termux/motd")
    os.makedirs(os.path.dirname(motd_path), exist_ok=True)
    with open(motd_path, "w") as f:
        f.write("""
  ██╗  ██╗ ██████╗███████╗
  ██║  ██║██╔════╝██╔════╝
  ███████║██║     █████╗  
  ██╔══██║██║     ██╔══╝  
  ██║  ██║╚██████╗██║     
  ╚═╝  ╚═╝ ╚═════╝╚═╝    
  HUNTER CYBER FORCE
  ─────────────────────────
  🔴 Stay Sharp. Stay Silent.
""")
    print(G + "  [✓] MOTD Banner set!" + RS)

# ── Main ─────────────────────────────────────────────────────────
def main():
    banner()
    print(R + "  ⚠️  For educational & authorized use only!" + RS)
    print()

    confirm = input(Y + "  Continue with HCF Setup? [y/N]: " + RS).strip().lower()
    if confirm != "y":
        print(R + "\n  Aborted." + RS)
        sys.exit(0)

    progress("Preparing HCF Environment...")

    step_update()
    step_basic()
    step_pip()
    step_security()
    step_zsh()
    step_finalize()

    print()
    print(G + "  ╔══════════════════════════════════════╗" + RS)
    print(G + "  ║   HCF SETUP COMPLETE! Restart Termux ║" + RS)
    print(G + "  ║   Now run: python3 run.py             ║" + RS)
    print(G + "  ╚══════════════════════════════════════╝" + RS)
    print()

if __name__ == "__main__":
    main()
