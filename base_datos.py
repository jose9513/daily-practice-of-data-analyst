import sqlite3 as sql
"""
import sqlite3

# 1. Creamos la CONEXIÓN (Si el archivo no existe, Python lo crea automáticamente)
conexion = sqlite3.connect("catalogo_bisuteria.db")

# 2. Creamos el CURSOR (Nuestro brazo robótico)
cursor = conexion.cursor()

print("🏗️ Construyendo la base de datos...")

# 3. Le damos la orden al cursor en lenguaje SQL puro
# Le decimos: "Crea una tabla llamada 'productos' con estas 3 columnas"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        nombre TEXT,
        precio REAL,
        comentario TEXT
    )
''')

# 4. Guardamos los cambios estructurales
conexion.commit()

# 5. Cerramos la puerta por seguridad
conexion.close()

print("✅ Base de datos 'catalogo_bisuteria.db' creada exitosamente.")
"""

#jueves 19 de marzo

"""
import sqlite3

conexion = sqlite3.connect("catalogo_bisuteria.db")

cursor = conexion.cursor()

print("se conecto exitosamente con la base de datos")

comando_sql = "INSERT INTO productos VALUES (?, ?, ?)"

datos_productos = ("collar de perlas sinteticas", 45.50, "muy elegante y ligero")

cursor.execute(comando_sql, datos_productos)

conexion.commit()
conexion.close()
"""


# viernes 20 de marzo

"""
import sqlite3

conexion = sqlite3.connect("catalogo_bisuteria.db")

cursor = conexion.cursor()

print("se conecto exitosamente con la base de datos")

cursor.execute("SELECT * FROM productos")

mis_datos = cursor.fetchall()

for dato in mis_datos:
    print(dato)
    
conexion.close()
"""

#sabado 21 de marzo


"""
import sqlite3

lote_nuevo = [
    {"nombre": "Cadena de Eslabones 316L", "precio": 55.00, "comentario": "Baño PVD impecable"},
    {"nombre": "Anillo Minimalista", "precio": 35.50, "comentario": "No se oxida con el agua"},
    {"nombre": "Pulsera Ajustable", "precio": 42.00, "comentario": "Material muy resistente"}
]

conexion = sqlite3.connect("catalogo_bisuteria.db")

cursor = conexion.cursor()

for producto in lote_nuevo:
    comando_sql = "INSERT INTO productos VALUES (?, ?, ?)"

    datos_productos = (producto["nombre"], producto["precio"], producto["comentario"])
    
    cursor.execute(comando_sql, datos_productos)
    
conexion.commit()

cursor.execute("SELECT * FROM productos")

mis_datos = cursor.fetchall()

conexion.close()
"""

#domingo 22 de marzo

"""
import sqlite3

conexion = sqlite3.connect("catalogo_bisuteria.db")
cursor = conexion.cursor()

presupuesto_maximo = 50.0

comando = "SELECT * FROM productos WHERE precio <= ?"

cursor.execute(comando, (presupuesto_maximo,))

mis_datos = cursor.fetchall()

for dato in mis_datos:
    print(dato)
    
conexion.close()
"""

#lunes 23 de marzo

"""
import sqlite3 as sql

with sql.connect("catalogo_bisuteria.db") as conexion:
    cursor = conexion.cursor()
    cursor.execute("DROP TABLE IF EXISTS productos")
    cursor.execute('''
                   CREATE TABLE productos(
                       id_producto INTEGER,
                       nombre TEXT,
                       precio REAL,
                       comentario TEXT,
                       PRIMARY KEY(id_producto AUTOINCREMENT)
                   )
                   ''')
    print("se agrego un nuevo campo a la tabla de productos")
"""

