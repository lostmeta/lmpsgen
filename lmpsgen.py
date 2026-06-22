from core.parser import parse_input
from core.generate import generate_wordlist
import argparse
def person_main(args):
    verb = 0
    if args.verbose:
        verb = 1
    base_words = []
    base_words += parse_input(args.year)
    base_words += parse_input(args.name)
    base_words += parse_input(args.lastname)
    base_words += parse_input(args.pet)
    base_words += parse_input(args.additional_words)
    wordlist_name = args.output
    str_wordl = 0
    wordlist = generate_wordlist(base_words,args.combo,args.leatspeak,args.spec_char)
    with open(wordlist_name,"w") as f:
        f.write("")
    for wordl in wordlist:
        str_wordl += 1
        with open(wordlist_name, "a") as f:
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
    parser.add_argument('-n','--name',dest='name',help="Target's First name")
    parser.add_argument('-l','--lastname',dest='lastname',help="Target's Last name")
    parser.add_argument('-y','--year',dest='year',help="Target's birth year or important dates")
    parser.add_argument('-o','--output',dest='output',help="Path to the output file (default: wordlist.txt")
    parser.add_argument('-p','--pet',dest='pet',help="Target's pet name")
    parser.add_argument('-a','--additional',dest='additional_words',help="Additional custom keywords, separated by comma")
    parser.add_argument('-v','--verbose',dest='verbose',action='store_true',help="Enable verbose output (detailed logging)")
    parser.add_argument('-c',dest='combo', default=2,type=int,help="Combination depth (e.g., -c 2 chains two words together)")
    parser.add_argument('-ls','--leatspeak',dest='leatspeak',action='store_true',help='Enable Leetspeak mutations (e.g., a->4, e->3)')
    parser.add_argument('-sc', '--specialchar', dest='spec_char', nargs='?', const='default',
                    help="Add special characters. Use without values for default (!@#$?) or specify custom (e.g., -sc '!_')")

    args = parser.parse_args()
    person_main(args)
