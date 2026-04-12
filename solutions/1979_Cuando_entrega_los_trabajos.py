# https://jv.umsa.bo/oj/problem.php?id=1979
#  Cuando entrega los trabajos
#  Enviar
#  Estado
#  Descripción
#    En la fabrica donde trabajas existen una cantidad de maquinas para realizar los trabajos de la empresa. Como cada maquina se compro en diferente años, cada maquina demora un tiempo diferente en realizar el trabajo.Por ejemplo si tenemos tres equipos y el tiempo de proceso que toma cada uno es p=[2,3,7]. Podemos preguntar cual es el mínimo tiempo para realizar 8 trabajos. La solución se halla sumando el numero de trabajos que puede hacer cada maquina, esto es 8/2=4,8/3=2,8/7=1 y la suma es 7. Si tomo 9, tenemos 9/2=4,9/3=3,9/7=1 sumando 9.El tiempo mínimo para procesar 8 trabajos es 9.
#   Entrada
#    La primera línea contiene n, el numero de maquinas ($2 \leq n \leq 100$).La segunda contiene valores n tiempos de proceso correspondientes a cada una de las maquinas donde cada uno menor a 100.La tercera linea contiene el numero consultas ($1 \leq c \leq 1000$).Luego siguen $c$ consultas, cada una en una linea.Cada consulta es un numero ($2 \leq k \leq 10000$) que representa el numero de trabajos que se quieren procesar.
#   Salida
#    Por cada consulta imprima el tiempo mínimo para procesar los trabajos.
#   Ejemplo Entrada
#    32 3 748679
#   Ejemplo Salida
#    Tiempo minimo para 8 trabajos es: 9Tiempo minimo para 6 trabajos es: 7Tiempo minimo para 7 trabajos es: 8Tiempo minimo para 9 trabajos es: 10
#   Ayuda

def min_time_to_complete_jobs(n, process_times, queries):
    def jobs_completed_in_time(t):
        return sum(t // p for p in process_times)
    
    results = []
    for k in queries:
        low, high = 1, max(process_times) * k
        while low < high:
            mid = (low + high) // 2
            if jobs_completed_in_time(mid) >= k:
                high = mid
            else:
                low = mid + 1
        results.append(low)
    return results

# Leer la entrada
n = int(input())
process_times = list(map(int, input().split()))
c = int(input())
queries = [int(input()) for _ in range(c)]

# Obtener los resultados
results = min_time_to_complete_jobs(n, process_times, queries)

# Imprimir los resultados
for k, result in zip(queries, results):
    print(f"Tiempo minimo para {k} trabajos es: {result}")