"""
import sqlite3 as sql

lote_joyas = [
    ("Anillo Solitario Diamante", "Anillos", "Oro Blanco 18k", 2500.00, 2),
    ("Collar Lágrima de Luna", "Collares", "Plata 925", 85.50, 15),
    ("Pulsera Tejido Bizantino", "Pulseras", "Oro Amarillo 18k", 450.00, 5),
    ("Aretes Perla Cultivada", "Aretes", "Plata 925", 60.00, 20),
    ("Anillo Sello Ónice", "Anillos", "Plata 925", 110.00, 8),
    ("Gargantilla Esmeralda", "Collares", "Oro Blanco 18k", 1800.00, 1),
    ("Pulsera Hilo Rojo Destino", "Pulseras", "Plata 925", 25.00, 50),
    ("Argollas Clásicas M", "Aretes", "Oro Amarillo 18k", 220.00, 12),
    ("Anillo Compromiso Zafiro", "Anillos", "Oro Blanco 18k", 1500.00, 3),
    ("Cadena Veneciana 45cm", "Collares", "Plata 925", 45.00, 30),
    ("Dije Árbol de la Vida", "Dijes", "Plata 925", 35.00, 25),
    ("Anillo Media Alianza", "Anillos", "Oro Rosado 18k", 380.00, 6),
    ("Pulsera Tenis Circonias", "Pulseras", "Plata 925", 150.00, 10),
    ("Aretes Topacio Azul", "Aretes", "Oro Blanco 18k", 320.00, 4),
    ("Collar Doble Capa", "Collares", "Oro Amarillo 18k", 580.00, 7),
    ("Anillo Minimalista V", "Anillos", "Plata 925", 40.00, 18),
    ("Pulsera Eslabón Cubano", "Pulseras", "Oro Amarillo 18k", 850.00, 2),
    ("Aretes Botón Oro", "Aretes", "Oro Rosado 18k", 190.00, 14),
    ("Dije Inicial Personalizada", "Dijes", "Oro Amarillo 18k", 120.00, 0), # Sin stock
    ("Collar Cuarzo Rosa", "Collares", "Plata 925", 70.00, 22)
]

def agregar_datos():
    with sql.connect("catalogo_bisuteria.db") as conexion:
        cursor = conexion.cursor()
        cursor.execute("DROP TABLE IF EXISTS joyas")
        cursor.execute('''
                       CREATE TABLE joyas (
                           id_joya INTEGER PRIMARY KEY AUTOINCREMENT,
                           nombre TEXT,
                           categoria TEXT,
                           material TEXT,
                           precio REAL,
                           stock INTEGER
                       )
                       ''')
        
        comando = "INSERT INTO joyas (nombre, categoria, material, precio, stock) VALUES (?, ?, ?, ?, ?)"
        cursor.executemany(comando, lote_joyas)
        print(f"se agregaron {cursor.rowcount} joyas a la base de datos")
        
if __name__ == "__main__":
    agregar_datos()
"""

"""
with sql.connect("catalogo_bisuteria.db") as conexion:
    cursor = conexion.cursor()
    
    comando = "SELECT * FROM joyas WHERE material = 'Plata 925' AND precio < 100"
    cursor.execute(comando)
    datos = cursor.fetchall()
    
    for dato in datos:
        print(dato)
"""

"""
with sql.connect("catalogo_bisuteria.db") as conexion:
    cursor = conexion.cursor()
    
    comando = "SELECT * FROM joyas WHERE categoria IN ('Collares', 'Pulseras') AND material LIKE '%Oro%' "
    cursor.execute(comando)
    datos = cursor.fetchall()
    
    for dato in datos:
        print(dato)
"""

"""
with sql.connect("catalogo_bisuteria.db") as conexion:
    cursor = conexion.cursor()
    
    comando = "SELECT * FROM joyas WHERE stock == 0 OR precio >= 1000"
    cursor.execute(comando)
    datos = cursor.fetchall()
    
    for dato in datos:
        print(dato)
        """
        
"""        
with sql.connect("catalogo_bisuteria.db") as conexion:
    cursor = conexion.cursor()
    
    comando = "SELECT * FROM joyas WHERE precio BETWEEN 100 AND 300"
    cursor.execute(comando)
    
    datos = cursor.fetchall()
    for dato in datos:
        print(dato)
"""

"""
with sql.connect("catalogo_bisuteria.db") as conexion:
    cursor = conexion.cursor()
    
    comando = "SELECT * FROM joyas WHERE stock BETWEEN 1 AND 5"
    cursor.execute(comando)
    
    datos = cursor.fetchall()
    for dato in datos:
        print(dato)
"""

"""
with sql.connect("catalogo_bisuteria.db") as conexion:
    cursor = conexion.cursor()
    
    comando = "SELECT * FROM joyas WHERE categoria = 'Anillos' AND precio BETWEEN 1000 AND 3000"
    cursor.execute(comando)
    
    datos = cursor.fetchall()
    for dato in datos:
        print(dato)
"""

"""
with sql.connect("catalogo_bisuteria.db") as conexion:
    cursor = conexion.cursor()
    
    comando = "SELECT SUM(stock) FROM joyas"
    cursor.execute(comando)
    
    dato = cursor.fetchall()
    
    print(dato)
"""

"""
with sql.connect("catalogo_bisuteria.db") as conexion:
    cursor = conexion.cursor()
    
    comando = "SELECT AVG(precio) FROM joyas WHERE categoria = 'Aretes'"
    cursor.execute(comando)
    
    dato = cursor.fetchall()
    print(f"el promedio de las joyas de categoria 'aretes' es: {dato[0][0]}")
"""

