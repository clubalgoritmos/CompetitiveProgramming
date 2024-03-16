import os
import re
import lib
import concurrent.futures

# Obtén el directorio actual
dir_path = "C:\\Users\\Andres\\Proyectos\\PyCompetitiveProgramming"
par = lib.Parser(path=dir_path)

# Obtén una lista de todos los archivos en el directorio
files = os.listdir(dir_path)

# Extrae los números de los nombres de los archivos
problem_numbers = [1090,1000,2568,2567,2572,2566]

# Define una función que será ejecutada en paralelo
def process_problem(problem):
    return par.create_Problem(f"https://jv.umsa.bo/oj/problem.php?id={problem}")

# Crea un pool de trabajadores y ejecuta las tareas en paralelo
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = list(executor.map(process_problem, problem_numbers))

# Imprime los resultados
for result in results:
    print(result)