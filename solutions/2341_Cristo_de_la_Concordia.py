# https://jv.umsa.bo/oj/problem.php?cid=2575&pid=10
## https://jv.umsa.bo/oj/problem.php?id=2341
#  Cristo de la Concordia
#  Estado
#  Descripción
#    Autor: Rodrigo Joaquin Salguero Morales - Universidad Mayor de San Simón
#    A Don Peyote le gusta visitar la ciudad de Cochabamba que se encuentra en el centro de Bolivia, la ciudad de Cochabamba tiene un atractivo turístico, el Cristo de la Concordia, que se encuentra en la cima del Cerro San Pedro, para llegar a el se puede subir en teleférico y también se puede subir por las gradas. Don Peyote sube las gradas del Cristo de la Concordia que contiene 1399 escalones, a él le gusta jugar y subir 1, 2 y hasta 3 escalones de un solo paso, pero después de subir 3 escalones de un paso, se cansa y en el siguiente paso solo puede subir 1 o 2 peldaños de un solo paso.Don Peyote se suele preguntar ¿De cuántas formas distintas se podrá subir al Cristo combinando pasos de longitud 1, 2 y 3 escalones? dos formas se consideran distintas si difieren en al menos la longitud de un solo paso.Don Peyote siempre tiene sueños muy extraños, esta vez se soñó que existen muchos Cristos de la Concordia y algunos tienen una cantidad extremadamente grande de peldaños. Don Peyote necesita tu ayuda para responder a la pregunta para cada longitud distinta que se le presente, como la respuesta puede ser muy larga Don Peyote te pide que le des cada respuesta modulo $10^9+7$.
#   Entrada
#    La primera línea contiene un entero $n$ $(1 \le n \le 10^4)-$ la cantidad de Cristos que existen en el sueño de Don Peyote.Cada una de las siguientes $n$ líneas contiene un entero. La $i$-ésima línea contiene el entero $X_i$ $(1 \le X_i \le 10^{18})-$ la cantidad de gradas que tiene cada Cristo.
#   Salida
#    Para cada Cristo imprime la respuesta, la cantidad de formas de subir a cada Cristo modulo $10^9+7$
#   Ejemplo Entrada
#    512361399
#   Ejemplo Salida
#    12423260300372
#   Ayuda

for _ in range(int(input())):
    n = int(input())
    dp = [0,1,2,4]
    for i in range(4,n+1):
        dp.append((dp[i-1]+dp[i-2]+dp[i-3])%1000000007)
    print(dp[n])