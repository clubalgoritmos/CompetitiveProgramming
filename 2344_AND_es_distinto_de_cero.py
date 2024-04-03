# https://jv.umsa.bo/oj/problem.php?cid=2819&pid=3
## https://jv.umsa.bo/oj/problem.php?id=2344
#  AND es distinto de cero
#  Enviar
#  Estado
#  Descripción
#    Se le da un vector que consta de todos los números enteros de $[l, r]$ inclusive. Por ejemplo, si $l = 2$ y $r = 5$, el vector sería $[2,3,4,5]$. ¿Cuál es el número mínimo de elementos que puede eliminar para hacer que el AND bit a bit del vector no sea cero?
#  AND bit a bit
#    Un AND bit a bit es una operación binaria que toma dos representaciones binarias de igual longitud y realiza la operación AND en cada par de los bits correspondientes.
#   Entrada
#    La primera línea contiene un número entero $t$ ($1 \leq t \leq 10^4$) - el número de casos de prueba. Luego siguen $t$ casos.
#    La primera línea de cada caso de prueba contiene dos números enteros $l$ y $r$ ($1 \leq l \leq r \leq 2⋅10^{5}$): la descripción del vector.
#   Salida
#    Para cada caso de prueba, genere un único entero: la respuesta al problema.
#   Ejemplo Entrada
#    51 22 84 51 5100000 200000
#   Ejemplo Salida
#    130231072
#   Ayuda
#    En el primer caso de prueba, el vector es $[1,2]$. Actualmente, el AND bit a bit es $0$, como $1 \& 2 = 0$. Sin embargo, después de eliminar $1$ (o $2$), el vector se convierte en $[2]$ (o $[1]$), y el AND bit a bit se convierte en $2$ (o $1$). Se puede demostrar que esto es lo óptimo, por lo que la respuesta es $1$.
#    En el segundo caso de prueba, el vector es $[2,3,4,5,6,7,8]$. Actualmente, el AND bit a bit es $0$. Sin embargo, después de eliminar $4$, $5$ y $8$, el vector se convierte en $[2,3,6,7]$, y el AND bit a bit se convierte en $2$. Esto puede demostrarse que es el óptimo, por lo que el la respuesta es $3$. Tenga en cuenta que puede haber otras formas de eliminar $3$ elementos.

for _ in range(int(input())):
    l, r = map(int, input().split())
    print(bin(l),bin(r))
    print(2**(len(bin(r))-3)-1 if l <= r//2 else r%l)