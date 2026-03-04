"""----------------------- PRACTICA PROPIA ------------------"""
"""
import requests
from bs4 import BeautifulSoup

URL_BASE = "https://lionluxury.com.pe/collections/cadenas-de-acero-316l"
html_obtenido = requests.get(URL_BASE).text
res = requests.get(URL_BASE)
soup = BeautifulSoup(html_obtenido, 'html.parser')

productos_joyas = []

items_web = soup.find_all('li', class_='grid__item')

for items in items_web:
    tag_nombre = items.find('span', class_= 'card__heading__product-title')
    tag_precio = items.find('span', class_= 'price-item price-item--regular')
    
    if tag_nombre and tag_precio:
        nombre_sucio = tag_nombre.get_text(strip=True)

        if 'Acero 316L' in nombre_sucio:
            producto = {
                'nombre': nombre_sucio,
                'precio': tag_precio.get_text(strip=True)
            }
            productos_joyas.append(producto)
            
from pprint import pprint
print(f"se encontraros {len(productos_joyas)} productos: ")
pprint(productos_joyas)
"""

"""----------------------- PRACTICA PROPIA ------------------"""

"""
from bs4 import BeautifulSoup
import requests

url = "https://webscraper.io/test-sites/e-commerce/allinone"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

Titulo_unico = soup.find('a', class_='title')
print(f"el tipo de dato es: {type(Titulo_unico)}")
print(Titulo_unico.get_text(strip=True))

Titulos_todos = soup.find_all('a', class_='title')
print(f"el tipo de dato es: {type(Titulos_todos)}")
"""

"""----------------------- EJEMPLO CON GEMINI ------------------"""

"""
from bs4 import BeautifulSoup

# HTML Simulado (Imagina que esto bajó de una web)
#poner triple comillas para el codigo HTML
html_joyeria = 
<html>
    <body>
        <div id="sidebar">
            <span class="precio">S/ 15.00 (Costo de Envío)</span>
        </div>

        <div class="contenedor-joyas">
            <article class="joya-card">
                <h3>Anillo Fuego</h3>
                <span class="precio">S/ 500</span>
            </article>
            <article class="joya-card">
                <h3>Anillo Agua</h3>
                <span class="precio">S/ 350</span>
            </article>
        </div>
    </body>
</html>


soup = BeautifulSoup(html_joyeria, 'html.parser')

print("--- INTENTO 1: Búsqueda Ingenua (Nivel 0) ---")
# Si buscamos todos los precios a lo loco...
#todos_los_precios = soup.find_all('span', class_='precio')
#print(f"Encontré {len(todos_los_precios)} precios (¡Incluye el envío! ❌)")
#for p in todos_los_precios:
#    print(p.text)

print("\n--- INTENTO 2: Búsqueda Jerárquica (Nivel 2) ---")

# PASO 1: Encontramos el CONTENEDOR PADRE que envuelve solo a las joyas
# Pista: Mira el HTML, ¿qué clase envuelve a los articles?
contenedor_padre = soup.find('div', class_='contenedor-joyas') 

# PASO 2: Buscamos las tarjetas SOLO dentro de ese contenedor
# Nota: Usamos contenedor_padre.find_all, NO soup.find_all
tarjetas_joyas = contenedor_padre.find_all('article', class_='joya-card')

print(f"Encontré {len(tarjetas_joyas)} joyas reales. ✅")

# PASO 3: Iteramos y extraemos
for card in tarjetas_joyas:
    # Buscamos el precio DENTRO de la card
    nombre = card.find('h3').text
    precio = card.find('span', class_='precio').text
    print(f"Joya: {nombre} | Precio: {precio}")
    """

"""----------------------- EJEMPLO CON GEMINI ------------------"""

"""
from bs4 import BeautifulSoup

html_tienda = 
<div class="tienda">
    <div class="producto"> <h3>iPhone 15</h3> <span class="precio">$999</span> </div>
    <div class="producto"> <h3>Samsung S24</h3> <span class="precio">$899</span> </div>
    <div class="producto"> <h3>Pixel 8</h3> <span class="precio">$799</span> </div>
</div>

soup = BeautifulSoup(html_tienda, 'html.parser')

# 1. Obtenemos la lista de las 3 tarjetas
tarjetas = soup.find_all('div', class_='producto')

print(f"Tengo {len(tarjetas)} tarjetas para procesar.")

# 2. El Bucle (Aquí está el error)
for card in tarjetas:
    # ERROR: Estamos buscando en 'soup' (toda la web) en vez de en 'card'
    titulo = card.find('h3').text 
    precio = card.find('span', class_='precio').text
    
    print(f"Producto: {titulo} | Precio: {precio}")
"""

"""----------------------- EMEPLO CON GEMINI ------------------"""

