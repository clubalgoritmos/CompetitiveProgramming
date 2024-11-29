# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=134
## https://jv.umsa.bo/oj/problem.php?id=1716
#    Copiado al portapapeles
#  Automatón
#  Enviar
#  Estado
#  Descripción
#    Pepito Pérez encontró la siguiente definición en Wikipedia: Autómata finito no determinista (AFND) Está representado formalmente por M = (Q, Ʃ, q0, F, Δ) donde:
#    Q: es un conjunto finito de estados.
#    Ʃ: es un alfabeto.
#    q0:es un estado inicial q0 ∈ Q.
#    ∈
#    F: es un conjunto de estados finales o de aceptación F⊆Q.
#    ⊆
#    Δ: es una función de transición Δ: Q x Ʃ→ P(Q).
#    Donde P(Q) es el conjunto potencia de Q. Sea w = a1,a2,…,an una palabra sobre el alfabeto Ʃ. El autómata finito no determinista M acepta la palabra w si existe una secuencia de estados r0,r1,…,rn en Q con las siguientes condiciones:
#    r0 = q0.
#    ri+1 ∈Δ (ri, ai+1), para i = 0, 1,.., n-1.
#    rn ∈ F.
#    F.
#    En otras palabras, la primera condición dice que la máquina se inicia en el estado de inicio q0. La segunda condición dice que para cada carácter de la cadena w, la máquina pasará de estado a estado de acuerdo con la función de transición A. La última condición dice que la máquina acepta w si la última entrada de w hace que la máquina esté en uno de Los estados de aceptación. Para que w sea aceptado por M, no es necesario que cada secuencia de estado termine en un estado de aceptación, es suficiente si uno lo hace. Por otra parte, si es imposible pasar de q0 a un estado de F siguiendo w, se dice que el autómata rechaza la cadena. El conjunto de cadenas que M acepta es el idioma reconocido por M y este lenguaje se denota por L(M).
#    Pepito implementó el autómata finito no determinista pero el tiempo de ejecución es demasiado grande para el reconocimiento de palabras. Pepito ha escuchado que cada palabra puede ser reconocida en O(|w|), ¡pero Pepito no tiene idea de cómo hacerlo! ¿Puedes ayudarlo?
#   Entrada
#    La entrada comienza con un entero t (1≤t≤10), el número de casos de prueba. La primera línea del caso de prueba contiene cuatro enteros positivos separados por espacios n m s k (1≤n≤18, 1≤m≤8424, 1≤s≤26, 1≤k≤n), que representan el número de estados, el número de transiciones, el número de símbolos alfabéticos y el número de estados de aceptación, respectivamente. La segunda línea contiene exactamente s diferentes símbolos separados por espacios o1, o2, o3,..., os (oi ∈ {a, b, c, d,..., z}, oi es cualquier letra minúscula del alfabeto inglés).
#    El alfabeto Ʃ está ordenado lexicográficamente. La tercera línea contiene exactamente k números enteros no negativos separados por espacios F1, F2,..., Fk (0≤i<n, para 0≤i≤k), estos son los estados de aceptación. El caso de prueba continúa con m líneas, cada una de ellas con una transición del autómata x y c (0≤x, y<n, c ∈Ʃ), donde x, y, c son el origen, el destino y la etiqueta de la transición, respectivamente. Luego se presenta una línea que contiene un entero positivo q que representa el total de palabras que se evaluarán en los autómatas, finalmente, se presentan q líneas, cada una de las cuales contiene una palabra w (w ∈Ʃ+, 1≤w≤105, que es decir, las palabras w tienen una longitud entre 1 y 105).
#   Salida
#    Para cada caso de prueba, debe imprimir q líneas individuales, cada línea que contenga la palabra Yes o No, dependiendo de si la palabra w ∈ L(M).
#   Ejemplo Entrada
#    15 12 2 2a b0 20 3 a0 1 b1 1 a1 1 b1 3 b2 0 a2 1 a2 4 b3 2 a3 4 b4 2 a4 4 a10aaaaaaaaababababbbbbaaaababaababbaabbababbbbaababbaabbaa
#   Ejemplo Salida
#    YesNoYesNoNoYesNoNoYesYes
#   Ayuda
#    Use metodos fast I/O.

