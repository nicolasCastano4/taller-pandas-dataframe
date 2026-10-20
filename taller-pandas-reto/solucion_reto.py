import pandas as pd

# 1. Configuración del DataFrame inicial con las correcciones de sintaxis
datos = {
    "producto": [
        "Cuaderno", "lapicera", "mochila", "Regla", "Cartuchera",
        "Calculadora", "Auriculares", "Resaltadores", "Goma", "Lapiz"
    ],
    "categoria": [
        "Libreria", "libreria", "Accesorios", "Libreria", "accesorios",
        "Tecnologia", "tecnologia", "Libreria ", "Indumentaria", "libreria"
    ],
    "precio": [2500, 1200, 15000, 800, 4500, 18000, 22000, 3000, 500, 900],
    "cantidad_vendida": [25, 40, 7, 12, 15, 5, 8, 30, 50, 22],
    "sucursal": [
        "Centro", "Centro", "Norte", "Sur", "Norte",
        "Centro", "Sur", "Centro", "Sur", "Centro"
    ],
    "forma_pago": [
        "Efectivo", "debito", "Credito", "Efectivo", "Debito",
        "credito", "Credito", "Debito", "Efectivo", "debito"
    ],
    "fecha": [
        "2024-03-01", "2024-03-01", "2024-03-02", "2024-03-02", "2024-03-03",
        "2024-03-03", "2024-03-04", "2024-03-04", "2024-03-05", "2024-03-05"
    ]
}

df = pd.DataFrame(datos)

# Pre-limpieza de la categoría
reemplazos_categoria = {
    'libreria': 'Libreria',
    'accesorios': 'Accesorios',
    'tecnologia': 'Tecnologia',
    'indumentaria': 'Indumentaria'
}
df['categoria_limpia'] = df['categoria'].str.strip().str.lower().replace(reemplazos_categoria)

# =========================================================
# SOLUCIÓN DEL RETO PRÁCTICO INTEGRADOR
# =========================================================

# Punto 1: Normalización de la columna forma_pago
df['forma_pago_estandarizada'] = df['forma_pago'].str.strip().str.lower()

# Punto 2: Filtrado Compuesto (múltiples condiciones con &)
condicion_categoria = df['categoria_limpia'] == 'Libreria'
condicion_pago = df['forma_pago_estandarizada'] == 'debito'
condicion_cantidad = df['cantidad_vendida'] >= 20

mascara_reto = condicion_categoria & condicion_pago & condicion_cantidad

# Punto 3: Proyección Tabular (DataFrame)
resultado_final = df[mascara_reto][['producto', 'precio', 'sucursal']]

# Punto 4: Auditoría de Dimensiones y Muestra de Resultados
print("=" * 45)
print("   RESULTADO DEL RETO PRÁCTICO INTEGRADOR")
print("=" * 45)
print("\n[DataFrame Resultante]:")
print(resultado_final)

print("\n--- AUDITORÍA ---")
print("Tipo del objeto resultado_final:", type(resultado_final))
print("Dimensiones finales (filas, columnas):", resultado_final.shape)
