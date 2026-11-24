#!/usr/bin/env python3
# ================================================================
#   HUNTER CYBER FORCE — Custom Banner Maker
#   Author  : HCF Team
#   Version : 1.0
#   GitHub  : github.com/sadnamaltamim-HCF/HunterCyberForce
# ================================================================

import os
import sys
import time
import subprocess

# ── Auto install pyfiglet & colorama ─────────────────────────────
def install_deps():
    for pkg in ["pyfiglet", "colorama"]:
        try:
            __import__(pkg)
        except ImportError:
            print(f"  [*] Installing {pkg}...")
            subprocess.run([sys.executable, "-m", "pip", "install", pkg],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

install_deps()

import pyfiglet
from colorama import Fore, Style, init
init(autoreset=True)

# ── Colors ───────────────────────────────────────────────────────
COLORS = {
    "1": ("\033[0;31m",  "Red",     Fore.RED),
    "2": ("\033[0;32m",  "Green",   Fore.GREEN),
    "3": ("\033[0;36m",  "Cyan",    Fore.CYAN),
    "4": ("\033[1;33m",  "Yellow",  Fore.YELLOW),
    "5": ("\033[0;35m",  "Magenta", Fore.MAGENTA),
    "6": ("\033[0;34m",  "Blue",    Fore.BLUE),
    "7": ("\033[1;37m",  "White",   Fore.WHITE),
}

RAINBOW = [
    "\033[0;31m", "\033[0;33m", "\033[0;32m",
    "\033[0;36m", "\033[0;34m", "\033[0;35m"
]

# ── Fonts ────────────────────────────────────────────────────────
FONTS = {
    "1": ("block",       "Block"),
    "2": ("slant",       "Slant"),
    "3": ("3-d",         "3D"),
    "4": ("shadow",      "Shadow"),
    "5": ("banner3-D",   "Banner 3D"),
    "6": ("doom",        "Doom"),
    "7": ("isometric1",  "Isometric"),
    "8": ("letters",     "Letters"),
    "9": ("star_wars",   "Star Wars"),
    "10": ("big",        "Big"),
}

RS = "\033[0m"
R  = "\033[0;31m"
G  = "\033[0;32m"
Y  = "\033[1;33m"
C  = "\033[0;36m"
W  = "\033[1;37m"

# ── Utilities ────────────────────────────────────────────────────
def clear():
    os.system("clear")

def pause():
    input(Y + "\n  [↵] Press Enter to continue..." + RS)

def hcf_banner():
    clear()
    print(R + """
  ██╗  ██╗ ██████╗███████╗
  ██║  ██║██╔════╝██╔════╝
  ███████║██║     █████╗  
  ██╔══██║██║     ██╔══╝  
  ██║  ██║╚██████╗██║     
  ╚═╝  ╚═╝ ╚═════╝╚═╝    """ + RS)
    print(C + "  ══ HUNTER CYBER FORCE — Banner Maker ══" + RS)
    print()

# ── Rainbow text ─────────────────────────────────────────────────
def rainbow_text(text):
    result = ""
    i = 0
    for ch in text:
        if ch != " ":
            result += RAINBOW[i % len(RAINBOW)] + ch
            i += 1
        else:
            result += ch
    return result + RS

def rainbow_banner(text):
    result = ""
    lines = text.split("\n")
    for i, line in enumerate(lines):
        result += RAINBOW[i % len(RAINBOW)] + line + "\n"
    return result + RS

# ── Preview banner ───────────────────────────────────────────────
def preview_banner(name, font_key, color_key, subtitle, tagline):
    clear()
    font  = FONTS.get(font_key, ("big", "Big"))[0]
    color = COLORS.get(color_key, ("\033[0;36m", "Cyan", Fore.CYAN))

    try:
        ascii_art = pyfiglet.figlet_format(name, font=font)
    except:
        ascii_art = pyfiglet.figlet_format(name, font="big")

    print()
    if color_key == "8":  # Rainbow
        print(rainbow_banner(ascii_art))
    else:
        print(color[0] + ascii_art + RS)

    if subtitle:
        if color_key == "8":
            print("  " + rainbow_text(subtitle))
        else:
            print(color[0] + f"  {subtitle}" + RS)

    if tagline:
        print(W + f"  {tagline}" + RS)

    print()

# ── Save to .zshrc / .bashrc ─────────────────────────────────────
def save_banner(name, font_key, color_key, subtitle, tagline):
    font  = FONTS.get(font_key, ("big", "Big"))[0]
    color = COLORS.get(color_key, ("\033[0;36m", "Cyan", Fore.CYAN))

    try:
        ascii_art = pyfiglet.figlet_format(name, font=font)
    except:
        ascii_art = pyfiglet.figlet_format(name, font="big")

    # Build banner lines
    lines = []
    lines.append('echo ""')

    if color_key == "8":
        rainbow_lines = ascii_art.split("\n")
        for i, line in enumerate(rainbow_lines):
            c = RAINBOW[i % len(RAINBOW)]
            escaped = line.replace("'", "'\\''")
            lines.append(f"echo '{c}{escaped}\\033[0m'")
    else:
        c = color[0]
        for line in ascii_art.split("\n"):
            escaped = line.replace("'", "'\\''")
            lines.append(f"echo '{c}{escaped}\\033[0m'")

    if subtitle:
        if color_key == "8":
            lines.append(f"echo '  {subtitle}'")
        else:
            lines.append(f"echo '{color[0]}  {subtitle}\\033[0m'")

    if tagline:
        lines.append(f"echo '\\033[1;37m  {tagline}\\033[0m'")

    lines.append('echo ""')

    banner_block = "\n".join(lines)

    # Remove old HCF banner block if exists
    for rc_file in ["~/.zshrc", "~/.bashrc"]:
        rc_path = os.path.expanduser(rc_file)
        if os.path.exists(rc_path):
            with open(rc_path, "r") as f:
                content = f.read()

            # Remove old banner
            if "# HCF-BANNER-START" in content:
                start = content.find("# HCF-BANNER-START")
                end   = content.find("# HCF-BANNER-END")
                if end != -1:
                    content = content[:start] + content[end+16:]

            # Add new banner
            content += f"\n# HCF-BANNER-START\n{banner_block}\n# HCF-BANNER-END\n"

            with open(rc_path, "w") as f:
                f.write(content)

            print(G + f"  [✓] Banner saved to {rc_file}" + RS)
            return

    # If no rc file exists, create .bashrc
    rc_path = os.path.expanduser("~/.bashrc")
    with open(rc_path, "w") as f:
        f.write(f"# HCF-BANNER-START\n{banner_block}\n# HCF-BANNER-END\n")
    print(G + f"  [✓] Banner saved to ~/.bashrc" + RS)

# ── Push to GitHub ───────────────────────────────────────────────
def push_to_github():
    print(Y + "\n  [*] Pushing to GitHub..." + RS)
    repo_path = os.path.expanduser("~/HunterCyberForce")
    if not os.path.exists(repo_path):
        print(R + "  [!] HunterCyberForce folder not found!" + RS)
        return

    # Copy banner_maker.py to repo
    os.system(f"cp {os.path.abspath(__file__)} {repo_path}/banner_maker.py")

    os.system(f"""
        cd {repo_path} &&
        git add . &&
        git commit -m "Update: banner_maker.py" &&
        git push origin main
    """)
    print(G + "  [✓] Pushed to GitHub!" + RS)

# ── Main ─────────────────────────────────────────────────────────
def main():
    hcf_banner()

    # ── Step 1: Name ─────────────────────────────────────────────
    print(Y + "  ━━━ Step 1: Your Name ━━━" + RS)
    name = input(C + "  Enter your name: " + RS).strip()
    if not name:
        name = "HCF"

    # ── Step 2: Font ─────────────────────────────────────────────
    print()
    print(Y + "  ━━━ Step 2: Choose Font ━━━" + RS)
    for k, (_, label) in FONTS.items():
        print(W + f"  [{k:>2}] " + C + label + RS)
    print()
    font_key = input(C + "  Font choice [1-10]: " + RS).strip()
    if font_key not in FONTS:
        font_key = "1"

    # ── Step 3: Color ────────────────────────────────────────────
    print()
    print(Y + "  ━━━ Step 3: Choose Color ━━━" + RS)
    for k, (_, label, _) in COLORS.items():
        print(W + f"  [{k}] " + C + label + RS)
    print(W + "  [8] " + C + "Rainbow 🌈" + RS)
    print()
    color_key = input(C + "  Color choice [1-8]: " + RS).strip()
    if color_key not in COLORS and color_key != "8":
        color_key = "3"

    # ── Step 4: Subtitle ─────────────────────────────────────────
    print()
    print(Y + "  ━━━ Step 4: Subtitle (optional) ━━━" + RS)
    print(W + "  Example: Hunter Cyber Force Member" + RS)
    subtitle = input(C + "  Subtitle (Enter to skip): " + RS).strip()

    # ── Step 5: Tagline ──────────────────────────────────────────
    print()
    print(Y + "  ━━━ Step 5: Tagline (optional) ━━━" + RS)
    print(W + "  Example: Stay Sharp. Stay Silent. 🔴" + RS)
    tagline = input(C + "  Tagline (Enter to skip): " + RS).strip()

    # ── Preview ──────────────────────────────────────────────────
    print()
    print(Y + "  [*] Preview:" + RS)
    time.sleep(0.5)
    preview_banner(name, font_key, color_key, subtitle, tagline)

    # ── Confirm ──────────────────────────────────────────────────
    confirm = input(Y + "  Set this as your Termux banner? [y/N]: " + RS).strip().lower()
    if confirm == "y":
        save_banner(name, font_key, color_key, subtitle, tagline)
        print()
        print(G + "  ╔══════════════════════════════════════╗" + RS)
        print(G + "  ║   Banner Set! Restart Termux to see  ║" + RS)
        print(G + "  ╚══════════════════════════════════════╝" + RS)
        print()

        # Push to GitHub option
        push = input(Y + "  Push to GitHub? [y/N]: " + RS).strip().lower()
        if push == "y":
            push_to_github()
    else:
        print(R + "\n  Cancelled." + RS)

    pause()

if __name__ == "__main__":
    main()
