#!/data/data/com.termux/files/usr/bin/bash
# Nuclei installer for Termux ARM64

pkg install -y golang 2>/dev/null
go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest 2>/dev/null
cp ~/go/bin/nuclei $PREFIX/bin/ 2>/dev/null
nuclei -update-templates 2>/dev/null
echo "Nuclei installed"
