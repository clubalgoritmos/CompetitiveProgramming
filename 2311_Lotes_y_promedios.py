# https://jv.umsa.bo/oj/problem.php?id=2311
#  Lotes y promedios
#  Enviar
#  Estado
#  Descripción
#    Dado un lote de $n$ números enteros. Almacenar en un vector los promedios de cada par de elementos adyacentes del lote, hasta ahi tendremos $n - 1$ elementos en el vector, el elemento $n$ será el promedio del primer y ultimo elemento del lote, a continuación un ejemplo:
#    Dado un lote de $n$ números enteros. Almacenar en un vector los promedios de cada par de elementos adyacentes del lote, hasta ahi tendremos $n - 1$ elementos en el vector, el elemento $n$ será el promedio del primer y ultimo elemento del lote, a continuación un ejemplo:
#    Dado un lote de $n$ números enteros. Almacenar en un vector los promedios de cada par de elementos adyacentes del lote, hasta ahi tendremos $n - 1$ elementos en el vector, el elemento $n$ será el promedio del primer y ultimo elemento del lote, a continuación un ejemplo:
#    Dado un lote de $n = 10$ elementos: $45$, $20$, $8$, $12$, $3$, $32$, $6$, $21$, $5$, $1$, tenemos:
#    Dado un lote de $n = 10$ elementos: $45$, $20$, $8$, $12$, $3$, $32$, $6$, $21$, $5$, $1$, tenemos:
#    Dado un lote de $n = 10$ elementos: $45$, $20$, $8$, $12$, $3$, $32$, $6$, $21$, $5$, $1$, tenemos:
#    Por tanto el vector resultante es: $32.5$ $14.0$ $10.0$ $7.5$ $17.5$ $19.0$ $13.5$ $13.0$ $3.0$ $23.0$
#    Por tanto el vector resultante es: $32.5$ $14.0$ $10.0$ $7.5$ $17.5$ $19.0$ $13.5$ $13.0$ $3.0$ $23.0$
#    Por tanto el vector resultante es: $32.5$ $14.0$ $10.0$ $7.5$ $17.5$ $19.0$ $13.5$ $13.0$ $3.0$
#    $14.0$
#    $7.5$
#    $19.0$
#    $13.0$
#    $23.0$
#    $23.0$
#   Entrada
#    La primera línea de entrada consiste en un número $n$ ($2 \leq n \leq 1000$), el cual indica el tamaño del lote.Le siguen $n$ líneas, donde $n_{i}$($1 \leq n_{i} \leq 10^{3}$) es el i-ésimo elemento del lote.
#    La primera línea de entrada consiste en un número $n$ ($2 \leq n \leq 1000$), el cual indica el tamaño del lote.Le siguen $n$ líneas, donde $n_{i}$($1 \leq n_{i} \leq 10^{3}$) es el i-ésimo elemento del lote.
#    La primera línea de entrada consiste en un número $n$ ($2 \leq n \leq 1000$), el cual indica el tamaño del lote.Le siguen $n$ líneas, donde $n_{i}$($1 \leq n_{i} \leq 10^{3}$) es el i-ésimo elemento del lote.
#   Salida
#    Imprima el vector resultante. (Debe existir un espacio entre cada par de elementos adyacentes), cada elemento del vector resultante debe imprimirse con un decimal de precisión.
#    Imprima el vector resultante. (Debe existir un espacio entre cada par de elementos adyacentes), cada elemento del vector resultante debe imprimirse con un decimal de precisión.
#    Imprima el vector resultante. (Debe existir un espacio entre cada par de elementos adyacentes), cada elemento del vector resultante debe imprimirse con un decimal de precisión.
#   Ejemplo Entrada
#    10452081233262151
#   Ejemplo Salida
#    32.5 14.0 10.0 7.5 17.5 19.0 13.5 13.0 3.0 23.0
#   Ayuda
#    En Python para imprimir con $1$ decimal de precisión se debe usar print("{:.1f}".format(variable))
#    En Python para imprimir con $1$ decimal de precisión se debe usar print("{:.1f}".format(variable))
#    En Python para imprimir con $1$ decimal de precisión se debe usar
#    print("{:.1f}".format(variable))

lotes = []
resultados = []
inline = int(input())
for k in range(inline+1):
    if k < 1:
        lotes.append(int(input()))
    elif k >= inline:
        #lotes.append(int(input()))
        resultados.append((lotes[k-1] + lotes[0])/2)
    else:
        lotes.append(int(input()))
        resultados.append((lotes[k-1] + lotes[k])/2)
        
print(' '.join(map(str, resultados)))