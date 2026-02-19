ventas_del_dia = [
    {"cliente": "Jose", "monto": 150, "pago_exitoso": True},
    {"cliente": "Maria", "monto": 300, "pago_exitoso": False},
    {"cliente": "Luis", "monto": 50, "pago_exitoso": True},
    {"cliente": "Ana", "monto": 200, "pago_exitoso": False}
]

total_ganado = 0
ventas_fallidas = 0

print("--- PROCESANDO VENTAS ---")

for venta in ventas_del_dia:
    if venta["pago_exitoso"] == True:
        print(f"✅ Procesando pago de {venta['cliente']} por ${venta['monto']}")
        total_ganado = total_ganado + venta["monto"]
    else:
        print(f"❌ Error en el pago de {venta['cliente']}. Ignorando...")
        ventas_fallidas = ventas_fallidas + 1
        
print(f"--- TOTAL EN CAJA: ${total_ganado} ---")
print(f"--- VENTAS FALLIDAS: {ventas_fallidas} ---")