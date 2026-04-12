# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=81
## https://jv.umsa.bo/oj/problem.php?id=1409
#    Copiado al portapapeles
#  Sorteos Bancarios
#  Enviar
#  Estado
#  Descripción
#    Muchos bancos locales han comenzado un sistema de sorteos en lugar de pagar intereses en la forma tradicional. Es más barato y mucha gente no ve la diferencia. El sistema de sorteos funciona como sigue:Al final de cada semana se realiza un sorteo. Cada cliente que posee una cuenta recibe un cupón por cada peso en su saldo de cuenta. Después que se han distribuido todos los cupones, se escoge un cupón al azar. Cada cupón tiene la misma probabilidad de salir escogido. El poseedor del cupón gana un premio que es inmediatamente adicionado a su cuenta.Usted acaba de abrir una cuenta en el banco y desea conocer su saldo esperado al momento, en el futuro. Usted curiosamente ha podido conocer los saldos de todos los clientes del banco. Estos balances son dados como un vector siendo el primer elemento su saldo.Para este problema tomen en cuenta que no hay transacciones adicionales al sorteo semanal. Tampoco se crean o cierran cuentas.Conocedor de sus conocimientos de programación le han pedido calcular su saldo esperado después de un número dado de semanas.Veamos un ejemplo:Supongamos que hay tres clientes cada uno con $2$ pesos de saldos, es decir, usted también tiene $2$ pesos. El premio asignado es de $1$ peso.Cuál es su saldo probable después de la segunda semana?Considere para la solución que la probabilidad de que los balances en la primera semana queden ${3,2,2}$ es de $1/3$.La probabilidad de que queden ${2,3,2}$ esta también de $1/3$ probabilidad y que se conviertan en ${2,2,3}$ es $1/3$. Esto nos da un saldo esperado es de $2.6666666666666665$.
#   Entrada
#    La entrada consiste en múltiples casos de prueba que terminan cuando no hay más datos.
#    La primera línea contiene un número entero ($1\leq n \leq 50$) que representa el número de cuentas.
#    La segunda línea contiene $n$ números enteros con el saldo de las cuentas. El primer valor representa su saldo. Por lo menos un saldo es mayor a cero.
#    La tercera línea contiene un entero entre $1$ y $1000$ inclusive que indica el monto del premio.
#    La cuarta línea contiene un entero entre $1$ y $1000$ inclusive que indica el número de semanasLa entrada termina cuando no hay más datos.
#   Salida
#    La salida consiste de una sola línea que contiene el saldo esperado. El resultado debe imprimirse con error menor a $1e-9$. Si no tiene dinero no puede ganar y la respuesta deberá ser "0.0".
#   Ejemplo Entrada
#    2100 100100232 2 212101 2 3 4 5 6 7 8 9 1010020    70 200 200 0 300 300 6003776
#   Ejemplo Salida
#    200.02.666666666666666537.363636363636370.0
#   Ayuda

