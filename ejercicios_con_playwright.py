"""from playwright.sync_api import sync_playwright

# 1. Iniciamos el motor de Playwright
with sync_playwright() as p:
    print("🤖 Despertando al bot...")
    
    # 2. Abrimos Chrome. 'headless=False' es el secreto para que TÚ puedas ver la ventana.
    navegador = p.chromium.launch(headless=False) 
    
    # 3. Abrimos una pestaña nueva
    pagina = navegador.new_page()
    
    print("🌐 Viajando a la web de frases...")
    # 4. Le decimos al navegador a dónde ir
    pagina.goto("https://quotes.toscrape.com/")
    
    print("👀 ¡Mira la pantalla! El bot cerrará esto en 3 segundos...")
    
    # 5. Hacemos que el bot espere 3 segundos (3000 milisegundos) para que te dé tiempo de verlo
    pagina.wait_for_timeout(3000) 
    
    # 6. Apagamos todo de forma limpia
    navegador.close()
    
print("🏆 Travesura completada. ¡Bienvenido a las grandes ligas!")
"""



"""
from playwright.sync_api import sync_playwright

def iniciar_bot():
    # 1. Iniciamos el motor general
    with sync_playwright() as p:
        
        print("1️⃣ Abriendo el Navegador...")
        # Llevamos headless=False para ver qué hace. 
        # slow_mo=1000 hace que el bot espere 1 segundo (1000ms) entre cada acción para que nuestros ojos humanos puedan seguirlo.
        navegador = p.chromium.launch(headless=False, slow_mo=1000)
        
        print("2️⃣ Creando un Contexto (Perfil en blanco)...")
        contexto = navegador.new_context()
        
        print("3️⃣ Abriendo una nueva pestaña (Página)...")
        pagina = contexto.new_page()
        
        print("🌐 Navegando a la web de filosofía...")
        pagina.goto("https://quotes.toscrape.com/")
        
        print("✅ Misión cumplida. Cerrando en 3 segundos...")
        pagina.wait_for_timeout(3000)
        
        # Apagamos todo en orden
        contexto.close()
        navegador.close()

# Ejecutamos la función
iniciar_bot()
"""



"""
from playwright.sync_api import sync_playwright

def login_automatico():
    with sync_playwright() as p:
        # Iniciamos con slow_mo para ver la magia en cámara lenta
        navegador = p.chromium.launch(headless=False, slow_mo=500)
        pagina = navegador.new_page()
        
        print("🌐 1. Entrando a la página principal...")
        pagina.goto("https://quotes.toscrape.com/")
        
        print("🖱️ 2. Buscando el botón de Login y haciendo clic...")
        # Playwright tiene un súper poder: puede buscar botones solo por su texto visible
        pagina.locator("text=Login").click()
        
        print("⌨️ 3. Escribiendo usuario y contraseña...")
        # Usamos los selectores CSS de las cajas de texto (igual que en BeautifulSoup)
        pagina.locator("#username").fill("aporia_admin")
        pagina.locator("#password").fill("filosofia123")
        
        print("🚀 4. Presionando el botón para entrar...")
        pagina.locator("input[type='submit']").click()
        
        print("✅ ¡Infiltración exitosa! Mira la esquina superior derecha de la web.")
        
        # Le damos 4 segundos para que aprecies el resultado antes de cerrar
        pagina.wait_for_timeout(4000)
        navegador.close()

login_automatico()
"""



"""
from playwright.sync_api import sync_playwright

print("Iniciando motor...")

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=True) # Lo ponemos en True para que lo haga invisible y rápido
    pagina = navegador.new_page()
    
    print("Viajando a Wikipedia...")
    pagina.goto("https://es.wikipedia.org/wiki/Filosofía")
    
    print("📸 Tomando foto...")
    # Esta es la magia de Playwright en 1 línea
    pagina.screenshot(path="foto_filosofia.png") 
    
    print("✅ ¡Foto guardada en tu carpeta!")
    """
    


