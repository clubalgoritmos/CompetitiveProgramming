# https://jv.umsa.bo/oj/problem.php?cid=2567&pid=1
#  CALCULADORA YUANFEN
#  Estado
#  Descripción
#    Yuanfen es un término chino difícil de entender para personas en otros países. En términos generales, YuanfenYuanfen es un término chino difícil de entender para personas en otros países. En términos generales, Yuanfen significa la "fuerza vinculante" predeterminada que une a dos personas (generalmente dos amantes). Aunque es una fe ciega, muchas personas, especialmente a las chicas les gusta calcularlo.
#    Yuanfen es un término chino difícil de entender para personas en otros países. En términos generales, Yuanfen
#    Yuanfen es un término chino difícil de entender para personas en otros países. En términos generales, Yuanfen significa la "fuerza vinculante" predeterminada que une a dos personas (generalmente dos amantes). Aunque es una fe ciega, muchas personas, especialmente a las chicas les gusta calcularlo.
#    Vamos a ayudar a todas las chicas, programando una Calculadora Yuanfen, por lo cual lo único que debemos hacer es encontrar un algoritmo que resuelva estos cálculos.
#    Vamos a ayudar a todas las chicas, programando una Calculadora Yuanfen, por lo cual lo único que debemos hacer es encontrar un algoritmo que resuelva estos cálculos.
#    Después de varias horas de análisis, encontramos el siguiente algoritmo:
#    Después de varias horas de análisis, encontramos el siguiente algoritmo:
#    Paso 1: Se empieza con las primeras letras de los nombres de ambas parejas y concatenarlas en una sola cadena. Por ejemplo, si la pareja tienen los siguientes nombres: Juan Yepez Farfan y Tatiana Yañez Romero, la cadena resultado sería: JYFTYR
#    Paso 1: Se empieza con las primeras letras de los nombres de ambas parejas y concatenarlas en una sola cadena. Por ejemplo, si la pareja tienen los siguientes nombres: Juan Yepez Farfan y Tatiana Yañez Romero, la cadena resultado sería: JYFTYR
#    Paso 2: Reemplaza cada letra con su respectivo valor numérico, de acuerdo a la siguiente tabla de equivalencias:significa la "fuerza vinculante" predeterminada que une a dos personas (generalmente dos amantes). Aunque es una fe ciega, muchas personas, especialmente a las chicas les gusta calcularlo.
#    Paso 2: Reemplaza cada letra con su respectivo valor numérico, de acuerdo a la siguiente tabla de equivalencias:significa la "fuerza vinculante" predeterminada que une a dos personas (generalmente dos amantes). Aunque es una fe ciega, muchas personas, especialmente a las chicas les gusta calcularlo.
#    Paso 2: Reemplaza cada letra con su respectivo valor numérico, de acuerdo a la siguiente tabla de equivalencias:
#    En el ejemplo, JYFTYR será reemplazado por la cadena: 10266212619
#    Paso 3: Repite el siguiente procedimiento: suma cada par de dígitos consecutivos y anota el último dígito de cada suma. Cada vez que realizamos esta operación, el número de dígitos es disminuido en 1. Cuando el resultado de este procedimiento llegue a 100 o a una cifra de dos dígitos, el proceso termina. El valor del resultado es el Yuanfen entre la pareja. Del ejemplo del paso 2, este sería el resultado:
#    Entonces, si el resultado final es 100, será una pareja FELIZ, y en otro caso, será una pareja INFELIZ.
#   Entrada
#    Hay una cadena de caracteres que representa a la abreviatura de los nombres de ambas parejas. La cadena tiene al menos 4 caracteres y como máximo 10 letras.
#   Salida
#    Se imprimirá el entero positivo resultado de la operación, un guión,
#    y el texto PAREJA FELIZ ó PAREJA INFELIZ.
#   Ejemplo Entrada
#    JYFTYR
#   Ejemplo Salida
#    68 - PAREJA INFELIZ
#   Ayuda

abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
a = list(map(int,''.join([str(abc.index(x)+1) for x in input()])))
n = int(''.join(map(str, a)))
while n>100:
    for i in range(1,len(a)):
        a[i-1] = (a[i-1]+a[i])%10
    a.pop(-1)
    n = int(''.join(map(str, a)))

if n==100:
    print(f"{n} - PAREJA FELIZ")
    exit()
print(f"{n} - PAREJA INFELIZ")