#solucion
n = int(input())
ex = input()
def convertir(s):
    r=str()
    for i in range(len(s)):
        if s[i] in ex:
            if i == list(ex).index(s[i]):
                r+="*"
            else:
                r+="!"
        else:
            r+="X"
    return r
arr = [convertir(ex)]+[convertir(input()) for _ in range(n-1)]
for _ in range(int(input())):
    print(arr.count(input()))