"""Generate Markov text from text files."""

from sys import argv
from random import choice
import string

# import pdb; pdb.set_trace()


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(file_path) as f:
        text = f.read()

    return text

# text_string = open_and_read_file('green-eggs.txt')
# print make_chains(text_string)


def make_chains(text_string, n):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    words = text_string.split()
    words.append(None)

    for i in range(len(words) - n):
        markov_key = tuple(words[i:i+n])

        # Check to see if dictionary has key. If not, adds key.
        if chains.get(markov_key):
            chains[markov_key].append(words[i+n])
        else:
            chains[markov_key] = [words[i+n]]

    return chains


def make_text(chains, n):
    """Return text from chains."""

    # Created a list with all keys that start a sentence (captial letter)
    sen_start_upper = []
    for chain in chains.keys():
        if chain[0][0] in string.ascii_uppercase:
            sen_start_upper.append(chain)

    # Select first key from sentence starter list
    first_ngram = choice(sen_start_upper)

    words = list(first_ngram)

    while True:

        next_word = choice(chains[first_ngram])

        if next_word is None:
            break

        words.append(next_word)

        if next_word[-1] in '.!?':
            break

        first_ngram_list = list(first_ngram)

        # Slices previous ngram from second item to the end for next iteration
        ngram_list = first_ngram_list[1:]
        ngram_list.append(next_word)

        # Converts the modified ngram to a tuple for the next iteration
        first_ngram = tuple(ngram_list)

    word_string = " ".join(words)

    return word_string[:140]

if __name__ == '__main__':
    input_path = argv[1]

    # Open the file and turn it into one long string
    input_text = open_and_read_file(input_path)

    # Get a Markov chain
    chains = make_chains(input_text, int(argv[2]))

    # Produce random text
    random_text = make_text(chains, int(argv[2]))

    print random_text