"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()
    pagina.goto("https://quotes.toscrape.com/")
    print("2. Haciendo clic en el botón Login...")
    pagina.locator("text=Login").click()
    print("3. Pausa para que veas que cambió de página...")
    pagina.wait_for_timeout(3000)
    
    print("4. ingresando usuario y contraseña en la pagina de login...")
    pagina.locator("#username").fill("aporia_admin")
    pagina.locator("#password").fill("filosofia123")
    
    print("5. dandole click al boton de submit par aingresar a la pagina...")
    pagina.locator("input[type='submit']").click()
    
    pagina.wait_for_timeout(3000)
    """
    
    
    
"""    
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    
    pagina = navegador.new_page()
    pagina.goto("https://es.wikipedia.org/")
    
    print("buscando el buscarod de wikipedia")
    pagina.locator("#searchInput").fill("filosofia")
    
    print("dandole enter a la busqueda que hicimos")
    pagina.locator("#searchInput").press("Enter")
    
    print("viendo el resultado de la busqueda")
    pagina.wait_for_timeout(3000)
"""

#lunes 9 de marzo
#ejercicio que obtiene la primera frase de la pagina de las etiquetas .text que encuentre

"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=True)
    
    pagina = navegador.new_page()
    pagina.goto("https://quotes.toscrape.com/")
    
    print("robando la primera frase")
    frase_robada = pagina.locator(".text").first.inner_text()
    
    print("se logro robar la primera frase")
    print(f"{frase_robada}")
    """
    
#ejercicio que obtiene todas las frases de las etiquetas .text que encuentre
    
"""    
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=True)
    
    pagina = navegador.new_page()
    pagina.goto("https://quotes.toscrape.com/")
    
    print("obteniendo todas las frases de la pagina")
    todas_las_frases = pagina.locator(".text").all_inner_texts()
    
    cantidad = len(todas_las_frases)
    
    print(f"se logro obtener {cantidad} frases en total")
    
    for i in todas_las_frases:
        print(f"{i}")
"""

#ejercicio que obtiene las frases que encuentre y el autor correspondiente

"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    navegador = p.chromium.launch()
    
    pagina = navegador.new_page()
    pagina.goto("https://quotes.toscrape.com/")
    
    frase = pagina.locator(".text").all_inner_texts()
    autor = pagina.locator(".author").all_inner_texts()
    
    cantidad = len(frase)
    print(f"obtuvimos un total de {cantidad} frases")
    
    for i in range(5):
        print(f"{frase[i]}")
        print(f"{autor[i]}")
        print("---------------------------------------------")
"""

#ejercicio que captura el primer texto de las primeras 2 paginas del link

"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=True)
    
    pagina = navegador.new_page()
    pagina.goto("https://quotes.toscrape.com/")
    
    primera_frase = pagina.locator(".text").first.inner_text()
    print(f"esta es la primera frase: {primera_frase}")
    
    #pasamos a la siguiente pagina
    pagina.locator("text=Next").click()
    
    print("------------------------------------------------------------------------------------------")
    segunda_frase = pagina.locator(".text").first.inner_text()
    print(f"esta es la segunda frase: {segunda_frase}")
    
    print("se obtuvieron las primeras frases de las 2 paginas")
"""

#ejercicio que captura todos los datos de todas las paginas de la url

