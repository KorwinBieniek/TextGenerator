from nltk.tokenize import WhitespaceTokenizer
from nltk.probability import FreqDist
from nltk.util import bigrams

tokenizer = WhitespaceTokenizer()
filename = input()
f = open(filename, "r", encoding="utf-8")

tokens = tokenizer.tokenize(f.read())
bigrm = bigrams(tokens)
bigram_tuple = tuple(bigrm)
fdist = FreqDist(tokens)

print(f'Number of bigrams: {len(bigram_tuple)}\n')

while True:
    user_input = input()
    if user_input == 'exit':
        break
    try:
        user_input = int(user_input)
        print(f'Head: {bigram_tuple[user_input][0]}\t Tail: {bigram_tuple[user_input][1]}')
    except TypeError:
        print('Type Error. Please input an integer.')
    except IndexError:
        print('Index Error. Please input an integer that is in the range of the corpus.')
    except ValueError:
        print('ValueError. Please input an integer')