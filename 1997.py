M = [["a","b","c","d","e","f","g","h","i","j"],
["k","l","m","n","o","p","q","r","s","t"],
["u","v","w","x","y","z"," ","*","bks"]]

def encuentra_x_desde_ij(x,i,j):
    for i1 in range(3):
        for j1 in range(10):
            if M[i1][j1]==x:
                return abs(i1-i)+abs(j1-j),i1,j1

for _ in range(int(input())):
    S = input()+"*"
    i,j=0,0
    su=0
    for s in S:
        s,i,j=encuentra_x_desde_ij(s,i,j)
        su+=s
    print(su)        