"""
from playwright.sync_api import sync_playwright
import csv

todos_los_datos = []

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=True)
    
    pagina = navegador.new_page()
    pagina.goto("https://quotes.toscrape.com/")
    
    pagina_actual = 1
    
    while True:
        print(f"obteniendo los datos de la pagina {pagina_actual}")
        
        lista_frases = pagina.locator(".text").all_inner_texts()
        lista_autores = pagina.locator(".author").all_inner_texts()
        
        for i in range(len(lista_frases)):
            todos_los_datos.append([lista_frases[i], lista_autores[i]])
            
        boton_siguiente_pagina = pagina.locator(".next > a")
        
        if boton_siguiente_pagina.is_visible():
            boton_siguiente_pagina.click()
            pagina_actual += 1
        else:
            print("no hay un boton para la siguiente pagina, terminando el programa...")
            break
        
print("\n============================================================================================================")
print("Extraccion masiva de datos completada")
print(f"total de frases extraidas en la base de datos: {len(todos_los_datos)}")
print("===============================================================================================================")

print("muestra de la lista de diccionarios")
print(todos_los_datos[0])
print(todos_los_datos[1])

with open("lista_frases_autores.csv", mode="w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    
    escritor.writerow(["todas las frases", "autores"])
    escritor.writerows(todos_los_datos)
    
print("se agregaron todas las frases y sus autores a un archivo .csv")
"""

#martes 10 de marzo
#ejercicio para loguearse en una pagina y guardar la coockie

"""
from playwright.sync_api import sync_playwright

def guardar_sesion():
    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=False, slow_mo=500)
        
        contexto = navegador.new_context()
        pagina = contexto.new_page()
        
        pagina.goto("https://quotes.toscrape.com/login")
        pagina.locator("#username").fill("aporia_admin")
        pagina.locator("#password").fill("filosofia123")
        pagina.locator("input[type='submit']").click()
        
        contexto.storage_state(path="estado_sesion.json")
        
        print("archivo 'estado_sesion.json' creado")
        pagina.wait_for_timeout(3000)
        
guardar_sesion()
"""

#ejercicio para usar la cookie que se guardo para acceder a la pagina sin necesidad de ingresar usuario y contraseña

"""
from playwright.sync_api import sync_playwright

def entrar_con_coockie():
    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=False)
        
        contexto = navegador.new_context(storage_state='estado_sesion.json')
        
        pagina = contexto.new_page()
        pagina.goto("https://quotes.toscrape.com/")
        
        pagina.wait_for_timeout(5000)
        
entrar_con_coockie()
"""

#ejercicio para agarrar la coockie que guardamos antes y usarla para acceder a la misma pagina web sin usuario ni contraseña, si no funciona entonces ingresamos con usuario y contraseña y reemplazamos la coockie anterior por la nueva

"""
import os
from playwright.sync_api import sync_playwright

archivo_sesion = "estado_sesion.json"

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False, slow_mo=500)
    
    if os.path.exists(archivo_sesion):
        print("llave encontrada, intentando entrar a la pagina")
        contexto = navegador.new_context(storage_state=archivo_sesion)
        
    else:
        print("no se encontro la llave, creando una nueva")
        contexto = navegador.new_context()
        
    pagina = contexto.new_page()
    pagina.goto("https://quotes.toscrape.com/")
    
    boton_login = pagina.locator("text=login")
    
    if boton_login.is_visible():
        boton_login.click()
        pagina.locator("#username").fill("aporia_admin")
        pagina.locator("#password").fill("filosofia123")
        pagina.locator("input[type='submit']").click()
        
        contexto.storage_state(path=archivo_sesion)
        
    else:
        print("se consiguio entrar a la pagina con la coockie obtenida en el pasado")
        
    pagina.wait_for_timeout(4000)
"""

#miercoles 11 de marzo
#ejercicio para entrar a otra pagina que tiene mejor seguridad que la anterior

"""
import os
from playwright.sync_api import sync_playwright

archivo_sesion = "llave.ecommerce.json"

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False, slow_mo=500)
    
    if os.path.exists(archivo_sesion):
        print("coockie encontrada, usandola para entrar a la pagina")
        contexto = navegador.new_context(storage_state=archivo_sesion)
    else:
        print("no se encontro el archivo de la coockie, ingresando a la pagina manualmente")
        contexto = navegador.new_context()
        
    pagina = contexto.new_page()
    pagina.goto("https://www.saucedemo.com/inventory.html")
    
    boton_login = pagina.locator("#login-button")
    
    if boton_login.is_visible():
        print("el servidor nos detecto y nos boto al login")
        
        pagina.locator("#user-name").fill("standard_user")
        pagina.locator("#password").fill("secret_sauce")
        boton_login.click()
        
        contexto.storage_state(path=archivo_sesion)
        print("la nueva coockie se ha guardado en tu pc")
    else:
        print("entrando a la pagina con exito")
        
    primer_producto = pagina.locator(".inventory_item_name").first.inner_text()
    print(f"primer producto en pantalla: {primer_producto}")

    pagina.wait_for_timeout(3000)
"""

