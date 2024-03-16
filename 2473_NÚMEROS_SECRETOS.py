# https://jv.umsa.bo/oj/problem.php?cid=2566&pid=2
#  NÚMEROS SECRETOS
#  Estado
#  Descripción
#    Dianita, debe enviar a Dereck, la clave de acceso de su candado, este candado tiene 3 cifras entre 0 y 9. Sin embargo, para que no sea tan evidente las 3 cifras, suma las mismas conjugando estos números, y envía exactamente 7 números. Ayuda a Dereck a encontrar esos 3 dígitos que son la clave del candado.
#    Dianita, debe enviar a Dereck, la clave de acceso de su candado, este candado tiene 3 cifras entre 0 y 9. Sin embargo, para que no sea tan evidente las 3 cifras, suma las mismas conjugando estos números, y envía exactamente 7 números. Ayuda a Dereck a encontrar esos 3 dígitos que son la clave del candado.
#   Entrada
#    La primera línea contiene el número de casos de prueba.
#    La primera línea contiene el número de casos de prueba.
#    Cada caso de prueba consiste en una línea que contiene exactamente 7 dígitos.
#    Cada caso de prueba consiste en una línea que contiene exactamente 7 dígitos.
#   Salida
#    Se imprime los 3 dígitos separados por un espacio, que serían la clave del candado.
#    Se imprime los 3 dígitos separados por un espacio, que serían la clave del candado.
#   Ejemplo Entrada
#    44 6 7 10 11 13 171 3 4 5 6 8 91 4 5 8 9 12 131 1 2 9 10 10 11
#   Ejemplo Salida
#    4 6 71 3 51 4 81 1 9
#   Ayuda

for _ in range(int(input())):
    arr = list(map(int, input().split()))
    arr.sort()
    print(arr[0], end=" ")
    print(arr[1], end=" ")
    a=2
    sw=False
    while a<len(arr) and sw==False:
        for i in range(a):
            for j in range(i+1,a):
                if not arr[i]+arr[j]==arr[a]:
                    print(arr[a])
                    sw=True
                    break
            if sw:
               break
        a+=1