"""
with sql.connect("catalogo_bisuteria.db") as conexion:
    cursor = conexion.cursor()
    
    comando = "SELECT SUM(precio * stock) FROM joyas"
    cursor.execute(comando)
    
    dato = cursor.fetchall()
    print(f"el ingreso total de todas las joyas seria de: {dato[0][0]}")
"""

"""
with sql.connect("catalogo_bisuteria.db") as conexion:
    cursor = conexion.cursor()
    
    comando = "SELECT categoria, COUNT(nombre) FROM joyas GROUP BY categoria"
    cursor.execute(comando)
    
    datos = cursor.fetchall()
    for dato in datos:
        print(dato)
"""

"""
with sql.connect("catalogo_bisuteria.db") as conexion:
    cursor = conexion.cursor()
    
    comando = "SELECT material, AVG(precio) FROM joyas GROUP BY material"
    cursor.execute(comando)
    
    datos = cursor.fetchall()
    for dato in datos:
        print(dato)
"""

"""
with sql.connect("catalogo_bisuteria.db") as conexion:
    cursor = conexion.cursor()
    
    comando = "SELECT categoria, SUM(precio * stock) FROM joyas GROUP BY categoria"
    cursor.execute(comando)
    
    datos = cursor.fetchall()
    for dato in datos:
        print(dato)
"""


def modelos_menos_de_5():
    with sql.connect("catalogo_bisuteria.db") as conexion:
        cursor = conexion.cursor()
        
        comando = """SELECT categoria, COUNT(nombre) as modelos_distintos
                    FROM joyas
                    GROUP BY categoria
                    HAVING modelos_distintos < 5"""
        cursor.execute(comando)
        
        datos = cursor.fetchall()
        for dato in datos:
            print(dato)

#--------------------------------------------------------------------------------------------------------------

def rentabilidad_material():
    with sql.connect("catalogo_bisuteria.db") as conexion:
        cursor = conexion.cursor()
        
        comando = """SELECT material, AVG(precio) as promedio
                     FROM joyas
                     GROUP BY material
                     HAVING promedio > 100"""
        cursor.execute(comando)
        
        datos = cursor.fetchall()
        for dato in datos:
            print(dato)

#------------------------------------------------------------------------------------

def dinero_inmovilizado():
    with sql.connect("catalogo_bisuteria.db") as conexion:
        cursor = conexion.cursor()
        
        comando = """SELECT categoria, SUM(precio * stock) as suma_total
                     FROM joyas
                     WHERE precio > 50
                     GROUP BY categoria
                     HAVING suma_total > 1000"""
        cursor.execute(comando)
        
        datos = cursor.fetchall()
        for dato in datos:
            print(dato)
            
#-------------------------------------------------------------------------------------------------------


lote_ventas = [
    # (id_joya, fecha, cantidad_vendida)
    (2, '2026-03-20', 1), 
    (2, '2026-03-22', 2), 
    (5, '2026-03-24', 1), 
    (7, '2026-03-25', 5), 
    (10, '2026-03-26', 3) 
]

def crear_tabla_ventas():
    with sql.connect("catalogo_bisuteria.db") as conexion:
        cursor = conexion.cursor()
        
        comando = """CREATE TABLE ventas(
                        id_venta INTEGER PRIMARY KEY AUTOINCREMENT,
                        id_joya INTEGER,
                        fecha TEXT,
                        cantidad_vendida INTEGER
                )"""
        cursor.execute(comando)
        
        comando_insert = "INSERT INTO ventas (id_joya, fecha, cantidad_vendida) VALUES (?, ?, ?)"
        cursor.executemany(comando_insert, lote_ventas)

#-------------------------------------------------------------------------------------------------------


def joyas_mayor_al_promedio():
    with sql.connect("catalogo_bisuteria.db") as conexion:
        cursor = conexion.cursor()
        
        comando = """SELECT nombre, precio
                     FROM joyas
                     WHERE precio > (SELECT AVG(precio) FROM joyas)"""
        cursor.execute(comando)
        
        datos = cursor.fetchall()
        for dato in datos:
            print(dato)
            
#-------------------------------------------------------------------------------------------------------

def joyas_menor_al_promedio_plata():
    with sql.connect("catalogo_bisuteria.db") as conexion:
        cursor = conexion.cursor()
        
        comando = """SELECT nombre, precio
                     FROM joyas
                     WHERE material = 'Plata 925' AND precio < (SELECT MAX(precio) FROM joyas WHERE material = 'Plata 925')"""
                     
        cursor.execute(comando)
        
        datos = cursor.fetchall()
        for dato in datos:
            print(dato)
            
#-------------------------------------------------------------------------------------------------------

