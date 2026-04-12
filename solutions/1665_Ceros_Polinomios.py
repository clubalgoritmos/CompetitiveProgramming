# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=119
## https://jv.umsa.bo/oj/problem.php?id=1665
#    Copiado al portapapeles
#  Ceros Polinomios
#  Enviar
#  Estado
#  Descripción
#    dada una función continua en un intervalo $[a,b]$ tal que $f ( a ) f ( b ) < 0$ un teorema básico de las matemáticas estipula que al menos un cero de $f$ en $( a, b )$ debe existir. Esto significa que existe un numero real $z$ tal que $a < z < b$ y $f ( z ) = 0$.Dado el polinomio $ p ( x ) = c_4x^4 + c_3x^3 + c_2x^2 + c_1x + c_0 $ con exactamente un cero en el rango $ ( 0, 1 )$. ¿Puede hallar este cero?
#   Entrada
#    Cada linea de la entrada describe un polinomio $p(x)$ con grado máximo de 4. Con exactamente un cero en el rango $(0,1)$. Cada polinomio se describe en orden decreciente como sigue: $c_4x^4 c_3x^3 c_2x^2 c_1x^1 c_0 0$. EL ultimo cero describe el final de la entrada. Cada numero esta separado por un espacio.
#    Cada $c_i$ es un numero real. Los pares $c_i i$ con $i=0$ no figuran en la entrada.
#   Salida
#    Por cada polinomio imprima una aproximación del cero $z$ en $(0,1)$, con la convención que z debe ser un numero real con exactamente 5 decimales después del punto decimal, tal que$0 \leq z \leq 0.99999$ y $p ( z ) p ( z + 0.00001 ) < 0$.
#   Ejemplo Entrada
#    -1 2 0.5 04 3 -6 1 1 04.65 4 -0.11 3 0.53 2 -6.51 1 0.13 06.31 4 7.64 3 -5.29 2 0.55 1 -9.2 0
#   Ejemplo Salida
#    0.707110.169940.020000.99974
#   Ayuda

