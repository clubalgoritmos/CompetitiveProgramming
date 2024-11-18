#solucion
P,  B = map(int,input().split())
if B < 2 * P - 1:
    print("*")
    exit()

def encontrar_xyz(B, P, x):
    y = (B - P) - 2 * x
    z = P - x - y
    return x, y, z

for x in range(P+1):
    x, y, z = encontrar_xyz(B, P, x)
    if min(x,y,z)<0:
        continue
    S = "-X-"*x+"X-"*y+"X"*z
    if 3*x+2*y+z==B:
        print(S)
        exit()
print("*")
    

#while len(S)<B:
#    espacio = Ratio
#    if Resto>0:
#        espacio+=1
#        n = Resto
#        Resto=0
#    else:
#        n = (B - len(S))//espacio
#
#    if espacio==3:
#        S+="-X-"*n
#        continue
#    if espacio==2:
#        S+="X-"*n
#        continue
#    S+="X"
#print(S)