# https://jv.umsa.bo/oj/problem.php?id=1019
#  Reduciendo Costos
#  Enviar
#  Estado
#  Descripción
#    La compañía XYZ se ha visto muy afectada por la recesión y está tomando una gran cantidad de medidas de reducción de costos. Algunas de estas medidas incluyen renunciar a espacios de oficinas, utilizar código abierto, reducir los incentivos, recortar los lujos y emitir cartas de despido.
#    Tienen tres (3) empleados que trabajan en el departamento de contabilidad y se va a despedir a dos (2) de ellos. Tras una serie de reuniones, han decidido despedir a la persona que percibe el mayor salario y también a la persona que percibe el menor salario. Esta suele ser la tendencia general durante crisis como esta. Le proporcionarán a Ud. los salarios de los 3 empleados que trabajan en el departamento de contabilidad. Usted tiene que encontrar el sueldo de la persona que se queda.
#   Entrada
#    La primera línea de entrada es un número entero T (T<20) que indica el número de casos de prueba. Cada caso consiste de una línea con 3 números enteros positivos distintos. Estos 3 enteros representan los sueldos de los tres empleados. Estos tres números enteros están en el rango [1000, 40000].
#   Salida
#    Para cada caso, obtenga el número del caso seguido del salario de la persona que se queda.
#   Ejemplo Entrada
#    31000 2000 30003000 2500 15001500 1200 1800
#   Ejemplo Salida
#    Case 1: 2000Case 2: 2500Case 3: 1500
#   Ayuda

t = int(input())
for i in range(1,t+1):
    a,b,c = sorted(map(int, input().split()))
    print(f"Case {i}: {b}")