#!/data/data/com.termux/files/usr/bin/bash
# Subfinder installer for Termux ARM64

pkg install -y golang -y 2>/dev/null
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest 2>/dev/null
cp ~/go/bin/subfinder $PREFIX/bin/ 2>/dev/null
echo "Subfinder installed"
