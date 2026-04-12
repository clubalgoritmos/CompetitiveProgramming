from itertools import product

vocales = {"A","E","I","O","U","Y"}
N = int(input())
words = [input() for i in range(N)]
prefixes = [[word[:i] for i in range(1, min(4, len(word) + 1))] for word in words]

for acronym in product(*prefixes):
    acronym = ''.join(acronym)
    if all(any(char in vocales for char in acronym[i:i+3]) for i in range(len(acronym)-2)):
        print(len(acronym))
        break
else:
    print('*')