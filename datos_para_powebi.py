import sqlite3 as sql
import csv

import random
from datetime import datetime, timedelta

def exportar_datos_para_bi():
    #Conectar a la base de datos
    conn = sql.connect('catalogo_bisuteria.db')
    with conn:
        cursor = conn.cursor()
        #ejecutar la consulta para obtener los datos
        cursor.execute("""SELECT * FROM joyas""")
        datos_joyas = cursor.fetchall()
        columnas_joyas = [descripcion[0] for descripcion in cursor.description]
        
        #Exportar los datos a un archivo CSV
        with open('datos_joyas.csv', 'w', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f)
            #Escribir los encabezados
            escritor.writerow(columnas_joyas)
            #Escribir los datos
            escritor.writerows(datos_joyas)
            
        print("Datos de joyas exportados correctamente a datos_joyas.csv")
            
        cursor.execute("""SELECT * FROM ventas""")
        datos_ventas = cursor.fetchall()
        columnas_ventas = [descripcion[0] for descripcion in cursor.description]
        
        #exportar los datos de las ventas a un archivo CSV
        with open('datos_ventas.csv', 'w', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f)
            #Escribir los encabezados
            escritor.writerow(columnas_ventas)
            #Escribir los datos
            escritor.writerows(datos_ventas)
            
        print("Datos de ventas exportados correctamente a datos_ventas.csv")
        
#-----------------------------------------------------------------------------------------------------------

def crear_ventas_hisoticas(cantidad_ventas=500):
    #conectar a la base de datos
    conn = sql.connect('catalogo_bisuteria.db')
    with conn:
        cursor = conn.cursor()
        #ejecutar la consulta para obtener los datos de las ventas
        cursor.execute("""SELECT id_joyas FROM joyas WHERE stock > 0""")
        joyas_disponibles = [fila[0] for fila in cursor.fetchall()]
        
        if not joyas_disponibles:
            print("No hay joyas disponibles para generar ventas históricas.")
            return
        fecha_inicio = datetime.now() - timedelta(days=180)
        
        cursor.execute("""BEGIN TRANSACTION""")
        venteas_creadas = 0
        for _  in range(cantidad_ventas):
            id_elegido = random.choice(joyas_disponibles)
            cantidad_comprada = random.randint(1, 3)
            
            # Generar una fecha aleatoria dentro de los últimos 6 meses
            dias_aleatorios = random.randint(0, 180)
            fecha_venta = fecha_inicio + timedelta(days=dias_aleatorios)
            fecha_str = fecha_venta.strftime("%Y-%m-%d %H:%M:%S")
            
            # Ejecutamos el insert de forma segura
            cursor.execute("""
                INSERT INTO ventas (id_joya, cantidad, fecha) 
                VALUES (?, ?, ?)
            """, (id_elegido, cantidad_comprada, fecha_str))
            
            ventas_creadas += 1
            
        # 4. Sellamos la bóveda con los 500 registros nuevos
        conn.commit()
        
        print(f"¡Éxito! Se han inyectado {ventas_creadas} ventas simuladas en la base de datos.")
        
if __name__ == "__main__":
    exportar_datos_para_bi()