"""
precio_sucio = "\n  S/. 3.500,00  \n"

paso1 = precio_sucio.strip() # Elimina espacios al inicio y al final
paso2 = paso1.replace('S/.', '') # Elimina el símbolo de moneda
paso3 = paso2.replace('.', '') # Elimina el punto de miles
paso4 = paso3.split(',')[0] # Toma solo la parte entera, eliminando los decimales

precio_final = int(paso4) # Convierte a entero

print(f"✅ Precio Final (Numérico): {precio_final}")
print(f"💰 Si vendemos 2, ganamos: {precio_final * 2}")
"""

"""----------------------- EJEMPLO CON GEMINI ------------------"""

"""
import requests
from bs4 import BeautifulSoup
import time # Importante para no ser bloqueado

# 1. Configuración
URL_BASE = "http://books.toscrape.com/catalogue/page-{}.html"
catalogo_total = []

# 2. El Bucle de Navegación (Del 1 al 3)
for numero_pagina in range(1, 4):
    
    # Generamos la URL dinámica (page-1.html, page-2.html...)
    url_actual = URL_BASE.format(numero_pagina)
    print(f"🕵️ Escaneando Página {numero_pagina}: {url_actual}")
    
    # Petición
    response = requests.get(url_actual)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 3. Extracción (Nivel 2 + 3)
    libros = soup.find_all('article', class_='product_pod')
    
    for libro in libros:
        # Título (A veces está en el atributo title del enlace)
        titulo = libro.find('h3').find('a')['title']
        
        # Precio Sucio (£51.77)
        precio_sucio = libro.find('p', class_='price_color').text
        
        # Limpieza (Nivel 4) - Quitamos el símbolo de libra £
        precio_limpio = float(precio_sucio.replace('£', ''))
        
        catalogo_total.append({
            "titulo": titulo,
            "precio": precio_limpio
        })
    
    # 4. Pausa de Cortesía (Ética Hacker)
    # Esperamos 1 segundo entre páginas para no tumbar el servidor
    time.sleep(1)

# --- REPORTE FINAL ---
print(f"\n✅ Misión Cumplida.")
print(f"📚 Total de libros capturados: {len(catalogo_total)}")
print("Muestra de los primeros 5:")

from pprint import pprint
pprint(catalogo_total[:5])

# 1. Importamos la librería (hazlo al inicio del archivo, pero aquí funciona igual)
import pandas as pd

# ... (Aquí termina tu bucle for y tienes la lista 'catalogo_total') ...

print("💾 Guardando archivo...")

# 2. Convertimos la lista de diccionarios en una "Tabla Inteligente" (DataFrame)
df = pd.DataFrame(catalogo_total)

# 3. Guardamos como CSV (Es el formato que Excel abre más rápido y pesa menos)
# encoding='utf-8-sig' es VITAL para que las tildes y la 'ñ' se vean bien en Excel
df.to_csv('Reporte_Libros_Artemisa.csv', index=False, encoding='utf-8-sig')

print(f"✅ ¡Éxito! Archivo guardado: 'Reporte_Libros_Artemisa.csv'")
"""

"""----------------------- PRACTICA PROPIA ------------------"""

"""
import requests
from bs4 import BeautifulSoup

def limpiar_precio(precio_inicio):
    # Elimina espacios, símbolos y convierte a número
    solo_numeros = "".join(caracter for caracter in precio_inicio if caracter.isdigit() or caracter == ".")
    
    return float(solo_numeros)

url_base = "https://books.toscrape.com/"
html_obtenido = requests.get(url_base).text
res = requests.get(url_base)
res.encoding = 'utf-8'
soup = BeautifulSoup(html_obtenido, 'html.parser')

padre = soup.find_all('article', class_='product_pod')

cinco_primeros = padre[:5]

for libro in cinco_primeros:
    titulo = libro.find('h3').find('a')['title']
    precio_sucio = libro.find('p', class_='price_color').text
    precio_limpio = limpiar_precio(precio_sucio)
    
    print(f"Libro: {titulo} | Precio: {precio_limpio}")
"""

"""----------------------- PRACTICA PROPIA ------------------"""

"""
import requests
from bs4 import BeautifulSoup

URL_BASE = "https://books.toscrape.com/"
res = requests.get(URL_BASE)
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')

padre = soup.find('ul', class_='nav-list').find('li').find('ul').find_all('li')

for nombre in padre:
    print(nombre.text.strip())
"""

"""----------------------- PRACTICA PROPIA ------------------"""

"""
import requests
from bs4 import BeautifulSoup

URL_BASE = "https://books.toscrape.com/"
res = requests.get(URL_BASE)
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')

obj = soup.find('img', class_='thumbnail')
print(f"{URL_BASE}{obj['src']}")
"""

