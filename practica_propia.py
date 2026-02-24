"""import requests
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
