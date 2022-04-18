import random

from nltk.tokenize import WhitespaceTokenizer
from nltk.util import bigrams


def open_file():
    filename = input()
    return open(filename, "r", encoding="utf-8")


def create_bigrams(f):
    tokenizer = WhitespaceTokenizer()
    text = f.read()
    tokens = tokenizer.tokenize(text)
    bigrm = bigrams(tokens)
    return tuple(bigrm)


def count_tail_occurrences(bigram_tuple, word):
    dict_of_words = {}
    for words in bigram_tuple:
        if words[0] == word:
            if words[1] in dict_of_words:
                dict_of_words[words[1]] += 1
            else:
                dict_of_words[words[1]] = 1
    return dict_of_words


def return_next_word(word):
    dict_of_occurences = count_tail_occurrences(bigram_tuple, word)
    return max(dict_of_occurences, key=dict_of_occurences.get)


def generate_pseudo_sentence(bigram_tuple):
    first_tuple = ''

    first_tuple = random.choice(bigram_tuple)
    while True:
        if first_tuple[0][0].isupper() and first_tuple[0][-1] not in '.!?':
            break
        else:
            first_tuple = random.choice(bigram_tuple)
    pseudo_sentence = first_tuple[0]
    next_word = return_next_word(pseudo_sentence)
    pseudo_sentence += f" {next_word}"
    while len(pseudo_sentence.split()) < 5:
        next_word = return_next_word(next_word)
        pseudo_sentence += f" {next_word}"
    while next_word[-1] not in '.?!':
        next_word = return_next_word(next_word)
        pseudo_sentence += f" {next_word}"
    print(pseudo_sentence)


f = open_file()
bigram_tuple = create_bigrams(f)

for i in range(10):
    generate_pseudo_sentence(bigram_tuple)