"""----------------------- PRACTICA PROPIA ------------------"""

"""
import requests
from bs4 import BeautifulSoup

URL_BASE = "https://books.toscrape.com/"
res = requests.get(URL_BASE)
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')

todas_etiquetas_a =[a['href'] for a in soup.find_all('a', href=True)]
print(f"Encontré {len(todas_etiquetas_a)} enlaces en la página.")
"""



"""
import requests
from bs4 import BeautifulSoup

#obtenemos el HTML de la página
URL_BASE = "https://books.toscrape.com/"
res = requests.get(URL_BASE)
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')

#funcion para limpiar los caracteres innecesarios del precio
def limpiar_precio(precio_inicio):
    # Elimina espacios, símbolos y convierte a número
    solo_numeros = "".join(caracter for caracter in precio_inicio if caracter.isdigit() or caracter == ".")
    
    return float(solo_numeros)

#buscamos el contenedor padre de los libros
contenedor_libros = soup.find_all('article', class_='product_pod')

#diccionario que contendra los primeros 10 libros con su precio limpio
primeros_10_libros = {}

#iteramos sobre los primeros 10 libros encontrados
for libro in contenedor_libros[:10]:
    # Extraemos el título y precio de CADA libro (usando la variable 'libro')
    titulo = libro.find('h3').find('a')['title']
    precio_sucio = libro.find('p', class_='price_color').text
    precio_limpio = limpiar_precio(precio_sucio)
    primeros_10_libros[titulo] = precio_limpio

# REPORTE FINAL
print("Los primeros 10 libros son:")
for titulo, precio in primeros_10_libros.items():
    print(f"Libro: {titulo} | Precio: {precio}")

# Cálculo del precio promedio
promedio_precio = sum(primeros_10_libros.values()) / len(primeros_10_libros)
print(f"\nEl precio promedio de los primeros 10 libros es: {promedio_precio:.2f}")
"""



"""
import requests

datos = [{"prod": "Reloj", "info": {"p": 50}}, {"prod": "Anillo"}, {"prod": "Cadena", "info": {}}]

precio_p = datos[0].get("info", {}).get("p", "Precio no disponible")
print(f"El precio del producto es: {precio_p}")
"""



"""
import requests
from bs4 import BeautifulSoup

datos_del_login = {
    'username': 'JoseUsuario',
    'password': 'mi_password_seguro'
}

sesion = requests.Session()

URL_BASE = "https://quotes.toscrape.com/"
URL_LIGIN = URL_BASE + "login"
sesion.post(URL_LIGIN, data=datos_del_login)

respuesta = sesion.get(URL_BASE)
soup = BeautifulSoup(respuesta.text, 'html.parser')

boton_logout = soup.find('a', href='/logout')

if boton_logout:
    print("✅ ¡Infiltración exitosa! Estamos dentro del sistema.")
    print(sesion.cookies.get_dict())  # Muestra las cookies que se están usando en la sesión
else:
    print("❌ Error de acceso. El servidor nos rechazó.")
    """
    
    
    
"""    
import requests
from bs4 import BeautifulSoup

# Creamos la mochila
sesion = requests.Session()

# Iniciamos el contador en cero
total_libros_acumulados = 0

for pagina in range(1, 4):
    url = f"https://books.toscrape.com/catalogue/page-{pagina}.html"
    print(f"🔎 Explorando la {url}...")
    
    # Hacemos la petición usando la sesión
    res = sesion.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    # Buscamos todos los artículos de libros en esta página
    libros_en_esta_página = soup.find_all('article', class_='product_pod')
    cantidad = len(libros_en_esta_página)
    
    print(f"✅ Encontré {cantidad} libros en esta página.")
    
    # Sumamos al total (el símbolo += significa: "lo que ya tenía más lo nuevo")
    total_libros_acumulados += cantidad
    
print("-" * 30)
print(f"🏆 ¡OPERACIÓN TERMINADA!")
print(f"📚 Total de libros recolectados entre las 3 páginas: {total_libros_acumulados}")
"""



"""
import requests

datos = [
    {"producto": "Reloj", "precio": 50},
    {"producto": "Anillo"},
    {"producto": "Collar", "precio": 120}
]

for item in datos:
    producto = item.get("producto", "Producto desconocido")
    precio = item.get("precio", "Precio no disponible")
    
    print(f"Producto: {producto} | Precio: {precio}")
"""



