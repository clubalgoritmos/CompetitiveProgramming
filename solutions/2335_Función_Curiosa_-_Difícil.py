# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=192
## https://jv.umsa.bo/oj/problem.php?id=2335
#    Copiado al portapapeles
#  Función Curiosa - Difícil
#  Enviar
#  Estado
#  Descripción
#    Considere la función que halla la suma de los dígitos de un numero al cuadrado modulo 9.Por ejemplo si $n=16$ se tiene $f^0(16)=(1+6)^2 \mod(9)=4$Ahora se define $f^1(n)=f(f^0(n))$, $f^2(n)=f(f^1(f^0(n)))$ y así sucesivamenteHalle la $\sum_{i=0}^k f^i$Por ejemplo, si n=124 y k=3 tenemos, $(1+2+4)\%9=7$\[f^0(124)=49,f(49)=16,f(16)=49, f(49)=16\]La suma pedida es 49+16+49+16=130
#   Entrada
#    La entrada consiste de múltiples casos de prueba. La primera línea indica el número de casos de prueba.Las líneas siguientes contienen dos números $(1 \leq n,k \leq 10^8)$.
#   Salida
#    En la salida escriba el resultado de la suma pedida.
#   Ejemplo Entrada
#    2124 3124 4
#   Ejemplo Salida
#    130179
#   Ayuda

