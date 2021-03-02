import re
import gzip
import sys


def splitter(text):
    ''' Splits the text into individual sentences on each line. '''
    pat = re.compile(r'([\"\'\-]?[A-Z0-9][^\.!?]*[\.!?][\"\']?)')
    split = pat.findall(text)
    return tokenizer(split)


def tokenizer(splittext):
    ''' Tokenizes the text based on words and punctuations. '''
    cleantext = []
    tokens = re.compile(r"[\w]*-[\w]*|[\w]+'n|[\w]+'s|[\w]+|[^\s\w]")
    for line in splittext:
        tokenize = tokens.findall(line)
        tokenline = ' '.join(tokenize)
        cleantext.append(tokenline)
    return cleantext


def main(argv):
    with gzip.open(sys.argv[1], 'rt', encoding='utf8') as f:
        text = f.read()
        splittext = text.splitlines()
        body = ' '.join(splittext[4:-7])
        sentstext = splitter(body)
        for line in sentstext:
            print(line)

    quit()


if __name__ == "__main__":
    main(sys.argv)
