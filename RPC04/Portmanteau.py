#solucion
def asd(word):
    for i in range(1, len(word)):
        if word[i] in "aeiou":
            return i
    return None

word1 = input()
v1 = asd(word1)
word2 = input()
v2 = asd(word2[::-1])
# print(v1,v2)
if v2 and word2[len(word2) - 1 - v2] in "aeiou":
    print(word1[:v1] + word2[len(word2) - 1 - v2:])
elif v1 and word1[v1] in "aeiou":
    print(word1[:v1+1] + word2[v2:])
else:
    print(word1[:v1] + "o" + word2[v2:])