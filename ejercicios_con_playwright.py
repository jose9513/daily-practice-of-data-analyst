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

#ejercicio que captura el primer texto de cada pagina del link


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