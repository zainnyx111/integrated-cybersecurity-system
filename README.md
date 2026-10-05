# Integrated Cybersecurity System

A Python command-line toolkit that combines three basic security checks in one menu-driven app.

## Modules
1. **Phishing Detection**: scores an email or URL against common phishing phrases and classifies it as safe, suspicious, or phishing.
2. **Vulnerability Scanning**: runs a fast Nmap scan (`nmap -F`) on a target IP address and shows the open ports.
3. **Intrusion Detection**: flags a possible brute-force attack when the number of failed login attempts exceeds a threshold.

## Requirements
- Python 3.8 or higher
- [Nmap](https://nmap.org/download.html) installed and added to your PATH

## How to run
1. Clone the repository:
       git clone https://github.com/zainnyx111/integrated-cybersecurity-system.git
2. Go into the folder:
       cd integrated-cybersecurity-system
3. Run the program:
       python script.py
4. Choose an option from the menu (1-4).

## Limitations
- Phishing detection is keyword-based, so it can miss or misflag some messages.
- Intrusion detection uses a manually entered count and does not read real logs yet.

## Future improvements
- Read real authentication logs
- Use machine learning for phishing detection
- Add automatic blocking of threats (IPS)

## Disclaimer
This project is for educational purposes only. Only scan systems you own or have written permission to test.
