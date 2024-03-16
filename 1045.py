import re
dics = set()
while True:
    try:
        S = input().split()
        for i in S:
            cleaned_word = re.sub(r'[^a-z]', '', i.lower())
            dics.add(cleaned_word)
    except EOFError:
        break
for a in sorted(dics):
    print(a)