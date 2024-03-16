# https://jv.umsa.bo/oj/problem.php?id=1295
#  Cifrado
#  Enviar
#  Estado
#  Descripción
#    Dadas la tabla de traducción y el texto cifrado con esta  tabla, recuperar el texto original. La tabla para decodificar consiste  en 26 caracteres donde el primero corresponde a la letra a y el ultimo a  la z.
#    Dadas la tabla de traducción y el texto cifrado con esta  tabla, recuperar el texto original. La tabla para decodificar consiste  en 26 caracteres donde el primero corresponde a la letra a y el ultimo a  la z.
#    Dadas la tabla de traducción y el texto cifrado con esta  tabla, recuperar el texto original. La tabla para decodificar consiste  en 26 caracteres donde el primero corresponde a la letra a y el ultimo a  la z.
#   Entrada
#    La entrada consiste de múltiples casos de prueba. Cada caso de prueba viene en multiples lineas.La primera linea es la tabla de traducción. Luego viene una linea con el numero de lineas de texto. Las siguientes linea son el texto a descifrar.Los espacios están sin codificar.
#    La entrada consiste de múltiples casos de prueba. Cada caso de prueba viene en multiples lineas.La primera linea es la tabla de traducción. Luego viene una linea con el numero de lineas de texto. Las siguientes linea son el texto a descifrar.Los espacios están sin codificar.
#    La entrada consiste de múltiples casos de prueba. Cada caso de prueba viene en multiples lineas.La primera linea es la tabla de traducción. Luego viene una linea con el numero de lineas de texto. Las siguientes linea son el texto a descifrar.Los espacios están sin codificar.
#   Salida
#    En la salida escriba el texto descifrado. Imprima una linea en blanco despues de cada caso de prueba.
#    En la salida escriba el texto descifrado. Imprima una linea en blanco despues de cada caso de prueba.
#    En la salida escriba el texto descifrado. Imprima una linea en blanco despues de cada caso de prueba.
#   Ejemplo Entrada
#    52-!813467/09*+.[();?']<:>796 !8)8).8(5-6+* )8 5?98*;5 50 -+*;89.05( 056*98*)6!5! !8 '?8);(+ .(896+ .+([?8!8).?8) !8 4528( 53+;5!+ 0+) ;508*;+) 05) '6(;?!8) 80 38*6+ 96)9+ !80 95) 3(5*!8 !8 0+) 48(+8) ;+!5'65 )8(65 :+ 6*!63*+ !898(8-8( 80 *+92(8 bcdefghijklmnopqrstuvwxyza3cfxbsf pg cvht jo uif bcpwf dpefj ibwf pomz qspwfe ju dpssfduopu usjfe ju
#   Ejemplo Salida
#    mi desesperacion se aumenta al contemplar lainmensidad de vuestro premio porquedespues de haber agotado los talentoslas virtudes el geniomismo del mas grande de losheroes todavia seria yo indigno demerecer el nombrebeware of bugs in the above codei have only proved it correctnot tried it
#   Ayuda
#    guarde los datos de los caracteres en un vector

"""problema de cifrado"""
import sys
dic = "abcdefghijklmnopqrstuvwxyz" 		#aqui tendremos la referencia para el alfabeto
if __name__ == "__main__":
	for cod in sys.stdin:				#leemos el diccionario
		n = int(input())				#la cantidad de frases a traducir
		for i in range(0, n):
			trad = ""					#para la traduccion
			cad = input()
			for letra in cad:			#vamos caracter por caracter
				if letra != " ":
					trad += dic[cod.index(letra)]
				else:
					trad += " "
			print(trad)					#tenemos la linea traducida
		print("")						#el salto de linea que se pide