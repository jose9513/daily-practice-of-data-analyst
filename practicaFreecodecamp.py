"""#Uso de apis
import requests
import json

lat = -24.6
long = -58.4
fecha = "2024-06-01"

respuesta_sunset = requests.get(f"https://api.sunrise-sunset.org/json?lat={lat}&lng={long}&date={fecha}")

datos_sunset = respuesta_sunset.json()
datos_sunset

sunset_status = datos_sunset["status"]
print(f"Estado de la respuesta: {sunset_status}")

sunset = datos_sunset["results"]["sunset"]
print(f"El {fecha} el sol se puso a las {sunset} UTC")

print("iterando por cada elemento del result")
for key, value in datos_sunset["results"].items():
    print(f"{key}: {value}")"""
    
"""import wikipediaapi
#instanciamos la clase wikipediaapi y utilizamos el metodo wikipedia con el parameto de idioma
IDIOMA = "es"
wiki_wiki = wikipediaapi.Wikipedia(IDIOMA)

#utilizamos el metodo page y hacemos un pedido con la palabra clave
PALABRA_CLAVE = "programación"
wikipedia_programacion = wiki_wiki.page(PALABRA_CLAVE)

#resumen
print(f"wikipedia_programacion es un objeto de tipo: {type(wikipedia_programacion)}")
print(wikipedia_programacion.title)
print(" ")
print(wikipedia_programacion.summary)

#url completa
print(wikipedia_programacion.fullurl)
"""

"""
from bs4 import BeautifulSoup
import requests
#obtener el HTML de la página
URL_BASE = "https://scrapepark.org/spanish/"
pedido_obtenido = requests.get(URL_BASE)
html_obtenido = pedido_obtenido.text

#parsear el HTML con BeautifulSoup
soup = BeautifulSoup(html_obtenido, 'html.parser')

primer_h2 = soup.find('h2')
print(f"El primer h2 encontrado es: {primer_h2.text}")

todos_los_h2 = soup.find_all('h2')
for h2 in todos_los_h2:
    print(h2.get_text(strip=True))

#print(todos_los_h2)"""

"""
from bs4 import BeautifulSoup
import requests
#obtener el HTML de la página
URL_BASE = "https://scrapepark.org/spanish/"
pedido_obtenido = requests.get(URL_BASE)
html_obtenido = pedido_obtenido.text

soup = BeautifulSoup(html_obtenido, 'html.parser')

divs = soup.find_all('div', class_='heading-container heading-center')

for div in divs:
    print(div)
    print("-------------")"""
    
    
"""    
from bs4 import BeautifulSoup
import requests
#obtener el HTML de la página
URL_BASE = "https://scrapepark.org/spanish/"
pedido_obtenido = requests.get(URL_BASE)
html_obtenido = pedido_obtenido.text

soup = BeautifulSoup(html_obtenido, 'html.parser')

imgs = soup.find_all(src=True)

for img in imgs:
    if img['src'].endswith('.jpg') or img['src'].endswith('.png'):
        print(img)
        """
        
        
"""    
from bs4 import BeautifulSoup
import requests
#obtener el HTML de la página
URL_BASE = "https://scrapepark.org/spanish/"
pedido_obtenido = requests.get(URL_BASE)
html_obtenido = pedido_obtenido.text

soup = BeautifulSoup(html_obtenido, 'html.parser')

src_todos = soup.find_all(src=True)

url_imagenes = []
for i, imagen in enumerate(src_todos):
    if imagen['src'].endswith('.png'):
        print(imagen['src'])
        r = requests.get(f"https://scrapepark.org/spanish/{imagen['src']}")
        
        with open(f"imagen_{i}.png", 'wb') as f:
            f.write(r.content)"""
            
            
"""            
#INFORMACION DE TABLAS
from bs4 import BeautifulSoup
import requests
#obtener el HTML de la página
URL_BASE = "https://scrapepark.org/spanish/"

pedido_obtenido = requests.get(URL_BASE)
html_obtenido = pedido_obtenido.text
soup = BeautifulSoup(html_obtenido, 'html.parser')

URL_TABLA = soup.find_all('iframe')[0]['src']

requests_tabla = requests.get(f"{URL_BASE}/{URL_TABLA}")

html_tabla = requests_tabla.text
soup_tabla = BeautifulSoup(html_tabla, 'html.parser')
soup_tabla.find('table')

productos_faltantes = soup_tabla.find_all(['tr', 'td'], attrs={'style': 'color: red;'})
productos_faltantes = [talle.text for talle in productos_faltantes]
print(productos_faltantes)
"""


"""
from bs4 import BeautifulSoup
import requests
#obtener el HTML de la página
URL_BASE = "https://scrapepark.org/spanish/"

pedido_obtenido = requests.get(URL_BASE)
html_obtenido = pedido_obtenido.text
soup = BeautifulSoup(html_obtenido, 'html.parser')

divs = soup.find_all('div', class_='detail-box')
productos = []
precios = []

for div in divs :
    if(div.h6 is not None) and ('Patineta' in div.h5.text):
        producto = div.h5.get_text(strip=True)
        precio = div.h6.get_text(strip=True).replace('$', '')
        #se pueden agregar filtros
        print(f"producto: {producto:<16} | precio: {precio}")
        productos.append(producto)
        precios.append(precio)
        """
        
        
"""
from bs4 import BeautifulSoup
import requests
#obtener el HTML de la página
URL_BASE = "https://scrapepark.org/spanish/contact"


for i in range (1,3):
    URL_FINAL = f"{URL_BASE}{i}"
    print(f"URL final: {URL_FINAL}")
    r = requests.get(URL_FINAL)
    soup = BeautifulSoup(r.text, 'html.parser')
    print(soup.h5.text)
    """
    
    
"""    
from bs4 import BeautifulSoup
import requests
#expreciones regulares
import re
#obtener el HTML de la página
URL_BASE = "https://scrapepark.org/spanish/"

pedido_obtenido = requests.get(URL_BASE)
html_obtenido = pedido_obtenido.text
#parsear el HTML con BeautifulSoup
soup = BeautifulSoup(html_obtenido, 'html.parser')

telefonos = soup.find_all(string=re.compile('\d+-\d+-\d+'))
print(telefonos)

#averiguamos si tiene copyright
copyrights = soup.find_all(string=re.compile('©'))
print(copyrights[0])

primer_copyright = copyrights[0]
print(primer_copyright.parent)
"""



from bs4 import BeautifulSoup
import requests
#expreciones regulares
import re
#obtener el HTML de la página
URL_BASE = "https://scrapepark.org/spanish/"

pedido_obtenido = requests.get(URL_BASE)
html_obtenido = pedido_obtenido.text
#parsear el HTML con BeautifulSoup
soup = BeautifulSoup(html_obtenido, 'html.parser')

strings_a_buscar = ["MENÚ", "©", "carpincho", "patineta"]

for string in strings_a_buscar:
    try:
        resultado = soup.find(string=re.compile(string))
        print(f"Resultado para '{string}': {resultado.text}")
    except AttributeError:
        print(f"No se encontró el string '{string}' en el HTML.")