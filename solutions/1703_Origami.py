# https://jv.umsa.bo/oj/problem.php?id=1703
#  Origami
#  Enviar
#  Estado
#  Descripción
#    Marco Reus va a tener una fiesta muy pronto, y ha decidido invitar a sus amigos.
#    Marco Reus va a tener una fiesta muy pronto, y ha decidido invitar a sus amigos.
#    Marco Reus va a tener una fiesta muy pronto, y ha decidido invitar a sus amigos.
#    Quiere hacer invitaciones en forma de origami. Para cada invitación, necesita dos hojas rojas, cinco hojas verdes y ocho hojas azules. La tienda vende un número infinito de cuadernos de cada color, pero cada cuaderno consta de un solo color con k hojas Es decir, cada cuaderno contiene k hojas de rojo, verde o azul.Encuentra el número mínimo de cuadernos que Marco Reus necesita comprar para invitar a todos los n de sus amigos.
#    Quiere hacer invitaciones en forma de origami. Para cada invitación, necesita dos hojas rojas, cinco hojas verdes y ocho hojas azules. La tienda vende un número infinito de cuadernos de cada color, pero cada cuaderno consta de un solo color con k hojas Es decir, cada cuaderno contiene k hojas de rojo, verde o azul.Encuentra el número mínimo de cuadernos que Marco Reus necesita comprar para invitar a todos los n de sus amigos.
#    Quiere hacer invitaciones en forma de origami.
#    Para cada invitación, necesita dos hojas rojas, cinco hojas verdes y ocho hojas azules.
#    La tienda vende un número infinito de cuadernos de cada color, pero cada cuaderno consta de un solo color con
#    k
#    hojas
#    Es decir, cada cuaderno contiene
#    k
#    ojas de rojo, verde o azul.Encuentra el número mínimo de cuadernos que Marco Reus necesita comprar para invitar a todos los n de sus amigos.
#    ojas de rojo, verde o azul.
#    Encuentra el número mínimo de cuadernos que Marco Reus necesita comprar para invitar a todos los
#    n
#    de sus amigos.
#   Entrada
#    La primera línea contiene dos enteros n y k ( 1≤n, k≤108): el número de amigos de Petya y el número de hojas en cada cuaderno, respectivamente.
#    La primera línea contiene dos enteros n y k ( 1≤n, k≤108): el número de amigos de Petya y el número de hojas en cada cuaderno, respectivamente.
#    La primera línea contiene dos enteros n y k ( 1≤n, k≤108): el número de amigos de Petya y el número de hojas en cada cuaderno, respectivamente.
#   Salida
#    Imprima un número: el número mínimo de cuadernos que Marco Reus necesita comprar.
#    Imprima un número: el número mínimo de cuadernos que Marco Reus necesita comprar.
#    Imprima un número: el número mínimo de cuadernos que Marco Reus necesita comprar.
#   Ejemplo Entrada
#    3 515 6
#   Ejemplo Salida
#    1038
#   Ayuda

"""origami"""
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        line = line.split()
        n = int(line[0])        #asignamos los amigos
        k = int(line[1])        #cantidad de hojas
        hoj = [8, 5, 2]         #hojas por color
        c = 0                   #cantidad de cuadernos
        for i in hoj:
            a = n*i             #cantidad de hojas que se necesitan
            if(a%k!=0):         #control para saber cuantos cuadernos comprar por color
                c+=(a//k)+1
            else:
                c+=a//k
        print(c)                #cuadernos en total