"""
import requests
from bs4 import BeautifulSoup

# Creamos la mochila
sesion = requests.Session()

# Iniciamos el contador en cero
total_titulos_acumulados = 0

for pagina in range(1, 4):
    url = f"https://books.toscrape.com/catalogue/page-{pagina}.html"
    print(f"🔎 Explorando la {url}...")
    
    # Hacemos la petición usando la sesión
    res = sesion.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    titulos_en_esta_pagina = soup.find_all('h3')
    cantidad_titulos_en_esta_pagina = len(titulos_en_esta_pagina)
    
    total_titulos_acumulados += cantidad_titulos_en_esta_pagina
    
    print(f"✅ Encontré {cantidad_titulos_en_esta_pagina} títulos en esta página.")
    
print("-" * 30)
print(f"🏆 ¡OPERACIÓN TERMINADA!")
print(f"📚 Total de títulos recolectados entre las 3 páginas: {total_titulos_acumulados}")
"""



"""
import csv

# 1. Los datos "falsos" que vamos a guardar por ahora (una lista de listas)
datos_inventario = [
    ["Anillo de Oro 18k", 150],
    ["Collar de Plata", 80],
    ["Pulsera con Diamantes", 300]
]

# 2. Creamos (o abrimos) el archivo en modo "w" (write = escribir)
with open("inventario_artemisa.csv", mode="w", newline="", encoding="utf-8") as archivo:
    
    # Creamos la herramienta que sabe cómo escribir en formato CSV
    escritor_csv = csv.writer(archivo)
    
    # 3. Primero, escribimos la fila de los títulos (Cabeceras)
    escritor_csv.writerow(["Nombre del Producto", "Precio en Dólares"])
    
    # 4. Segundo, escribimos todos los datos de golpe
    escritor_csv.writerows(datos_inventario)

print("✅ ¡Magia pura! El archivo 'inventario_artemisa.csv' se ha creado.")
"""



"""
import requests
from bs4 import BeautifulSoup
import csv

sesion = requests.Session()

# 1. Creamos la "caja fuerte" donde guardaremos todo antes de pasarlo al CSV
todos_los_libros = []

print("🚀 Iniciando extracción de datos...")

# 2. El motor del bot (viajamos por 3 páginas)
for pagina in range(1, 4):
    url = f"https://books.toscrape.com/catalogue/page-{pagina}.html"
    print(f"🔎 Extrayendo página {pagina}...")
    
    res = sesion.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    libros = soup.find_all('article', class_='product_pod')
    
    # 3. Extraemos título y precio de cada libro
    for libro in libros:
        titulo = libro.find('h3').find('a')['title']
        precio = libro.find('p', class_='price_color').text
        
        # Juntamos los datos en una mini-lista y los guardamos en la caja fuerte
        datos_del_libro = [titulo, precio]
        todos_los_libros.append(datos_del_libro)

print(f"✅ Extracción completada. {len(todos_los_libros)} libros encontrados.")
print("💾 Guardando en archivo Excel (CSV)...")

# 4. Abrimos el archivo y guardamos la información
with open("base_de_datos_libros.csv", mode="w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    
    # Escribimos los títulos de las columnas
    escritor.writerow(["Título del Libro", "Precio"])
    
    # Guardamos todos los datos de golpe
    escritor.writerows(todos_los_libros)

print("🏆 ¡Éxito! Tu base de datos está lista en 'base_de_datos_libros.csv'.")
"""




import requests
import csv

# 1. Obtenemos los datos de la joyería
url_api = "https://fakestoreapi.com/products/category/jewelery"
respuesta = requests.get(url_api)
datos_joyas = respuesta.json()

# 2. Preparamos nuestra "caja temporal"
lista_para_excel = []

for joya in datos_joyas:
    nombre = joya.get("title")
    precio = joya.get("price")
    
    # Metemos cada joya en la caja temporal
    lista_para_excel.append([nombre, precio])

print("✅ Datos de joyas extraídos. Preparando el Excel...")

# ==========================================
# 🚨 TU MISIÓN EMPIEZA AQUÍ 🚨
# ==========================================

# 3. Abre el archivo "proveedores_artemisa.csv" en modo escritura ("w")
# ESCRIBE AQUÍ LA LÍNEA DEL 'with open...':
with open("base_datos_artemisa.csv", mode="w", newline="", encoding="utf-8") as archivo:

    # 4. Crea el escritor CSV
    # ESCRIBE AQUÍ LA LÍNEA DEL 'csv.writer...':
    escritor = csv.writer(archivo)
        
    # 5. Escribe los títulos de las columnas (ej: "Producto", "Costo")
    # ESCRIBE AQUÍ LA LÍNEA DEL 'writerow':
    escritor.writerow(["Producto", "Costo"])

    # 6. Escribe toda la lista_para_excel de golpe
    # ESCRIBE AQUÍ LA LÍNEA DEL 'writerows':
    escritor.writerows(lista_para_excel)

print("🏆 ¡Base de datos de Artemisa creada exitosamente!")