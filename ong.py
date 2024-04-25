def fact_i(n):
    """
    Calcula el factorial de un número dado.

    Args:
    - n (int): Número para calcular el factorial.

    Returns:
    - int: Factorial de n.
    """
    # Inicializamos el resultado como 1
    result = 1
    # Iteramos desde 1 hasta n, multiplicando cada número
    # al resultado para calcular el factorial
    for i in range(1, n + 1):
        result *= i
    return result

def pro_i(lista):
    """
    Calcula la productoria de una lista de números.

    Args:
    - lista (list): Lista de números para calcular la productoria.

    Returns:
    - int: Productoria de los números en la lista.
    """
    # Inicializamos el resultado como 1
    result = 1
    # Iteramos sobre cada número en la lista, multiplicándolo
    # al resultado para calcular la productoria
    for num in lista:
        result *= num
    return result

def calcular(*args):
    """
    Controla los cálculos de factorial y productoria.

    Args:
    - args (tuple): Tupla de argumentos para los cálculos.
    """
    # Iteramos sobre cada argumento recibido
    for arg in args:
        # Si el argumento es un entero, calculamos su factorial
        if isinstance(arg, int):
            print(f"El factorial de {arg} es {fact_i(arg)}")
        # Si el argumento es una lista, calculamos su productoria
        elif isinstance(arg, list):
            print(f"La productoria de {arg} es {pro_i(arg)}")
        else:
            # Si el argumento no es ni un entero ni una lista,
            # mostramos un mensaje de error
            print("Argumento no reconocido:", arg)

# Ejemplo de uso
calcular(5, [4, 6, 7, 4, 3], 6)