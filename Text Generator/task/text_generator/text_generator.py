from nltk.tokenize import WhitespaceTokenizer
from nltk.probability import FreqDist

tokenizer = WhitespaceTokenizer()
filename = input()
f = open(filename, "r", encoding="utf-8")

tokens = tokenizer.tokenize(f.read())
fdist = FreqDist(tokens)

print('Corpus statistics\n'
      f'All tokens: {FreqDist(tokens).N()}\n'
      f'Unique tokens: {FreqDist(tokens).B()}')

while True:
    user_input = input()
    if user_input == 'exit':
        break
    try:
        user_input = int(user_input)
        print(tokens[user_input])
    except TypeError:
        print('Type Error. Please input an integer.')
    except IndexError:
        print('Index Error. Please input an integer that is in the range of the corpus.')
    except ValueError:
        print('ValueError. Please input an integer')