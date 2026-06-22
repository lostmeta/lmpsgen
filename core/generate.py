import itertools
def generate_wordlist(base_words,combo_limit,leet_mode,spec_char):
    wordlist = set()
    leet = {"a": "4","A": "4","i": "1","I": "1","e": "3","E": "3","o": "0","O": "0"}
    special_char = ["!","@","#","$","?"]
    table = str.maketrans(leet)
    for r in range(1,combo_limit + 1):
        for combo in itertools.permutations(base_words,r):
            word = "".join(combo)
            variants = {word,word.lower(),word.capitalize(),word.title()}
            for variant in variants:
                wordlist.add(variant)
                if leet_mode in ["yes","y"]:
                    wordlist.add(variant.translate(table))
                for char in special_char:
                    if spec_char in ["yes","y"]:
                        wordlist.add(f"{variant}{char}")
                        if leet_mode in ["yes","y"]:
                            wordlist.add(f"{variant.translate(table)}{char}")
    for num in range(1,10000):
        for word2 in base_words:
            variants = {word2,word2.lower(),word2.capitalize(),word2.title()}
            for variant in variants:
                wordlist.add(f"{variant}{num}")
                if leet_mode in ["yes","y"]:
                    wordlist.add(f"{variant.translate(table)}{num}")
                for char in special_char:
                    if spec_char in ["yes","y"]:
                        wordlist.add(f"{variant}{num}{char}")
                        if leet_mode in ["yes","y"]:
                            wordlist.add(f"{variant.translate(table)}{num}{char}")
    return wordlist