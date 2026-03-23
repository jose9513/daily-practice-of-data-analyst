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