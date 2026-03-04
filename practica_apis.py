"""import requests
import json

url_api = "https://www.plazavea.com.pe/api/catalog_system/pub/products/search?fq=H:47664&_from=0&_to=15"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0"
}

response = requests.get(url_api, headers=headers)

datos_json = response.json()

catalogo_final = []

for producto in datos_json:
    nombre = producto.get("productName", "Sin nombre")
    
    try:
        precio = producto.get("items", [{}])[0].get("sellers", [{}])[0].get("commertialOffer", {}).get("Price", "Sin precio")
    
    except (KeyError, IndexError, TypeError):
        precio  = 0.0
        
    catalogo_final.append({
        "Producto": nombre,
        "Precio": precio
    })
    
from pprint import pprint
pprint(catalogo_final[:3])
"""

"""----------------------------------------------------------------------------------"""

"""
catalogo_api = [
    {"nombre": "Anillo A", "detalles": {"precio": 100, "stock": 5}},
    {"nombre": "Anillo B", "detalles": {"precio": 200}}, # Falta stock
    {"nombre": "Anillo C"} # Falta la sección 'detalles' completa
]

for joya in catalogo_api:
    # 1. Extracción segura del primer nivel
    nombre = joya.get("nombre", "Sin Nombre")
    
    # 2. RETO A: Extraer la "carpeta" de detalles. 
    # Si la joya no tiene "detalles" (como el Anillo C), tu salvavidas DEBE ser un diccionario vacío: {}
    info_segura = joya.get("detalles", {})
    
    # 3. RETO B: Ahora que tienes 'info_segura' (que puede ser los datos reales o tu {} vacío), 
    # extrae el precio. Si no hay precio, el salvavidas es 0.
    precio = info_segura.get("precio", 0)
    
    # 4. RETO C: Extrae el stock usando la misma lógica. Si no hay, el salvavidas es 0.
    stock = info_segura.get("stock", 0)
    
    print(f"Joya: {nombre} | Precio: ${precio} | Stock: {stock}")
    """
    
    
"""    
import pprint

datos = {
    'usuario': 'admin',
    'permisos': ['leer', 'escribir', 'eliminar'],
    'config': {'tema': 'oscuro', 'idioma': 'es'}
}

# Con print() normal (salida desordenada)
#print(datos)

# Con pprint (salida formateada)
pprint.pprint(datos)
"""


"""
import requests
import json

url_api = "https://fakestoreapi.com/products/category/jewelery"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0"
}

response = requests.get(url_api)
datos_json = response.json()

catalogo_final = []

for producto in datos_json:
    nombre = producto.get("title", "sin nombre")
    precio = producto.get("price", 0)
    
    catalogo_final.append({
        "Producto": nombre,
        "Precio": precio
    })
    
from pprint import pprint
pprint(catalogo_final)
"""



"""
import requests
import json

url_api = "https://pokeapi.co/api/v2/pokemon/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0"
}

response = requests.get(url_api, headers=headers)
datos_json = response.json()

pokemon = input("Ingrese el nombre de un Pokémon: ").lower()
respuesta = requests.get(f"{url_api}{pokemon}", headers=headers)

datos_pokemon = respuesta.json()

print(f"Nombre: {pokemon} | tipo: {datos_pokemon.get('types', [{}])[0].get('type', {}).get('name', 'Desconocido')}")

primeros_5_movimientos = datos_pokemon.get("moves", [])[:5]

for movimiento in primeros_5_movimientos:
    nombre_movimiento = movimiento.get('move', []).get('name', 'desconocido')
    
    print(f"Movimiento: {nombre_movimiento}")
"""



"""
import requests

# Creamos el objeto sesión. Este es nuestro "navegador virtual" con memoria.
sesion = requests.Session()

# PASO 1: Vamos a una URL que nos "regala" una cookie de acceso.
# Imagina que esto es el login de tu proveedor de joyas.
print("Obteniendo credenciales...")
sesion.get("https://httpbin.org/cookies/set/nivel_acceso/mayorista_oro")

# PASO 2: Ahora pedimos ver qué cookies tenemos guardadas.
# Si usamos la MISMA sesión, recordará que somos 'mayorista_oro'.
respuesta = sesion.get("https://httpbin.org/cookies")

print("\nCookies guardadas en la sesión:")
print(respuesta.json())

# PASO 3: ¿Qué pasa si intento entrar con un request normal (sin sesión)?
print("\nIntento con un request independiente (sin memoria):")
independiente = requests.get("https://httpbin.org/cookies")
print(independiente.json())
"""



"""
import requests
from bs4 import BeautifulSoup

# Creamos la sesión (Nuestra mochila)
sesion = requests.Session()

# 1. Definimos los datos del login (Esta página acepta cualquier usuario/pass)
datos_login = {
    'username': 'Artemisa_Bot',
    'password': 'password123'
}

# 2. ENVIAR LOS DATOS (El Login)
# Usamos .post para 'empujar' los datos al servidor
url_login = "https://quotes.toscrape.com/login"
sesion.post(url_login, data=datos_login)

# 3. VERIFICACIÓN: Intentamos ir a una página que requiere estar logueado
# En esta web, si estás logueado, aparece un enlace que dice "Logout"
respuesta = sesion.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(respuesta.text, 'html.parser')

# Buscamos si existe el botón de Logout
boton_logout = soup.find('a', href='/logout')

if boton_logout:
    print("✅ ¡Infiltración exitosa! Estamos dentro del sistema.")
else:
    print("❌ Error de acceso. El servidor nos rechazó.")
"""



