#!/data/data/com.termux/files/usr/bin/bash

# ============================================================
#   HUNTER CYBER FORCE — Termux Setup Script
#   Version: 1.0
#   Author: HCF Team
# ============================================================

RED='\033[0;31m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
BOLD='\033[1m'
RESET='\033[0m'

LOG_FILE="$HOME/hcf-setup.log"

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

print_banner() {
  clear
  echo -e "${RED}"
  cat << 'EOF'
  ██╗  ██╗ ██████╗███████╗
  ██║  ██║██╔════╝██╔════╝
  ███████║██║     █████╗  
  ██╔══██║██║     ██╔══╝  
  ██║  ██║╚██████╗██║     
  ╚═╝  ╚═╝ ╚═════╝╚═╝     
EOF
  echo -e "${CYAN}"
  cat << 'EOF'
  HUNTER CYBER FORCE
  [ Termux Advanced Setup ]
EOF
  echo -e "${RESET}"
  echo -e "${YELLOW}  ⚡ Setting up your cyber environment...${RESET}"
  echo -e "${YELLOW}  📋 Log: ~/hcf-setup.log${RESET}"
  echo ""
}

check_error() {
  if [ $? -ne 0 ]; then
    echo -e "${RED}[✗] Error: $1 failed!${RESET}"
    log "ERROR: $1 failed"
    exit 1
  else
    echo -e "${GREEN}[✓] $1 done!${RESET}"
    log "SUCCESS: $1"
  fi
}

step() {
  echo -e "\n${CYAN}${BOLD}[*] $1...${RESET}"
  log "STEP: $1"
}

# ── 1. STORAGE PERMISSION ────────────────────────────────────
setup_storage() {
  step "Setting up storage permission"
  termux-setup-storage
  sleep 2
  check_error "Storage setup"
}

# ── 2. UPDATE & UPGRADE ──────────────────────────────────────
update_system() {
  step "Updating & Upgrading packages"
  pkg update -y && pkg upgrade -y
  check_error "System update"
}

# ── 3. BASIC PACKAGES ────────────────────────────────────────
install_basic() {
  step "Installing basic packages"
  BASIC_PKGS=(
    git curl wget python python-pip
    nodejs ruby php perl
    openssh openssl nano vim
    tar zip unzip p7zip
    ffmpeg imagemagick
    termux-api htop tree
    jq dnsutils iproute2
    tsu bash zsh
  )
  for pkg in "${BASIC_PKGS[@]}"; do
    echo -e "  ${YELLOW}→ Installing $pkg${RESET}"
    pkg install -y "$pkg" >> "$LOG_FILE" 2>&1
  done
  check_error "Basic packages"
}

# ── 4. SECURITY TOOLS ────────────────────────────────────────
install_security() {
  step "Installing security tools"

  # Nmap
  pkg install -y nmap >> "$LOG_FILE" 2>&1
  echo -e "  ${GREEN}✓ Nmap${RESET}"

  # Metasploit
  echo -e "  ${YELLOW}→ Installing Metasploit (this may take a while)...${RESET}"
  curl -sL https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh | bash >> "$LOG_FILE" 2>&1
  echo -e "  ${GREEN}✓ Metasploit${RESET}"

  # Hydra
  pkg install -y hydra >> "$LOG_FILE" 2>&1
  echo -e "  ${GREEN}✓ Hydra${RESET}"

  # SQLMap
  pip install sqlmap >> "$LOG_FILE" 2>&1
  echo -e "  ${GREEN}✓ SQLMap${RESET}"

  # WhatWeb
  gem install whatweb >> "$LOG_FILE" 2>&1
  echo -e "  ${GREEN}✓ WhatWeb${RESET}"

  # Subfinder
  bash tools/install_subfinder.sh >> "$LOG_FILE" 2>&1
  echo -e "  ${GREEN}✓ Subfinder${RESET}"

  # Nuclei
  bash tools/install_nuclei.sh >> "$LOG_FILE" 2>&1
  echo -e "  ${GREEN}✓ Nuclei${RESET}"

  # Nikto
  git clone https://github.com/sullo/nikto ~/tools/nikto >> "$LOG_FILE" 2>&1
  echo -e "  ${GREEN}✓ Nikto${RESET}"

  check_error "Security tools"
}

# ── 5. ZSH + OH-MY-ZSH ──────────────────────────────────────
install_zsh() {
  step "Installing Zsh & Oh-My-Zsh"
  pkg install -y zsh >> "$LOG_FILE" 2>&1

  # Oh-My-Zsh
  export RUNZSH=no
  export CHSH=no
  sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended >> "$LOG_FILE" 2>&1

  # Plugins
  git clone https://github.com/zsh-users/zsh-autosuggestions \
    ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions >> "$LOG_FILE" 2>&1
  git clone https://github.com/zsh-users/zsh-syntax-highlighting \
    ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting >> "$LOG_FILE" 2>&1

  # Apply plugins to .zshrc
  sed -i 's/plugins=(git)/plugins=(git zsh-autosuggestions zsh-syntax-highlighting)/' ~/.zshrc

  check_error "Zsh setup"
}

