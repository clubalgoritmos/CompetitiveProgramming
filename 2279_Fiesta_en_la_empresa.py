# https://jv.umsa.bo/oj/problem.php?cid=2826&pid=25
## https://jv.umsa.bo/oj/problem.php?id=2279
#  Fiesta en la empresa
#  Enviar
#  Estado
#  Descripción
#    Una empresa tiene $n$ empleados numerados de $1$ a $n$. Cada empleado no tiene un gerente inmediato o exactamente un gerente inmediato, que es otro empleado con un número diferente. Se dice que un empleado $A$ es superior a otro empleado $B$ si al menos uno de los siguientes es verdadero:
#    El empleado $A$ es el gerente inmediato del empleado $B$
#    El empleado $B$ tiene un empleado $C$ de gerente inmediato, de modo que el empleado $A$ es superior al empleado $C$.
#    La empresa no tendrá un ciclo gerencial. Es decir, no existirá un empleado que sea superior a su propio gerente inmediato.
#    Hoy la empresa va a organizar una fiesta. Esto implica dividir todos los $n$ empleados en varios grupos: cada empleado debe pertenecer exactamente a un grupo. Además, dentro de un solo grupo, no debe haber dos empleados $A$ y $B$ de manera que $A$ sea superior a $B$.
#    ¿Cuál es el número mínimo de grupos que se deben formar?
#   Entrada
#    La primera línea contiene el número entero $n$ ($1 \leq n \leq 2000$) - el número de empleados.
#    Las siguientes $n$ líneas contienen los números enteros $p_{i}$ ($1 \leq p_{i} \leq n$ o $p_{i} = -1$). Cada $p_{i}$ denota el gerente inmediato del $i$-ésimo empleado. Si $p_{i}$ es $-1$, eso significa que el i-ésimo empleado no tiene un gerente inmediato.
#    Se garantiza que ningún empleado será el gerente inmediato de sí mismo ($p_{i} \neq i$). Además, no habrá ciclos gerencial.
#   Salida
#    Imprime un solo entero que denota el número mínimo de grupos que se formarán en la fiesta.
#   Ejemplo Entrada
#    5-1121-1
#   Ejemplo Salida
#    3
#   Ayuda
#    Para el primer ejemplo, tres grupos son suficientes, por ejemplo:
#    Empleado 1
#    Empleados 2 y 4
#    Empleados 3 y 5

