# https://jv.umsa.bo/oj/problem.php?cid=2567&pid=9&type=official_contest
## https://jv.umsa.bo/oj/problem.php?id=2482
#  110010 Aniversario
#  Enviar
#  Estado
#  Descripción
#    Es el 50 aniversario de la Carrera de Informática, por lo tanto hay muchos eventos (charlas, seminarios, bautizo, tarde de juegos, etc.), como también un concurso de programación. Todos quieren participar en algo, incluso los michis de la carrera.
#    El gato TOMY quiere participar en la competencia de programación, por ese motivo estaba estudiando la manipulación de los bits estas semanas, le fascinaba todo lo que se puede hacer con los operadores binarios (AND(&), OR(|), XOR(^)), como también las cosas que se pueden hacer con los operadores de desplazamiento hacia la izquierda (<<) y hacia la derecha (>>).
#    TOMY esta tan fascinado que quiere compartir todo lo que aprendió con su amigo el gato MILANESO, para que este también participe en la competencia, para no traumarle de por vida con el manejo de los bits, primeramente solo le explicó sobre como calcular la distancia Hamming entre2números. Por ejemplo, si tuviéramos2números:
#    TOMY esta tan fascinado que quiere compartir todo lo que aprendió con su amigo el gato MILANESO, para que este también participe en la competencia, para no traumarle de por vida con el manejo de los bits, primeramente solo le explicó sobre como calcular la distancia Hamming entre
#    2
#    números. Por ejemplo, si tuviéramos
#    números:
#    x = 1x=1,y =4y=4, tenemos que ver en su equivalente binario:2
#    x = 1x=1
#    x = 1
#    x=1
#    x=
#    x
#    =
#    1
#    ,
#    y =4y=4
#    y =4
#    y=4
#    y=
#    y
#    4
#    , tenemos que ver en su equivalente binario:
#    La distancia Hamming sería 2, ya que es la cantidad de bits que difieren entre x y y. Después de algo de práctica y una crisis existencial, el MILANESO ya entendió como poder calcular la distancia Hamming entre 2 números, asi que ahora quiere retar a TOMY en una competencia.
#    MILANESOtendrá 2 números (a y b), y TOMY también tendrá 2 números (c y d), Milaneso quiere ver si la distancia Hamming de sus 2 números supera a la distancia Hamming de los números de TOMY. Nuestra misión es calcular quien va a ganar, si MILANESOo TOMY o habrá un empate.
#   Entrada
#    La primera línea tendrá un valor t $(1 \leq t \leq 10^4$), que es la cantidad de casos de entrada. Las siguientes t líneas tendrán 4 números por línea: a ($0 \leq a \leq(2^{31})-1$), b ($0 \leq b \leq(2^{31})-1$), c ($0 \leq c \leq (2^{31})-1$), d ($0 \leq d \leq (2^{31})-1$), los 2 números de MILANESO y los 2 números de TOMY respectivamente.
#   Salida
#    Para cada caso de prueba imprimir en diferentes líneas y en letras mayúsculas:MILAsi la distancia Hamming de los números del MILANESO es más grande que la distancia Hamming de TOMY, caso contrario imprimir TOMY, y en caso de empate imprimir EMPATE.
#   Ejemplo Entrada
#    77 10 7 134 3 6 57 3 18 139 10 3 816 17 10 711 12 5 1618 7 8 6
#   Ejemplo Salida
#    MILAMILATOMYTOMYTOMYEMPATEEMPATE
#   Ayuda

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    x = a ^ b
    y = c ^ d
    if bin(x).count("1") > bin(y).count("1"):
        print("MILA")
    elif bin(x).count("1") < bin(y).count("1"):
        print("TOMY")
    else:
        print("EMPATE")