# ── 6. SSH KEY ───────────────────────────────────────────────
setup_ssh() {
  step "Generating SSH Key"
  if [ ! -f ~/.ssh/id_rsa ]; then
    ssh-keygen -t rsa -b 4096 -C "hcf-termux" -f ~/.ssh/id_rsa -N "" >> "$LOG_FILE" 2>&1
    echo -e "${YELLOW}  Your SSH Public Key:${RESET}"
    cat ~/.ssh/id_rsa.pub
  else
    echo -e "  ${YELLOW}SSH key already exists, skipping.${RESET}"
  fi
  check_error "SSH key"
}

# ── 7. NGROK ────────────────────────────────────────────────
install_ngrok() {
  step "Installing Ngrok"
  wget -q https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-arm64.tgz -O /tmp/ngrok.tgz
  tar xf /tmp/ngrok.tgz -C $PREFIX/bin/
  chmod +x $PREFIX/bin/ngrok
  check_error "Ngrok"
}

# ── 8. CLOUDFLARE TUNNEL ─────────────────────────────────────
install_cloudflared() {
  step "Installing Cloudflared (Cloudflare Tunnel)"
  wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64 \
    -O $PREFIX/bin/cloudflared >> "$LOG_FILE" 2>&1
  chmod +x $PREFIX/bin/cloudflared
  check_error "Cloudflared"
}

# ── 9. CUSTOM ALIASES ────────────────────────────────────────
setup_aliases() {
  step "Setting up HCF custom aliases"
  cat >> ~/.zshrc << 'ALIASES'

# ── HCF Custom Aliases ──────────────────
alias update='pkg update && pkg upgrade -y'
alias myip='curl -s ifconfig.me && echo'
alias ports='nmap -sT localhost'
alias scan='nmap -sV -sC'
alias sqlm='python $(which sqlmap)'
alias msf='msfconsole'
alias hyd='hydra'
alias web='whatweb'
alias cfstart='cloudflared tunnel'
alias gitup='git add . && git commit -m "update" && git push'
alias ..='cd ..'
alias ...='cd ../..'
alias ll='ls -la'
alias c='clear'
alias h='history'
alias tools='ls ~/tools/'
ALIASES

  check_error "Aliases"
}

# ── 10. HCF MOTD BANNER ──────────────────────────────────────
setup_banner() {
  step "Setting up HCF login banner"
  cat > ~/.termux/motd << 'MOTD'

  ██╗  ██╗ ██████╗███████╗
  ██║  ██║██╔════╝██╔════╝
  ███████║██║     █████╗  
  ██╔══██║██║     ██╔══╝  
  ██║  ██║╚██████╗██║     
  ╚═╝  ╚═╝ ╚═════╝╚═╝     
  HUNTER CYBER FORCE
  ──────────────────────────
  🔴 Stay Sharp. Stay Silent.
MOTD

  check_error "Banner"
}

# ── 11. CHANGE DEFAULT SHELL ─────────────────────────────────
set_zsh_default() {
  step "Setting Zsh as default shell"
  chsh -s zsh >> "$LOG_FILE" 2>&1
  check_error "Default shell"
}

# ── MAIN ─────────────────────────────────────────────────────
print_banner

echo -e "${YELLOW}This will install all HCF tools and configs.${RESET}"
echo -e "${RED}For educational/CTF/authorized pentesting use only!${RESET}"
echo ""
read -p "Continue? [y/N]: " confirm
if [[ "$confirm" != "y" && "$confirm" != "Y" ]]; then
  echo "Aborted."
  exit 0
fi

setup_storage
update_system
install_basic
install_security
install_zsh
setup_ssh
install_ngrok
install_cloudflared
setup_aliases
setup_banner
set_zsh_default

echo ""
echo -e "${GREEN}${BOLD}╔═══════════════════════════════════════╗${RESET}"
echo -e "${GREEN}${BOLD}║   HCF SETUP COMPLETE! Restart Termux  ║${RESET}"
echo -e "${GREEN}${BOLD}╚═══════════════════════════════════════╝${RESET}"
echo ""
echo -e "${CYAN}  📋 Full log saved at: ~/hcf-setup.log${RESET}"
echo -e "${CYAN}  🔑 SSH Public Key:${RESET}"
cat ~/.ssh/id_rsa.pub 2>/dev/null
echo ""
log "SETUP COMPLETE"
