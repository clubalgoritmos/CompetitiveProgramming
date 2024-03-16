import os
import re
import lib

# Obtén el directorio actual
dir_path = "C:\\Users\\Andres\\Proyectos\\PyCompetitiveProgramming"
par = lib.Parser(path=dir_path)

# Obtén una lista de todos los archivos en el directorio
files = os.listdir(dir_path)

# Extrae los números de los nombres de los archivos
problem_numbers = [int(re.search(r'\d{0,4}', file).group()) for file in files if re.search(r'\d+', file)]

for problem in problem_numbers:
    print(par.create_Problem(f"https://jv.umsa.bo/oj/problem.php?id={problem}"))