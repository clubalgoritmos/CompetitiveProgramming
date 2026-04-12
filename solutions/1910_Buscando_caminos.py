# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=159
## https://jv.umsa.bo/oj/problem.php?id=1910
#    Copiado al portapapeles
#  Buscando caminos
#  Enviar
#  Estado
#  Descripción
#    Tienes un árbol que con $N$ vértices enumerado de $1, 2, 3, ... , N$, la raíz de este árbol es el vértice numero $1$. Un árbol es un grafo conectado no dirigido con $N - 1$ aristas.
#    Tu tienes que responder $m$ consultas, la $i$ - ésima consulta consiste en un conjunto de distintos $k_i$ vértices $v_i[1], v_i[2], ..., v_i[k_i]$, tu tarea es verificar si existe algún camino desde la raiz a algún vertice $u$, tal que cada vértice del conjunto $k$ pertenezca a este camino o este a distancia $1$ a algún vértice de este camino.
#   Entrada
#    La primera linea contiene dos enteros $n$, $m$ $(2 \leq n \leq 2 * 10 ^ 5, 1 \leq m \leq 2 * 10 ^ 5)$ el número de vértices en el árbol y el número de consultas.
#    Cada una de las $N - 1$ describe una conexión en el arbol, la $i$ - ésima linea tiene dos enteros $u_i$ y $v_i$ $(1 \leq u_i, v_i \leq N, u_i != v_i)$, que denota que ambos vértices estan conectados.
#    Se garantiza que las aristas dadas forman un árbol.
#    Lassiguientes $m$ lineas describen las consultas.
#    Las
#    siguientes $m$ lineas describen las consultas.
#    La $i$ - ésima consulta consta de dos lineas, empieza por un número entero $k_i$, $(1 \leq k_i \leq N)$, el número vértices en la consulta actual, la siguiente linea contiene a los siguientes $k_i$ enteros $v_i[1], v_i[2], ... , v_i[k_i]$ $(1 \leq v_i[j] <= N)$, donde $v_i[j]$ el $j$ - ésimo vértice de la $i$ - ésima consulta.
#    Se garantiza que todos los los vértices en una consulta son diferentes.
#    Se garantiza que la sumatoria del tamaño del conjunto $k_i$ de cada consulta no es mayor a $2 * 10 ^ 5$, en otras palabras. \begin{equation}\displaystyle\sum_{i = 1} ^ {m} k_i \leq 2 * 10 ^ 5 \end{equation}
#   Salida
#    Para cada consulta imprima "YES", si existe el camino buscado, caso contrario imprima "NO".
#   Ejemplo Entrada
#    10 11 21 31 42 52 63 77 87 99 1054 3 8 9 10
#   Ejemplo Salida
#    YES
#   Ayuda
#    La siguiente imagen corresponde al ejemplo anterior.
#    la primera consulta es $[4, 3, 8, 9, 10]$. La respuesta es "YES", porque tu puedes escoger el camino de la raiz $1$ al vértice $u = 10$, entonces los vértices $[3, 9, 10]$, pertenecen al camino de $1$ a $10$, y el vértice $8$ esta a distancia $1$ del vértice $7$ el cual pertenece a este camino, el vértice $4$ esta a distancia $1$ del vértice $1$ el cual pertenece a este camino.

