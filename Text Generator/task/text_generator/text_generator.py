from nltk.tokenize import WhitespaceTokenizer
from nltk.util import bigrams

tokenizer = WhitespaceTokenizer()
filename = input()
f = open(filename, "r", encoding="utf-8")

tokens = tokenizer.tokenize(f.read())
bigrm = bigrams(tokens)
bigram_tuple = tuple(bigrm)

while True:
    try:
        user_input = input()
        if user_input == 'exit':
            break
        print(f'Head: {user_input}')
        dict_of_words = {}
        for words in bigram_tuple:
            if words[0] == user_input:
                if words[1] in dict_of_words:
                    dict_of_words[words[1]] += 1
                else:
                    dict_of_words[words[1]] = 1
        if dict_of_words[user_input] == 0:
            raise KeyError
        for key, item in dict_of_words.items():
            print(f'Tail: {key} Count: {item}')
    except TypeError:
        print('Type Error. Please input an integer.')
    except IndexError:
        print('Index Error. Please input an integer that is in the range of the corpus.')
    except ValueError:
        print('ValueError. Please input an integer')
    except KeyError:
        print('Key Error. The requested word is not in the model. Please input another word.')
