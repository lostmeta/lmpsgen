from core.parser import parse_input
from core.generate import generate_wordlist
import argparse
def person_main(args):
    verb = 0
    if args.verbose:
        verb = 1
    target_first_name = input("Target First name: ").strip()
    target_last_name = input("Target Last name: ").strip()
    target_birthday = input("Target birthday (DD-MM-YYYY): ").strip()
    partner_name = input("Target Partner name: ").strip()
    pet_name = input("Pet Name: ").strip()
    additional_words = input("additional words: ").strip()
    spec_char = input("Do you want to add special chars at the end of words?: ").strip()
    leet_mode = input("Leet mode?: ").strip()
    
    day,month,year = target_birthday.split("-")
    base_words = [day,month,year]
    base_words += parse_input(target_first_name)
    base_words += parse_input(target_last_name)
    base_words += parse_input(partner_name)
    base_words += parse_input(pet_name)
    base_words += parse_input(additional_words)

    str_wordl = 0
    wordlist = generate_wordlist(base_words,args.combo,leet_mode,spec_char)
    with open("wordlist.txt","w") as f:
        f.write("")
    for wordl in wordlist:
        str_wordl += 1
        with open("wordlist.txt", "a") as f:
            f.write(f"{wordl}\n")
            if verb == 1:
                if args.verbose:
                    print(f"\r[*] Adding {wordl:<60}", end="", flush=True)
    if args.verbose:
        print("\r" + " " * 70 + "\r", end="") 

    print(f"words generated: {str_wordl}")
    print(f"wordlist saved in wordlist.txt")
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generating wordlists")
    parser.add_argument('-v','--verbose',dest='verbose',action='store_true',help="Enable verbose output (detailed logging)")
    parser.add_argument('-c',dest='combo', default=2,type=int,help="Combination depth (e.g., -c 2 chains two words together)")
    args = parser.parse_args()
    person_main(args)
