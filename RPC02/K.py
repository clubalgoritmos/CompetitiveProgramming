sequence = list(map(int, list(input().strip())))
c=0
while sequence != sorted(sequence):
    for i in range(len(sequence)-1):
        if sequence[i] > sequence[i+1]:
            sequence[i], sequence[i+1] = sequence[i+1], sequence[i]
            c+=1
print(c)