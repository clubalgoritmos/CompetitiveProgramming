# https://jv.umsa.bo/oj/problem.php?id=1723
#  Casi Igual
#  Enviar
#  Estado
#  Descripción
#    Juan ha decidido ir al oculista porque va ha renovar su licencia de conducir. Para examinar la visión de Juan el oculista ha escrito un número en una pizarra que le pide que lea. Juan puede determinar correctamente la cantidad de dígitos, sin embargo no ve del todo bien, por lo que no puede identificar los dígitos individualmente. Finalmente cuando lee el numero el doctor sale por un breve momento.Como no quiere una receta de lentes inmediatamente que sale el doctor corre a la pizarra para cambiar el número con la finalidad que iguale al que leyó. El tiempo solo le da para cambiar un solo dígito del número.Dados dios números A y B usted debe escribir la palabra feliz si A difiere de B en un solo dígito o lentes, en otro caso.
#   Entrada
#    La entrada consiste de múltiples casos de prueba y termina cuando no hay más datos.Cada cada caso de prueba consiste de los números A y B ambos menores a 999,999. Los dos tienen la misma cantidad de dígitos.
#   Salida
#    Escriba una linea por cada caso de entrada con la palabra feliz o lentes como se muestra en el ejemplo
#   Ejemplo Entrada
#    8072 3072508 540854000 8540001 6385900 123000
#   Ejemplo Salida
#    felizlentesfelizfelizlentes
#   Ayuda

#casi igual
import sys

if __name__ == '__main__':
    for i in sys.stdin:
        a, b = i.split()
        cont = 0
        for j in range(len(a)):
            if a[j] != b[j]:
                cont += 1
                if cont > 1:
                    break
        if cont <= 1:
            print('feliz')
        else:
            print('lentes')