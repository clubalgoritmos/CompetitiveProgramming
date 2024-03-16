# https://jv.umsa.bo/oj/problem.php?id=1012
#  Palindrome  Extendido
#  Enviar
#  Estado
#  Descripción
#    Un string palindrome, es un string que se lee igual cuando es invertida. Por ejemplo ORURO, ABBA son palindromes, pero ABB no lo es.
#    Un string palindrome, es un string que se lee igual cuando es invertida. Por ejemplo ORURO, ABBA son palindromes, pero ABB no lo es.
#    Un string palindrome, es un string que se lee igual cuando es invertida. Por ejemplo ORURO, ABBA son palindromes, pero ABB no lo es.
#    En este problema tú debes agregar caracteres a la derecha del string dada y convertirla en palindrome (Obviamente si ya es palindrome no es necesario hacer nada mas).
#    En este problema tú debes agregar caracteres a la derecha del string dada y convertirla en palindrome (Obviamente si ya es palindrome no es necesario hacer nada mas).
#    En este problema tú debes agregar caracteres a la derecha del string dada y convertirla en palindrome (Obviamente si ya es palindrome no es necesario hacer nada mas).
#   Entrada
#    Entrada terminara con el string END, cada línea tendrá un string no vacío de letras minúsculas. La longitud de la cadena será menor a 200000.
#    Entrada terminara con el string END, cada línea tendrá un string no vacío de letras minúsculas. La longitud de la cadena será menor a 200000.
#    Entrada terminara con el string END, cada línea tendrá un string no vacío de letras minúsculas. La longitud de la cadena será menor a 200000.
#    END
#   Salida
#    Para cada caso de prueba imprimir el palíndrome del string dado.
#    Para cada caso de prueba imprimir el palíndrome del string dado.
#    Para cada caso de prueba imprimir el palíndrome del string dado.
#   Ejemplo Entrada
#    aaaaabbaamanaplanacanalxyzEND
#   Ejemplo Salida
#    aaaaabbaamanaplanacanalpanamaxyzyx
#   Ayuda
#    2da div. 2012 UMSA
#    para no adicionar extra consderar que si existen palindromo en una subcadena descartando un o varios caracteres a la izquierda, luego de tener uno o no exista alguno ir añadiendo carcateres al final iguales a los q estan en el paralelo izquierdo

def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

while True:
    S = input()
    if S=="END":
        break
    if is_palindrome(S):
        print(S)
        continue
    for i in range(len(S)):
        if is_palindrome(S[i:]):
            print(S + S[:i][::-1])
            break