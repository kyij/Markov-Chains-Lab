"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file = open(file_path)
    text = file.read()
    file.close()

    return text


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

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

    words1 = text_string.split()
    
    for i in range(len(words1)- 2):
        key = (words1[i], words1[i+1])
        value = words1[i+2]

        if key not in chains:
            chains[key] = []

        chains[key].append(value)
        

    return chains


def make_text(chains):
    """Return text from chains."""

    # state (bubble you're on right)
    # total string (all the words you've chosen)
    
    key1 = choice(list(chains.keys())) # state (always a tuple of 2 words)
    words2 = [key1[0],key1[1]] # total string, add onto it as we generate more words
    random_word = choice(chains[key1])
    # make a while loop:
         # Look up the words that can come after your key
         # Use the choice function to pick a random word to add next
         # Append that to your words2 list
         # Change key1:   ('Would', 'you')  then we chose 'could'   =>  key1 = ('you', 'could')
            # key1 = (key1[1], random_word)
    while random_word is not None:
        key1 = (key1[1], random_word)
        words2.append(random_word)
        if key1 not in chains: 
            break
        print(words2)
        random_word = choice(chains[key1])
        

    return ' '.join(words2)


file_path = 'gettysburg.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(file_path)

# Get a Markov chain
chains = make_chains(input_text)
print(chains)
# Produce random text
random_text = make_text(chains)

print(random_text)
