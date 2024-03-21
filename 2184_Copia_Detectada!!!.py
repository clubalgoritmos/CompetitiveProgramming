# https://jv.umsa.bo/oj/problem.php?id=2184
## https://jv.umsa.bo/oj/problem.php?id=2184
#  Copia Detectada!!!
#  Enviar
#  Estado
#  Descripción
#    Hoy se llevó a cabo el examen de liberación de INF-111, los estudiantes inscritos en este examen creyeron que no habria control de copias, pero no fue así, ya que auxiliar Ivan se dió cuenta que los estudiantes copiarón en pleno examen, Ivan registró las notas de los examenes en un vector, se le da un vector $a$ que consta de $n$ ($n \geq 3$) números enteros positivos los cuales representan las notas de los estudiantes. Se sabe que en este vector de notas, todos las notas excepto uno son iguales (por ejemplo, en la vector [$4$,$11$,$4$,$4$] todos las notas excepto una son iguales a $4$), Ivan sabe que todos menos uno se copiaron en el examen, ayúdalo a encontrar la nota de esta persona para no invalidar su examen.
#    Hoy se llevó a cabo el examen de liberación de INF-111, los estudiantes inscritos en este examen creyeron que no habria control de copias, pero no fue así, ya que auxiliar Ivan se dió cuenta que los estudiantes copiarón en pleno examen, Ivan registró las notas de los examenes en un vector, se le da un vector $a$ que consta de $n$ ($n \geq 3$) números enteros positivos los cuales representan las notas de los estudiantes. Se sabe que en este vector de notas, todos las notas excepto uno son iguales (por ejemplo, en la vector [$4$,$11$,$4$,$4$] todos las notas excepto una son iguales a $4$), Ivan sabe que todos menos uno se copiaron en el examen, ayúdalo a encontrar la nota de esta persona para no invalidar su examen.
#    Hoy se llevó a cabo el examen de liberación de INF-111, los estudiantes inscritos en este examen creyeron que no habria control de copias, pero no fue así, ya que auxiliar Ivan se dió cuenta que los estudiantes copiarón en pleno examen, Ivan registró las notas de los examenes en un vector, se le da un vector $a$ que consta de $n$ ($n \geq 3$) números enteros positivos los cuales representan las notas de los estudiantes. Se sabe que en este vector de notas, todos las notas excepto uno son iguales (por ejemplo, en la vector [$4$,$11$,$4$,$4$] todos las notas excepto una son iguales a $4$), Ivan sabe que todos menos uno se copiaron en el examen, ayúdalo a encontrar la nota de esta persona para no invalidar su examen.
#    Imprime el índice del elemento que no es igual a otros. Los números del vector se numeran a partir de cero.
#    Imprime el índice del elemento que no es igual a otros. Los números del vector se numeran a partir de cero.
#    Imprime el índice del elemento que no es igual a otros. Los números del vector se numeran a partir de cero.
#   Entrada
#    La primera línea contiene un solo entero $t$ ($1 \leq t \leq 100$). Luego siguen $t$ casos de prueba.
#    La primera línea contiene un solo entero $t$ ($1 \leq t \leq 100$). Luego siguen $t$ casos de prueba.
#    La primera línea contiene un solo entero $t$ ($1 \leq t \leq 100$). Luego siguen $t$ casos de prueba.
#    La primera línea de cada caso de prueba contiene un solo entero $n$ ($3 \leq n \leq 100$) - la longitud del vector $a$(de notas).
#    La primera línea de cada caso de prueba contiene un solo entero $n$ ($3 \leq n \leq 100$) - la longitud del vector $a$(de notas).
#    La primera línea de cada caso de prueba contiene un solo entero $n$ ($3 \leq n \leq 100$) - la longitud del vector $a$(de notas).
#    La segunda línea de cada caso de prueba contiene $n$ números enteros $a_{0}$, $a_{1}$,…, $a_{n-1}$ ($1 \leq a_{i} \leq 100$).
#    La segunda línea de cada caso de prueba contiene $n$ números enteros $a_{0}$, $a_{1}$,…, $a_{n-1}$ ($1 \leq a_{i} \leq 100$).
#    La segunda línea de cada caso de prueba contiene $n$ números enteros $a_{0}$, $a_{1}$,…, $a_{n-1}$ ($1 \leq a_{i} \leq 100$).
#    Se garantiza que todos los números excepto uno en el vector $a$ sean iguales.
#    Se garantiza que todos los números excepto uno en el vector $a$ sean iguales.
#    Se garantiza que todos los números excepto uno en el vector $a$ sean iguales.
#   Salida
#    Para cada caso de prueba, genere un único entero: el índice del elemento que no es igual a los demás.
#    Para cada caso de prueba, genere un único entero: el índice del elemento que no es igual a los demás.
#    Para cada caso de prueba, genere un único entero: el índice del elemento que no es igual a los demás.
#   Ejemplo Entrada
#    4411 13 11 1151 4 4 4 4103 3 3 3 10 3 3 3 3 3320 20 10
#   Ejemplo Salida
#    1042
#   Ayuda

for _ in range(int(input())):
    N = int(input())
    A = list(map(int,input().split()))
    for x in set(A):
        if A.count(x)==1:
            print(A.index(x))
            break
    