#jueves 12 de marzo

"""
from playwright.sync_api import sync_playwright

# 1. Construimos nuestro "Audífono de Espía"
# Esta función se activará sola cada vez que el servidor envíe CUALQUIER COSA a tu computadora
def capturar_trafico(respuesta):
    # La web descarga cientos de imágenes y basura. 
    # Solo queremos interceptar las llamadas tipo "fetch" o "xhr" (donde viven los JSON)
    if respuesta.request.resource_type in ["fetch", "xhr"]:
        print(f"📡 API Detectada en: {respuesta.url}")
        print(f"   Estado: {respuesta.status}")
        print("-" * 50)

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False, slow_mo=500)
    contexto = navegador.new_context()
    pagina = contexto.new_page()
    
    # 2. 🎯 LA MAGIA: Conectamos el radar a la página ANTES de navegar
    pagina.on("response", capturar_trafico)
    
    print("🚀 Entrando a la búsqueda de empleos y prendiendo el radar...\n")
    
    # Entramos directamente a la sección de tecnología
    pagina.goto("https://pe.computrabajo.com/trabajo-de-python")
    
    # Pausa de 10 segundos para que te dé tiempo de ver la página
    # y para que el radar termine de capturar todos los paquetes rezagados
    pagina.wait_for_timeout(10000)
    
    print("\n✅ Escaneo de red finalizado.")
    """
    


"""
from playwright.sync_api import sync_playwright

# 1. Creamos nuestro "Audífono de Espía"
def capturar_trafico(respuesta):
    # Filtramos: Solo queremos URLs con "offer/" y que hayan sido exitosas (Status 200)
    if "offer/" in respuesta.url and respuesta.status == 200:
        print(f"\n🎯 ¡Blanco fijado! URL interceptada: {respuesta.url}")
        
        try:
            # 📦 LA MAGIA: Convertimos la respuesta de la web en un Diccionario de Python
            datos = respuesta.json()
            
            # Imprimimos solo un fragmento para no inundar toda tu pantalla
            print("💎 ¡Tesoro extraído! Aquí están los datos ocultos:")
            print(str(datos)[:400] + " ... [Datos cortados para resumir]")
            print("-" * 60)
            
        except:
            print("🔒 Falsa alarma: El paquete no era un JSON o estaba vacío.")

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()
    
    # 2. Conectamos el radar ANTES de entrar a la web
    pagina.on("response", capturar_trafico)
    
    print("🚀 Entrando a la página. Preparando radares...\n")
    pagina.goto("https://pe.computrabajo.com/trabajo-de-python")
    
    print("👉 ¡Tu turno! Haz clic en 3 ofertas diferentes de la lista izquierda.")
    
    # Te doy 20 segundos para que hagas clic manualmente en las ofertas
    pagina.wait_for_timeout(20000)
    
    print("\n✅ Intervención finalizada.")
"""

#viernes 13 de noviembre

