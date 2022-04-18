import random

from nltk.tokenize import WhitespaceTokenizer
from nltk.util import ngrams


def open_file():
    filename = input()
    return open(filename, "r", encoding="utf-8")


def create_trigrams(f):
    tokenizer = WhitespaceTokenizer()
    text = f.read()
    tokens = tokenizer.tokenize(text)
    trigrm = ngrams(tokens, 3)
    trigram = list()
    for x in trigrm:
        trigram.append((x[0] + " " + x[1], x[2]))
    return trigram


def count_tail_occurrences(trigram_tuple, word):
    dict_of_words = {}
    for words in trigram_tuple:
        if words[0] == word:
            if words[1] in dict_of_words:
                dict_of_words[words[1]] += 1
            else:
                dict_of_words[words[1]] = 1
    return dict_of_words


def return_next_word(word):
    dict_of_occurences = count_tail_occurrences(trigram_tuple, word)
    dict_of_occurences = dict(sorted(dict_of_occurences.items(), key=lambda item: item[1], reverse=True))
    list_of_next_words = list(dict_of_occurences.keys())[:3]
    return random.choice(list_of_next_words)


def generate_pseudo_sentence(trigram_tuple):
    first_tuple = random.choice(trigram_tuple)
    while True:
        first_token = first_tuple[0].split()
        if first_token[0][0].isupper() and first_token[0][-1] not in '.!?' and first_token[1][-1] not in '.!?':
            break
        else:
            first_tuple = random.choice(trigram_tuple)
    pseudo_sentence = first_tuple[0]
    last_word = pseudo_sentence.split(" ")[-1]
    next_word = last_word + " " + return_next_word(pseudo_sentence)
    pseudo_sentence += f" {next_word.split()[1]}"
    while len(pseudo_sentence.split()) < 5:
        next_word = pseudo_sentence.split(" ")[-1] + " " + return_next_word(next_word)
        pseudo_sentence += f" {next_word.split()[1]}"
    while next_word[-1] not in '.?!':
        next_word = pseudo_sentence.split(" ")[-1] + " " + return_next_word(next_word)
        pseudo_sentence += f" {next_word.split()[1]}"
    print(pseudo_sentence)


f = open_file()
trigram_tuple = create_trigrams(f)
first_tuple = random.choice(trigram_tuple)
for i in range(10):
    generate_pseudo_sentence(trigram_tuple)
