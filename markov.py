"""Generate Markov text from text files."""

# from random import choice
import random


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file = open(file_path).read()

    return file


def make_chains(text_string):
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
    all_the_words = text_string.split()
    # print(all_the_words)

    for index in range(len(all_the_words) - 2):
        key = (all_the_words[index], all_the_words[index + 1])
        value = all_the_words[index + 2]

        if key not in chains:
            lst = []
            lst.append(value)
            chains[key] = lst
        # elif key in chains:
        #     chains[key].append(value)
        chains[key].append(value)

    return chains


def make_text(chains):
    """Return text from chains."""

    output_text = []
    key_list = list(chains.keys())
    # try orig import and eliminate random. here later
    start_point = random.choice(key_list)

    
    value_list = chains[start_point]
    chosen_word = random.choice(value_list)
    our_string = ' '.join(start_point)
    our_string = f"{our_string} {chosen_word}"
    print(our_string)


    # put this somewhere
    # for i in tuple:
    #     "" = tuple[0]
    #     str += str.join()

    # while True:
    #     everything above


    # return " ".join(output_text)
    pass


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
