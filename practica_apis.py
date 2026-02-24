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
