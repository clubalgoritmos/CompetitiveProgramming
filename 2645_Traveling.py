# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=232
## https://jv.umsa.bo/oj/problem.php?id=2645
#    Copiado al portapapeles
#  Traveling
#  Enviar
#  Estado
#  Descripción
#    Hay una cuadrícula de tamaño \(n \times m\). Te encuentras en la celda \((1,1)\) y tu objetivo es llegar a la celda \((n,m)\).
#    Puedes moverte a las celdas vecinas hacia la derecha o hacia abajo. En otras palabras, supongamos que te encuentras en la celda \((x,y)\). Puedes:
#    - Moverte hacia la derecha a la celda \((x,y+1)\) — esto tiene un costo de \(x\) rupias.- Moverte hacia abajo a la celda \((x+1,y)\) — esto tiene un costo de \(y\) rupias.
#    ¿Puedes llegar a la celda \((n,m)\) gastando exactamente \(k\) rupias?
#   Entrada
#    La primera línea contiene el único entero \(t\) \((1 \leq t \leq 100)\) — el número de casos de prueba.
#    La primera y única línea de cada caso de prueba contiene tres enteros \(n\), \(m\) y \(k\) \((1 \leq n, m \leq 100; 0 \leq k \leq 10^4)\) — los tamaños de la cuadrícula y la cantidad exacta de dinero que necesitas gastar.
#   Salida
#    Para cada caso de prueba, si puedes llegar a la celda \((n, m)\) gastando exactamente \(k\) rupias, imprime "SI". De lo contrario, imprime "NO".
#   Ejemplo Entrada
#    61 1 02 2 22 2 32 2 41 4 3100 100 10000
#   Ejemplo Salida
#    SINOSINOSINO
#   Ayuda
#    En el primer caso de prueba, ya te encuentras en la celda final, por lo que no gastas rupias (0 rupias).
#    En el segundo, tercer y cuarto caso de prueba, hay dos caminos desde (1,1) hasta (2,2): (1,1) → (1,2) → (2,2) o (1,1) → (2,1) → (2,2). Ambos cuestan 1+2=3 rupias, por lo que es la única cantidad de dinero que puedes gastar.
#    En el quinto caso de prueba, hay una única ruta desde (1,1) hasta (1,4) y cuesta 1+1+1=3 rupias.

