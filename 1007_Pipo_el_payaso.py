# https://jv.umsa.bo/oj/problem.php?id=1007
#  Pipo el payaso
#  Enviar
#  Estado
#  Descripción
#   Entrada
#   Salida
#   Ejemplo Entrada
#    22tres tristes tigres tragan trigo en un trigalpedro picapiedra pone piedras3pepe puede comer camarones picantespablito clavo un clavito sobre la cabeza de un calvitoprometo prometo prometo prometo prometo prometo prometo prometo
#   Ejemplo Salida
#    El ganador es 1El ganador es 3
#   Ayuda

def obtCantPref(n):     
    pre = []
    for i in n:
        pre.append(i[0])
    letra = []
    mayor = 0
    for i in pre:       
        if i in letra:  
            continue
        letra.append(i) 
        nu = pre.count(i)
        if nu > mayor:  
            mayor = nu
    return mayor        


casos = int(input())
for i in range(casos):
    jug = []
    num = int(input())
    cant = []
    mayor = 0
    for j in range(num):            
        frase = input().split()
        nu = obtCantPref(frase)     
        if nu > mayor:              
            mayor = nu
        cant.append(nu)             
    print("El ganador es "+str(cant.index(mayor)+1)) 