import requests, re, os
from bs4 import BeautifulSoup
from urllib.parse import parse_qs, urlparse
from bs4 import BeautifulSoup
import shutil
class Parser:
    def __init__(self,path:str=os.getcwd()):
        self.path = path
        self.valores = {
            "h2": 1,
            "h3": 2,
            "span": 3,
            "p": 3,
            "pre": 3,
            "a": 1
        }
        self.base_url = "https://jv.umsa.bo/oj/"
        pass

    # Función para obtener el texto de un elemento
    def get_attrs(self, element):
        attrs = element.attrs
        attrs["text"] = "".join(ch for ch in element.get_text().strip() if ch.isprintable())
        attrs["name"] = element.name
        return attrs

    def get_content(self,url:str):
        # Realizar la solicitud HTTP
        response = requests.get(url)

        # Analizar el HTML con BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        return soup

    def list_contest(self):
        for i in range(2815,1000,-1):
            try:
                soup = self.get_content(self.base_url+f"contest.php?cid={i}")
                print(soup.select("main h2")[0].text)
            except:
                pass


        

    def get_from_table(self,url:str):
        soup = self.get_content(url)

        # Seleccionar la primera tabla
        table = soup.select("main table")[0]

        # Obtener las filas de la tabla
        rows = table.select("tbody tr")

        # Obtener el texto de las filas
        rows = list(map(lambda row: row.select("td a")[0], rows))
        # Obtener el texto de las filas
        elements = list(map(self.get_attrs, rows))

        for element in elements:
            print(self.create_Problem(self.base_url+element["href"]))

    def create_Problem(self,url:str):
        # Realizar la solicitud HTTP
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        # Seleccionar todos los elementos a la vez
        elements = soup.select("main h2, main h3, main a, main span, main p, main pre")

        # Obtener el texto de los elementos
        elements = list(map(self.get_attrs, elements))
        
        def search_send():
            for element in elements:
                if element["text"]=="Estado":
                    return self.base_url+element["href"]
            return self.base_url

        # Parsear la URL para obtener el argumento 'id'
        params_url = parse_qs(urlparse(url).query)
        params_statusurl = parse_qs(urlparse(search_send()).query)
        id = params_url.get("id", [None])[0] or params_statusurl.get("id", [None])[0] or params_url.get("cid", [None])[0]+"-"+params_url.get("pid", [None])[0]

        # Ruta del archivo
        file_path = os.path.join(
            self.path,
            re.sub(r'[\\/:*?"<>|]', "", f"{id}_{elements[0]["text"]}").replace(" ", "_") + ".py",
        )
        
        # Verificar si el archivo ya existe
        if os.path.exists(file_path):
            return "ya resuelto"

        # Obtener el valor de la clave 'text' de cada diccionario
        elements_text = [f"{' '*self.valores[el['name']]} {el['text']}" for el in elements if el['text']!=""]

        # Crear el archivo
        with open(file_path, "w", encoding='utf-8') as file:  # Abrir el archivo en modo de escritura
            file.write(f"# {url}\n#")
            file.write("\n#".join(elements_text))
            file.write("\n\n")

        exist_legacy = os.path.join(self.path, f"{id}.py")
        if os.path.exists(exist_legacy):
            with open(exist_legacy, "r") as legacy_file:
                with open(file_path, "a") as new_file:  # Abrir el archivo en modo de agregar
                    new_file.write(legacy_file.read())
            os.remove(exist_legacy)  # Borrar el archivo de donde se ha copiado

        # Imprimir la ruta del archivo
        return file_path