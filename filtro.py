import sys

# Diccionario de precios de productos
precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
}

# Obtener el umbral del primer argumento de la línea de comandos
umbral = int(sys.argv[1])

# Si se proporciona un segundo argumento en la línea de comandos, 
# establecer la operación según ese argumento, de lo contrario, 
# la operación predeterminada es 'mayor'
if len(sys.argv) == 3:
    operacion = sys.argv[2].lower()
else:
    operacion = 'mayor'

# Lista para almacenar los productos que cumplen con la condición especificada
productos_filtrados = []

# Iterar sobre los productos y precios para filtrar aquellos que cumplen con la condición especificada
for producto, precio in precios.items():
    if (operacion == 'mayor' and precio > umbral) or (operacion == 'menor' and precio < umbral):
        productos_filtrados.append(producto)

# Si hay productos que cumplen con la condición, imprimirlos; 
# de lo contrario, imprimir un mensaje de error
if productos_filtrados:
    print("Los productos", operacion, "al umbral son:", ', '.join(productos_filtrados))
else:
    print("Lo sentimos, no es una operación válida")


# py filtro.py 30000