"""
from playwright.sync_api import sync_playwright
import time
import json

def capturar_trafico(respuesta):
    if "oferta.computrabajo.com/offer/" in respuesta.url and respuesta.status == 200:
        try:
            datos = respuesta.json()
            print(f"------------------- busca aqui las etiquetas del titulo y la empresa --------------")
            
            descripcion = datos.get("o", {}).get("ld", "sin descripcion")
            
            print(descripcion[:300] + " ... [CORTADO]")
            print("-" * 60)
            
        except:
            pass
        
with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False, slow_mo=500)
    pagina = navegador.new_page()
    
    pagina.on("response", capturar_trafico)
    
    print(f"entrando a la web y buscando ofertas")
    pagina.goto("https://pe.computrabajo.com/trabajo-de-python")
    
    ofertas = pagina.locator(".box_offer")
    
    cantidad = ofertas.count()
    print(f"se encontraron {cantidad} ofertas. Iniciando extraccion automatica")
    
    for i in range(5):
        print(f"bot haciendo click en la oferta {i + 1}")
        
        ofertas.nth(i).click()
        
        time.sleep(2)
"""

#ejercicio para capturar las apis que pasan por tiktok

"""
from playwright.sync_api import sync_playwright
import time

def atrapar_productos(respuesta):
    if respuesta.request.resource_type in ["fetch", "xhr"]:
        if "cloudfront.net" not in respuesta.url and "google-analytics.com" not in respuesta.url and "analytics.google.com" not in respuesta.url and "google.com" not in respuesta.url:
            print(f"📡 ¡Api detectada!: {respuesta.url}")
        
            print(f"   Tipo de paquete: {respuesta.headers.get('content-type', 'Desconocido')}")
            print("-" * 50)
        
        
with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False, slow_mo=500)
    pagina = navegador.new_page()
    
    pagina.on("response", atrapar_productos)
    pagina.goto("https://webscraper.io/test-sites/e-commerce/more/computers/laptops")
    
    boton_cargar_mas = pagina.locator("button.e-commerce-more")
    
    for i in range(3):
        if boton_cargar_mas.is_visible():
            print(f"click {i +1}")
            boton_cargar_mas.click()
            
            time.sleep(2)
        else:
            break
"""

#sabado 14 de marzo
#codigo para capturar la api de unsplash.com sin tener que ir a la pagina

"""
from playwright.sync_api import sync_playwright
import time

def capturar_api(respuesta):
    if respuesta.request.resource_type in ["fetch", "xhr"]:
        if "napi/search" in respuesta.url or "napi/photos" in respuesta.url:
            try:
                datos = respuesta.json()
                
                lista_fotos = datos.get("results", [])
                
                if len(lista_fotos) > 0:
                    print(f"paquete de {len(lista_fotos)} capturado")
                    
                    for foto in lista_fotos:
                        link_imagen = foto.get('urls', {}).get('regular', 'sin link')
                        fotografo = foto.get('user', {}).get('name', 'nonimo')
                        
                        print(f"📸 {fotografo}: {link_imagen}")
                        
                        print("-" * 60)
            except:
                pass
            
with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False, slow_mo=300)
    pagina = navegador.new_page()
    
    pagina.on("response", capturar_api)
    
    pagina.goto("https://unsplash.com/es/s/fotos/tecnologia")
    
    time.sleep(3)
    
    boton_continuar = pagina.locator("button", has_text="Cargar más")
    
    for i in range(3):
        if boton_continuar.is_visible():
            boton_continuar.click()
            time.sleep(1)
            pagina.keyboard.press("End")
            
            time.sleep(3)
        else:
            pagina.keyboard.press("End")
            time.sleep(3)
"""

#codigo para capturar los productos, precios y reseña del producto de una api


from playwright.sync_api import sync_playwright
import json

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=True)
    pagina = navegador.new_page()
    
    respuesta = pagina.goto("https://dummyjson.com/products/category/womens-jewellery")
    
    datos = respuesta.json()
    productos = datos.get("products", [])
    
    if len(productos) > 0:
        print(f"paquete de {len(productos)} productos capturados")
        
        for producto in productos:
            nombre = producto.get("title", "no se encontro el titulo")
            precio = producto.get("price", "no se encontro el precio")
            rating = producto.get("rating", "no se encontro el rating")
            
            print(f"producto: {nombre} \nprecio: {precio} \nrating: {rating}")