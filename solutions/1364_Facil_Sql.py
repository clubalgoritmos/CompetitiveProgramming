# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=69
## https://jv.umsa.bo/oj/problem.php?id=1364
#    Copiado al portapapeles
#  Facil Sql
#  Enviar
#  Estado
#  Descripción
#    SQL (Structured Query Language, Lenguaje Estructurado de Consulta) es un lenguaje hecho para manipular los datos contenidos dentro de una Base de Datos. Cada tabla en una Base de Datos tiene un DDL (Data Definition Language, Lenguaje de Definici\'on de Datos) y un DML (Data Management Language, Lenguaje de Manipulaci\'on de Datos).Para hacer la Manipulaci\'on de Datos m\'as f\'acil, queremos crear la sentencia $SELECT$, usando la Definici\'on de Datos de cada tabla, que usa la sentencia $CREATE \; TABLE$.Por ejemplo, tenemos la tabla:$CREATE \; TABLE \; table1 \; (field1 \; type1, \; field2 \; type2)$Y para obtener su contenido usamos:$SELECT \; field1, \; field2 \; FROM \; table1$Tu tarea es dada una sentencia $CREATE TABLE$, construir la sentencia $SELECT$.
#   Entrada
#    La entrada tiene varios casos de prueba. Cada l\'inea contiene una sentencia $CREATE \; TABLE$. El fin de la entrada es representada por un \#.
#   Salida
#    Para cada sentencia $CREATE \; TABLE$, imprimir la sentencia $SELECT$
#   Ejemplo Entrada
#    CREATE TABLE table1 (field1 type1, field2 type2)CREATE TABLE table2 (field3 type3, field4 type4, field5 type5, field6 type6)#
#   Ejemplo Salida
#    SELECT field1, field2 FROM table1SELECT field3, field4, field5, field6 FROM table2
#   Ayuda

