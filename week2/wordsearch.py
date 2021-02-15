import argparse
import sys
import json


def reverse(line):
    return line[::-1]


def solve(file, words, advanced=False):
    wordfile = str(words)
    search_list = []

    puzzle = open(file, 'r')
    rows = []
    for line in puzzle.readlines():
        rows.append(line.rstrip())
    for line in rows:
        search_list.append(line)

    for i in range(len(rows[0])):
        search_list.append(''.join([row[i] for row in rows]))

    if advanced is True:
        temp_list = []
        for line in search_list:
            rev_line = reverse(line)
            temp_list.append(rev_line)
        for templine in temp_list:
            search_list.append(templine)

    with open(wordfile) as f:
        data = json.load(f)
        matches = []
        for words in data.values():
            for word in words:
                word_str = str(word.upper())
                for entry in search_list:
                    if entry.find(word_str) != -1:
                        matches.append(word_str)

    return matches
    puzzle.close()


def main(argv):
    parser = argparse.ArgumentParser(description='Give files to process')
    parser.add_argument('txtfile',
                        help='Provide a txt file with a word search.')
    parser.add_argument('--wordlist', required=False, default='words.json',
                        help='Provide JSON wordlist (default: words.json)')
    parser.add_argument('--advanced', action='store_true',
                        help='If specified, also searches in reverse.')
    args = parser.parse_args()

    print(solve(args.txtfile, args.wordlist, args.advanced))


if __name__ == "__main__":
    main(sys.argv)
