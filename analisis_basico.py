"""
Repaso de Python para análisis de datos
Data Science II: Machine Learning para la Ciencia de Datos - Coderhouse
Autor: Matías Rodríguez
"""

# ---------------------------------------------------------------
# Tarea 1: Definición de variables
# Se definen los datos básicos de un producto con distintos tipos.
# ---------------------------------------------------------------
nombre_producto = "Notebook Lenovo IdeaPad"   # str
precio_producto = 899.99                      # float
stock_producto = 25                           # int
tiene_descuento = True                        # bool

# Resumen del producto usando f-strings
print(
    f"Producto: {nombre_producto} | Precio: ${precio_producto:.2f} | "
    f"Stock: {stock_producto} unidades | Descuento disponible: {tiene_descuento}"
)

# ---------------------------------------------------------------
# Tarea 2: Lógica de negocio (bucle + condicional)
# Se clasifica cada precio como "Caro" (> 100) o "Económico" (<= 100).
# ---------------------------------------------------------------
precios = [45.50, 120.00, 99.99, 250.75, 100.00, 15.30]

for precio in precios:
    if precio > 100:
        print(f"${precio:.2f} -> Caro")
    else:
        print(f"${precio:.2f} -> Económico")

# ---------------------------------------------------------------
# Tarea 3: Estructura de datos compleja (diccionario)
# Las llaves son nombres de productos y los valores, su stock.
# ---------------------------------------------------------------
almacen = {
    "Mouse": 150,
    "Teclado": 80,
    "Monitor": 35,
    "Auriculares": 60,
}

# Se agrega un nuevo producto al diccionario
almacen["Webcam"] = 40

# Se consulta el stock de un producto específico
producto_consultado = "Monitor"
print(f"Stock de {producto_consultado}: {almacen[producto_consultado]} unidades")
print(f"Almacén actualizado: {almacen}")


# ---------------------------------------------------------------
# Tarea 4: Modularización con funciones
# Recibe una lista de números y devuelve suma, promedio y cantidad.
# ---------------------------------------------------------------
def resumen_estadistico(numeros):
    """Devuelve un diccionario con la suma total, el promedio y la cantidad de elementos."""
    cantidad = len(numeros)
    suma_total = sum(numeros)
    promedio = suma_total / cantidad if cantidad > 0 else 0
    return {
        "suma": suma_total,
        "promedio": promedio,
        "cantidad": cantidad,
    }


# Llamada de ejemplo a la función e impresión del resultado
resultado = resumen_estadistico([10, 20, 30])
print(f"Resumen estadístico: {resultado}")

# También se aplica sobre la lista de precios
print(f"Resumen de precios: {resumen_estadistico(precios)}")