def joyas_sin_ventas():
    with sql.connect("catalogo_bisuteria.db") as conexion:
        cursor = conexion.cursor()
        
        comando = """SELECT nombre, stock
                     FROM joyas
                     WHERE id_joya NOT IN (SELECT id_joya FROM ventas)"""
        cursor.execute(comando)
        
        datos = cursor.fetchall()
        for dato in datos:
            print(dato)
            
#-------------------------------------------------------------------------------------------------------

def joyas_mas_caras_de_su_categoria():
    with sql.connect("catalogo_bisuteria.db") as conexion:
        cursor = conexion.cursor()
        
        comando = """SELECT nombre, precio, categoria
                     FROM joyas AS j1
                     WHERE precio > (SELECT AVG(precio) FROM joyas AS j2 WHERE j2.categoria = j1.categoria)"""
        cursor.execute(comando)
        
        datos = cursor.fetchall()
        for dato in datos:
            print(dato)
            
#-------------------------------------------------------------------------------------------------------

def capital_alto_riesgo():
    with sql.connect("catalogo_bisuteria.db") as conexion:
        cursor = conexion.cursor()
        
        comando = """SELECT categoria, SUM(precio * stock) as capital_inmovilizado
                     FROM joyas
                     WHERE precio > (SELECT AVG(precio) FROM joyas)
                     GROUP BY categoria
                     HAVING SUM(stock) > 3
                     ORDER BY capital_inmovilizado DESC"""
        cursor.execute(comando)
        
        datos = cursor.fetchall()
        for dato in datos:
            print(dato)
            
#-------------------------------------------------------------------------------------------------------

def stock_basura():
    with sql.connect("catalogo_bisuteria.db") as conexion:
        cursor = conexion.cursor()
        
        comando = """SELECT categoria, SUM(stock) as total_stock
                     FROM joyas
                     WHERE precio < (SELECT AVG(precio) FROM joyas)
                     GROUP BY categoria
                     HAVING total_stock > 10
                     ORDER BY total_stock DESC"""
        cursor.execute(comando)
        
        datos = cursor.fetchall()
        for dato in datos:
            print(dato)

#-------------------------------------------------------------------------------------------------------

def rentabilidad_por_categoria():
    with sql.connect("catalogo_bisuteria.db") as conexion:
        cursor = conexion.cursor()
        
        comando = """SELECT material, SUM(precio * stock) as capital_inmovilizado
                     FROM joyas
                     WHERE id_joya IN (SELECT id_joya FROM ventas)
                     GROUP BY material
                     ORDER BY capital_inmovilizado DESC"""
        cursor.execute(comando)
        
        datos = cursor.fetchall()
        for dato in datos:
            print(dato)
            
#-------------------------------------------------------------------------------------------------------

def benchmark_global():
    with sql.connect("catalogo_bisuteria.db") as conexion:
        cursor = conexion.cursor()
        
        comando = """SELECT categoria, AVG(precio) as precio_promedio
                     FROM joyas
                     GROUP BY categoria
                     HAVING precio_promedio > (SELECT AVG(precio) FROM joyas)
                     ORDER BY precio_promedio DESC"""
                     
        cursor.execute(comando)
        
        datos = cursor.fetchall()
        for dato in datos:
            print(dato)
            
#-------------------------------------------------------------------------------------------------------

def etiqueta_ultra_premium():
    with sql.connect("catalogo_bisuteria.db") as conexion:
        cursor = conexion.cursor()
        
        comando = """SELECT nombre, categoria, precio
                     FROM joyas
                     WHERE precio > (SELECT AVG(precio) *2 FROM joyas)
                     ORDER BY precio DESC"""
                     
        cursor.execute(comando)
        datos = cursor.fetchall()
        for dato in datos:
            print(dato)
            
def standar_oro():
    with sql.connect("catalogo_bisuteria.db") as conexion:
        cursor = conexion.cursor()
        
        comando = """SELECT categoria, SUM(stock)
                     FROM joyas
                     GROUP BY categoria
                     HAVING MIN(precio) > (SELECT AVG(precio) FROM joyas)"""
                     
        cursor.execute(comando)
        datos = cursor.fetchall()
        for dato in datos:
            print(dato)


if __name__ == "__main__":
    #modelos_menos_de_5()
    #rentabilidad_material()
    #dinero_inmovilizado()
    #crear_tabla_ventas()
    #joyas_mayor_al_promedio()
    #joyas_menor_al_promedio_plata()
    #joyas_sin_ventas()
    #joyas_mas_caras_de_su_categoria()
    #capital_alto_riesgo()
    #stock_basura()
    #rentabilidad_por_categoria()
    #benchmark_global()
    #etiqueta_ultra_premium()
    standar_oro()