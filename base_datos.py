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


import sqlite3

def auditar_inventario():
    print("Iniciando sistema de inventario...")
    
    with sqlite3.connect("artemisa_core.db") as conexion:
        cursor = conexion.cursor()
        
        # 1. ARQUITECTURA (Destruimos y reconstruimos para pruebas limpias)
        cursor.execute("DROP TABLE IF EXISTS productos")
        
        cursor.execute('''
            CREATE TABLE productos (
                id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                categoria TEXT,
                precio REAL,
                stock INTEGER
            )
        ''')
        
        # 2. INYECCIÓN MASIVA (Omitimos el ID para que SQLite lo genere)
        lote_joyas = [
            ("Collar de Cuarzo Rosa", "Collares", 85.50, 15),
            ("Anillo de Plata 925", "Anillos", 120.00, 4),   # Stock crítico
            ("Pulsera de Amatista", "Pulseras", 45.00, 20),
            ("Pendientes de Perla", "Aretes", 65.00, 2),     # Stock crítico
            ("Cadena de Oro 18k", "Collares", 350.00, 8)     # Stock bajo
        ]
        
        comando_insert = "INSERT INTO productos (nombre, categoria, precio, stock) VALUES (?, ?, ?, ?)"
        cursor.executemany(comando_insert, lote_joyas)
        print(f"📦 Se inyectaron {cursor.rowcount} productos en la bóveda.")
        
        # 3. INTELIGENCIA DE NEGOCIO (El valor para la empresa)
        # Queremos que el bot nos avise qué productos están a punto de agotarse
        consulta_alerta = '''
            SELECT nombre, stock 
            FROM productos 
            WHERE stock < 10 
            ORDER BY stock ASC
        '''
        
        cursor.execute(consulta_alerta)
        alertas = cursor.fetchall()
        
        # 4. REPORTE EJECUTIVO EN TERMINAL
        print("\n" + "=" * 55)
        print("🚨 ALERTA AUTOMÁTICA: PRODUCTOS CON STOCK CRÍTICO (< 10)")
        print("=" * 55)
        
        for item in alertas:
            # item[0] es el nombre, item[1] es el stock
            print(f"⚠️ Reabastecer urgente: {item[0]:<25} | Quedan: {item[1]} unidades")

# La Regla de Oro: Solo se ejecuta si le damos "Play" a este archivo
if __name__ == "__main__":
    auditar_inventario()