"""
import requests

# --- ESCENARIO A: Sin Sesión (El olvidadizo) ---
print("--- Escenario A ---")
requests.get("https://httpbin.org/cookies/set/nombre/Jose")
respuesta_a = requests.get("https://httpbin.org/cookies")
print(f"¿Me conoce el servidor?: {respuesta_a.json()}") 
# Saldrá {} (vacío), porque olvidó quién eres entre el primer y segundo paso.


# --- ESCENARIO B: Con Sesión (El que recuerda) ---
print("\n--- Escenario B ---")
mi_cartera = requests.Session() # Creamos la memoria
mi_cartera.get("https://httpbin.org/cookies/set/nombre/Jose")
respuesta_b = mi_cartera.get("https://httpbin.org/cookies")
print(f"¿Me conoce el servidor?: {respuesta_b.json()}") 
# Saldrá {'cookies': {'nombre': 'Jose'}}. ¡Te recordó!
"""



"""
import requests
import json

url_api = "https://fakestoreapi.com/products/category/jewelery"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0"
}

response = requests.get(url_api, headers=headers)
datos_json = response.json()

catalogo_100 = []

for producto in datos_json:
    precio = producto.get("price", 0)
    
    if precio > 100:
        nombre = producto.get("title", "sin nombre")
        catalogo_100.append({
            "Producto": nombre,
            "Precio": precio
        })
        
from pprint import pprint
pprint(catalogo_100)
"""



"""
import requests
import json

url_api = "https://jsonplaceholder.typicode.com/posts"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0"
}

response = requests.get(url_api, headers=headers)
datos_json = response.json()

post_user_1 = []

for post in datos_json:
    if post.get("userId") == 1:
        post_user_1.append({
            "title": post.get("title", "sin título"),
            "body": post.get("body", "sin cuerpo")
        })
        
print(f"Posts del usuario 1: {len(post_user_1)}\n")
for post in post_user_1:
    print(f"Titulo: {post['title']}\nCuerpo: {post['body']}\n---")
"""



"""
import requests
import json

url_api = "https://fakestoreapi.com/products"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0"
}

response = requests.get(url_api, headers=headers)
datos_json = response.json()

lista_productos = []

for producto in datos_json:
    nombre = producto.get("title", "sin nombre")
    tasa = producto.get("rating", {}).get("rate", 0)
    
    lista_productos.append({
        "Producto": nombre,
        "Rating": tasa
    })
    
print("estos son los productos con su rating: ")
for producto in lista_productos:
    print(f"Producto: {producto['Producto']} | Rating: {producto['Rating']}")
"""



"""
import requests
import json

url_api = "https://fakestoreapi.com/products/1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0"
}

response = requests.get(url_api, headers=headers)
datos_json = response.json()

producto_formateado = {
    "Producto": datos_json.get("title", "sin título"),
    "Precio": datos_json.get("price", 0),
    "Categoria": datos_json.get("category", "sin categoría")
}

print("Producto formateado:")
print(json.dumps(producto_formateado, indent=4))
"""



"""
import requests

# 1. Creamos la sesión
navegador = requests.Session()

print("--- Iniciando recorrido de sesión ---")

# 2. Primera parada: Obtenemos la cookie de identidad
navegador.get("https://httpbin.org/cookies/set/usuario/jose_artemisa")

# 3. Segunda parada: Obtenemos la cookie de idioma (SIN PERDER LA ANTERIOR)
# URL: https://httpbin.org/cookies/set/idioma/espanol
# ESCRIBE AQUÍ LA LÍNEA PARA VISITAR ESA URL:

navegador.get("https://httpbin.org/cookies/set/idioma/espanol")

# 4. Tercera parada: Verificamos qué hay en nuestra "mochila"
respuesta = navegador.get("https://httpbin.org/cookies")
datos_finales = respuesta.json()

print("\nContenido de mi mochila de sesión:")
print(datos_finales)

# 5. VALIDACIÓN PROFESIONAL
if "usuario" in datos_finales['cookies'] and "idioma" in datos_finales['cookies']:
    print("\n✅ EXCELENTE: La sesión mantuvo ambos datos. Eres un experto en persistencia.")
else:
    print("\n❌ ALGO FALLÓ: Se perdió una cookie en el camino.")
    """
    
#Domingo 1 de Marzo

"""
import requests
import json

url_api = "https://fakestoreapi.com/products/category/jewelery"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0"
}

response = requests.get(url_api, headers=headers)
datos_json = response.json()

nombre_articulos_baratos = []

for productos in datos_json:
    precio = productos.get("price", 0)
    nombre = productos.get("title", "no se encontor el nombre de este articulo")
    
    if precio <= 100:
        nombre_articulos_baratos.append(nombre)
    
print(f"{nombre_articulos_baratos}")
"""

# Lunes 2 de Marzo

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