"""import json

stock_joyeria = #aca se necesita triple dobles comillas[
    {"nombre": "anillo", "precio": 100, "cantidad": 10},
    {"nombre": "collar", "precio": 250, "cantidad": 1},
    {"nombre": "pulsera", "precio": 150, "cantidad": 8}
]#aca se necesita triple dobles comillas

leads = json.loads(stock_joyeria)

print(f"Analizando {len(leads)} leads de joyería...")

comprar_mas = [c for c in leads if c["cantidad"] < 2]

print(f"se necesita comprar mas de: {[c['nombre'] for c in comprar_mas]}")"""

"""-----------------------------------------------------------------------------------------"""

"""
# Simulamos que esto llegó de internet
data_simulada = {
    "bpi": {
        "USD": {"rate": "98,450.60"}
    }
}

try:
    # Extraemos y limpiamos el precio
    precio_raw = data_simulada["bpi"]["USD"]["rate"]
    precio_limpio = float(precio_raw.replace(',', ''))
    
    print(f"💰 Precio simulado: ${precio_limpio}")

    # --- TU LÓGICA DE NEGOCIO ---
    if precio_limpio > 95000:
        print("🚀 Vende para reinvertir en stock de ARTEMISA.")
    else:
        print("💎 Sigue acumulando para la Agencia de Automatización.")
        
except Exception as e:
    print(f"❌ Error procesando datos: {e}")"""
    
"""------------------------------------------------------------------------------------------"""

"""import requests

# Esta API devuelve personajes de Rick and Morty
url = "https://rickandmortyapi.com/api/character"

try:
    response = requests.get(url)
    response.raise_for_status() # Esto lanza un error si la página no carga
    
    data = response.json()
    personajes = data["results"] # Aquí están los datos reales

    print(f"✅ Conexión exitosa. Se encontraron {len(personajes)} personajes.")

    # RETO DE FILTRADO:
    # Solo queremos los personajes que estén "Alive" (Vivos)
    vivos = [p["name"] for p in personajes if p["status"] == "Alive"]
    
    print(f"Personajes vivos encontrados: {vivos}")

except requests.exceptions.ConnectionError:
    print("❌ Seguimos con problemas de internet. Revisa tu conexión o DNS.")
except Exception as e:
    print(f"❌ Ocurrió un error inesperado: {e}")"""
    
"""------------------------------------------------------------------------------------------"""

"""import requests

url = "https://rickandmortyapi.com/api/character"

try:
    response = requests.get(url)
    response.raise_for_status()
    
    data = response.json()
    personajes = data["results"]
    personajes_interesantes = [p["name"] for p in personajes if p["species"] == "Human" and p["status"] == "Alive"]
    
    print(f"Personajes humanos vivos encontrados: {personajes_interesantes}")
    
except requests.exceptions.ConnectionError:
    print("❌ Seguimos con problemas de internet. Revisa tu conexión o DNS.")
except Exception as e:
    print(f"❌ Ocurrió un error inesperado: {e}")"""
    
"""------------------------------------------------------------------------------------------"""

"""import requests
from bs4 import BeautifulSoup

url = "https://www.pandoraoficial.com.pe/" 
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

descuento = 0.15

try:
    # Buscamos el contenedor padre que tiene todo el precio
    contenedor_precio = soup.find('span', class_='vtex-product-price-1-x-currencyInteger')
    
    if contenedor_precio:
        # .get_text() con strip=True limpia espacios basura
        precio_completo = contenedor_precio.get_text(strip=True)
        precio_con_descuento = float(precio_completo.replace(',', '')) * (1 - descuento)
        print(f"✅ Precio Total: {precio_completo} 
precio con descuento = ${precio_con_descuento:.2f}")
    else:
        print("❌ Contenedor no encontrado")

except Exception as e:
    print(f"Error: {e}")
    """

"""------------------------------------------------------------------------------------------"""

"""import requests
from bs4 import BeautifulSoup

url = "https://www.pandoraoficial.com.pe/lanzamientos" 
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

enlaces = []

# ... tu código anterior ...
enlaces_productos = soup.find_all('a', class_=lambda x: x and 'product-summary' in x)

print(f"🔗 Se encontraron {len(enlaces_productos)} productos.")

for el in enlaces_productos:
    link_relativo = el['href']
    # Construimos el link completo si es necesario
    if link_relativo.startswith('/'):
        link_completo = f"https://www.pandoraoficial.com.pe{link_relativo}"
    else:
        link_completo = link_relativo
        
    print(f"🚀 Producto: {link_completo}")
    """
   
"""------------------------------------------------------------------------------------------"""

"""import requests
from bs4 import BeautifulSoup

url = "https://www.pandoraoficial.com.pe"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

productos_bloques = soup.find_all('section', class_=lambda x: x and 'vtex-product-summary-2-x-container' in x)

catalogo = []

for item in productos_bloques:
    """