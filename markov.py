"""Generate Markov text from text files."""

import random
from sys import argv


# Temp took out file_path arg to take user input
def open_and_read_file():
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    try:
        file = open(argv[1]).read()
    except IndexError:
        file = input("Please enter a text file: ")
        file = open(file).read()

    # Version 1: doesn't prompt for user input
    # file = open(file_path).read()

    return file


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains."""

    chains = {}
    all_the_words = text_string.split()

    for index in range(len(all_the_words) - 2):
        key = (all_the_words[index], all_the_words[index + 1])
        value = all_the_words[index + 2]

        if key not in chains:
            lst = []
            lst.append(value)
            chains[key] = lst

        chains[key].append(value)

    return chains


def make_text(chains):
    """Return text from chains."""

    # Initializes our output as list
    output_text = []

    # Makes a list of all the keys in the dictionary
    key_list = list(chains.keys())
    # Our randomized start point for the chain
    start_point = random.choice(key_list)
    # Pulls the values associated with our start point from the dictionary
    value_list = chains[start_point]
    # Chooses a random word from the value list associated with the start point key
    chosen_word = random.choice(value_list)
    # Adding first value at index zero in our starting point tuple to our output
    output_text.append(start_point[0])
    # Adding second value in our starting point tuple to the output
    output_text.append(start_point[1])

    # Creates a new state with the second word from previous state and the
    # Randomly chosen word, This is the code moving through the Markov chain
    new_key = (start_point[1], chosen_word)

    # As long as the new key is in the dictionary continue markoving
    # (moving to new states)
    while new_key in chains:

        value_list = chains[new_key]
        chosen_word = random.choice(value_list)
        output_text.append(chosen_word)

        new_key = (new_key[1], chosen_word)

    # Converts our Markov [] to a string
    return (" ".join(output_text))

# n-grams not fully implemented, manke_n_chains() partially finished
# [::n-1] step slicing ???
def make_n_chains(text_string, n):
    """Take input text as string; return dictionary of Markov chains with n-grams"""

    # Initializes chains as an empty dictionary
    chains = {}
    # Splits text_string on white space and assigns to variable
    all_the_words = text_string.split()
    # Initializes empty key list
    key = []
    # Initializes value as the next word after the end of our key tuple
    value = all_the_words[n]

    # Loops n times to make the key tuple
    # for index in range(len(all_the_words) - n):
    # #currently only looping n times to make the first dictionary entry and then stopping
    #     start = 0
    #     for i in range(start, n):
    #         key.append(all_the_words[i])
    #         start += 1
    #         n += 1
    for i in range(n):
        key.append(all_the_words[i])
        # print(key)
    key = tuple(key)

    if key not in chains:
        lst = []
        lst.append(value)
        chains[key] = lst

    chains[key].append(value)

    print(chains)
    return chains


# possible helper stub for key making
# def key_helper(key, n):
#     for i in range(n):
#         key.append(all_the_words[i])
#     return key


# possible helper stub for value updating
# def value_helper(value):
#     lst = []
#     lst.append(value)
#     chains[key] = lst
#     return lst


def make_n_text(chains, n):
    """Return text from chains using n-grams."""

    # Initializes our output as list
    output_text = []

    # Makes a list of all the keys in the dictionary
    key_list = list(chains.keys())
    # Initialized a blank list for holding key tuple slices
    addtl_key_list = []
    # Our randomized start point for the chain
    start_point = random.choice(key_list)
    # Pulls the values associated with our start point from the dictionary
    value_list = chains[start_point]
    # Chooses a random word from the value list associated with the start point key
    chosen_word = random.choice(value_list)

    # Adding value at index i in our starting point tuple to our output
    for i in range(n):
        output_text.append(start_point[i])

    # Creates a new state with the second word from previous state and the
    # randomly chosen word, This is the code moving through the Markov chain
    # Loop grabs the last n-1 words of the key tuple and puts them in a list
    for i in range(-n, -1):
        addtl_key_list.append(start_point[i])
    # addtl_key_list appends the nth word onto the list
    addtl_key_list.append(chosen_word)
    # new_key makes the addtl_key_list into a tuple
    new_key = tuple(addtl_key_list)

    print(new_key)

    # As long as the new key is in the dictionary continue markoving
    # (moving to new states)
    while new_key in chains:

        value_list = chains[new_key]
        chosen_word = random.choice(value_list)
        output_text.append(chosen_word)
        n_key_list = []

        # 
        for i in range():
            print("here")
            n_key_list.append(new_key[i])
            # addtl_key_list appends the nth word onto the list
        n_key_list.append(chosen_word)
        # new_key makes the addtl_key_list into a tuple
        new_key = tuple(n_key_list)

    # Converts our Markov [] to a string
    return (" ".join(output_text))


# No need with new version of open_and_read_file with user input
# input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file()
n = input("Please enter amount n for n-gram: ")
n = int(n)
# Get a Markov chain
chains = make_n_chains(input_text, n)

# Produce random text
# random_text = make_text(chains)
random_text = make_n_text(chains, n)

print(random_text)
