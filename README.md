# lmpsgen - Lostmeta. Password wordlist generator

### Quick start
```bash
python3 lmpsgen.py
```

### Options
```text
options:
  -h, --help     show this help message and exit
  -v, --verbose  Enable verbose output (detailed logging)
  -c COMBO       Combination depth (e.g., -c 2 chains two words together)
```
**1. Standard Interactive Mode (Quiet)**
Generates a list of words by concatenating two words or numbers (SmithJohn, EmmaJohn).
```bash
python3 lmpsgen.py -c 2
```

**2. Live Verbose Mode**
See words being added to the list in real-time.
```bash
python3 lmpsgen.py -c 2 -v
```

**3. Custom Combination Depth**
The Custom Combination Depth function generates a list of words by combining three words or numbers (SmithJohn2002, 2002EmmaJohn).
```bash
python3 lmpsgen.py -c 3 -v
```
<img width="565" height="417" alt="изображение" src="https://github.com/user-attachments/assets/2d1af5f1-9563-487d-b677-923a1abcff83" />
