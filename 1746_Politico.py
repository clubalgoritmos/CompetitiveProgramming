# https://jv.umsa.bo/oj/problem.php?cid=2575&pid=4
## https://jv.umsa.bo/oj/problem.php?id=1746
#  Politico
#  Estado
#  Descripción
#    En un pais distante los jueces estan tratando de saber cuanto dinero han ganado en las elecciones por transferencias bancarias.Existen tres tipos de transacciones:1.- R nombre numero : Significa que el político recibió dinero de fuente desconocida2.- G nombre numero : Significa que un político regala un mondo de dinero3.- P nombre numero nombre : Significa que un político transfiere un monto de dinero a a otro políticoNombre se refiere al nombre del político, y número al monto de dinero.
#   Entrada
#    La entrada consiste de múltiple casos de prueba. Cada caso de prueba termina con la palabra END.En un caso de prueba las transacciones que puede llegar a $10^5$.
#   Salida
#    Escriba en la salida el nombre del político y su saldo. El listado estará en orden alfabético por nombre.
#   Ejemplo Entrada
#    R Smith 1000G Taylor 20000ENDP Taylor 20000 SmithENDP Blue 3 RedG Brown 100000R Blue 3R Orange 5000P White 1 BlondeR Pink 12345END
#   Ejemplo Salida
#    {Smith=1000, Taylor=-20000}{Smith=20000, Taylor=-20000}{Blonde=1, Blue=0, Brown=-100000, Orange=5000, Pink=12345, Red=3, White=-1}
#   Ayuda

def añadir(nombre, numero):
    if nombre in politicos:
        politicos[nombre] += numero
    else:
        politicos[nombre] = numero

def regalar(nombre, numero):
    if nombre in politicos:
        politicos[nombre] -= numero
    else:
        politicos[nombre] = -numero

def transfiere(nombre, numero, nombre2):
    if nombre in politicos:
        politicos[nombre] -= numero
    else:
        politicos[nombre] = -numero
    if nombre2 in politicos:
        politicos[nombre2] += numero
    else:
        politicos[nombre2] = numero

funcs = {
    "R": lambda nombre, numero: añadir(nombre,int(numero)), #Obtiene
    "G": lambda nombre, numero: regalar(nombre, int(numero)), #Regala
    "P": lambda nombre, numero, nombre2: transfiere(nombre, int(numero), nombre2) #Transfiere
}

while True:
    try:
        politicos=dict()
        while True:
            entry = tuple(input().split())
            if entry[0] == "END":
                break
            funcs[entry[0]](*entry[1:])
        print("{" + ", ".join(f"{k}={politicos[k]}" for k in sorted(politicos)) + "}")
    except:
        break