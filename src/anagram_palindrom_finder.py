import argparse
from urllib.request import urlopen
from collections import defaultdict

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--url",
        type=str,
        help="url to load text"
    )
    return parser.parse_args()

def main():
    args = parse_args()
    file = urlopen(args.url)
    anag_dict = defaultdict(set)
    palindromes = set()
    for line in file:
        words_list = line.decode("utf-8").split()
        for word in words_list:
            anag_dict[''.join(sorted(word))].add(word)
            if word == word[::-1]:
                palindromes.add(word)
    anagrams = []
    for _, value in anag_dict.items():
        if len(value) >= 2:
            anagrams.append(value)
    print("Anagrams:")
    print(anagrams)
    print()
    print("Palindromes:")
    print(palindromes)


if __name__ == "__main__":
    main()
