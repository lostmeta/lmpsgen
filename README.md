# lmpsgen - Lostmeta. Password wordlist generator

## Quick Start

Clone the repository and run the tool:
```bash
git clone https://github.com/lostmeta/lmpsgen.git
cd lmpsgen
python3 lmpsgen.py -h
```

## Example of work
Generate wordlists instantly using specific command-line arguments:
```bash
python3 lmpsgen.py -n John -l Smith -y 2002 -ls -sc -o my_wordlist.txt
```

### Options
```text
    -h      Show this help menu and exit
    -n      Target's first name
    -l      Target's last name
    -y      Target's birth year or important dates
    -p      Target's pet name
    -a      Custom keywords (comma-separated, e.g. -a "RealMadrid,Lakers")
    -o      Output file name (default: wordlist.txt)
    -c      Combination depth for words chaining (default: 2)
    -ls     Enable leetspeak mutations (a->4, e->3, o->0, i->1)
    -sc     Add special characters. Empty for default (!@#$?) or custom (e.g. -sc '!_')
    -v      Enable verbose real-time logging
```
