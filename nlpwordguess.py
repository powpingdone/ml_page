from sys import argv, exit
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
import io
import re
from random import choice

# reminder: THIS REQUIRES PYTHON3.11


def preproc(f: io.TextIOWrapper) -> (list[str], list[str]):
    # create list of tokens
    sw = set(stopwords.words("english"))
    is_regular = re.compile(r"\w*")
    tokens = []
    while inp := f.readline().strip().lower():
        dump = word_tokenize(inp, preserve_line=True)
        # first processing for the tokens
        # strip short words,
        # check if word is just regular chars,
        # and is not a stop word
        tokens += [
            x for x in dump if len(x) > 5 and is_regular.fullmatch(x) and x not in sw
        ]
    # lemmatize the tokens
    lem = WordNetLemmatizer()
    # note: this order is specific so that it will
    # process the maximum amount of parts of speech
    # because, apparently, pos_tag(set(...)) causes this
    # why? probably because of the same reason that dicts are not actually
    # sortable, so python can order them however it pleases
    # yes, this uses more RAM because this generates a new list, then puts
    # it into a set, but it's now consistent
    nouns = list(set(pos_tag([lem.lemmatize(x) for x in tokens])))
    print("Tagged POS word set: \n{}".format("\n".join([str(x) for x in nouns[:20]])))
    # finally, sort nouns out
    nouns = [x for (x, tkn) in nouns if len(tkn) > 2 and tkn[:2] == "NN"]
    print(f"Tokens: {len(tokens)}\nNouns: {len(nouns)}")
    return (tokens, nouns)


def main():
    if len(argv) != 2:
        print(f"usage: {argv[0]} <filename>")
        exit(1)

    # lexical diversity
    with open(argv[1]) as f:
        reg = re.compile(r"\w*")
        tokens = []
        while inp := f.readline().strip().lower():
            # extract words only
            tokens += [
                x for x in word_tokenize(inp, preserve_line=True) if reg.fullmatch(x)
            ]
        print(f"Lexical Diversity: {len(set(tokens))/len(tokens):.2f}")

    # actual proc
    with open(argv[1]) as f:
        tokens, nouns = preproc(f)

    # get popular words
    count = {x: 0 for x in nouns}
    for word in tokens:
        if word in count:
            count[word] += 1
    count_list = list(count.items())
    count_list.sort(key=lambda x: x[1], reverse=True)
    words = [x[0] for x in count_list][:50]

    # word guesser game
    score = 5
    while True:
        wrd = choice(words)
        discover = [False]*(len(wrd))
        print("Let's play a word guessing game!")
        while False in discover and score >= 0:
            # output current guess
            for (letter, readout) in zip(wrd, discover):
                print(f"{letter if readout else '_'} ", end="")
            print()

            # check letter guess
            letter = input("Guess a letter:")
            if letter in wrd:
                if discover[wrd.find(letter)]:
                    print("Letter already discovered, try another")
                    continue
                x = wrd.find(letter)
                while x != -1:
                    discover[x] = True
                    x = wrd.find(letter, x + 1)
                score += 1
                print(f"Right! Score is {score}")
            elif letter == "!":
                exit()
            else:
                score -= 1
                # yes, replicating the output with an extra space
                # is completely needed, because that's what happened in
                # the sample output
                print(f"Sorry, guess again. Score is  {score}")
                if score < 0:
                    exit()
        if score >= 0:
            print(f"{' '.join(wrd)}\nYou solved it!\n\nCurrent score: {score}\n\nGuess another word")


if __name__ == "__main__":
    main()
