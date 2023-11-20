from typing import Tuple, Union

def busqueda_lineal(tupla: Tuple[Union[int, str]], objetivo: Union[int, str]) -> int:
    """
    Realiza una búsqueda lineal en la tupla para encontrar el objetivo.
    
    Args:
        tupla (Tuple): La tupla en la que se realizará la búsqueda.
        objetivo (Union[int, str]): El elemento que se busca en la tupla.
        
    Returns:
        int: El índice del objetivo si se encuentra, o -1 si no se encuentra.
    """
    # Implementa la búsqueda lineal aquí
    indice: int = 0
    for indice, elemento in enumerate(tupla):
        if elemento == objetivo:
            return indice
    return -1

# Ejemplo de uso
datos: Tuple[int] = (5, 1, 8, 3, 2)
indice: int = busqueda_lineal(datos, 3)
print(f"El valor 3 se encontró en el índice {indice}.")

# Ejemplo de uso 1: Elemento encontrado
datos: Tuple[int] = (5, 1, 8, 3, 2)
indice: int = busqueda_lineal(datos, 3)
print(f"El valor 3 se encontró en el índice {indice}.")
# Salida esperada: "El valor 3 se encontró en el índice 3."

# Ejemplo de uso 2: Elemento no encontrado
datos: Tuple[int] = (5, 1, 8, 3, 2)
indice: int = busqueda_lineal(datos, 6)
print(f"El valor 6 se encontró en el índice {indice}.")
# Salida esperada: "El valor 6 se encontró en el índice -1."

# Ejemplo de uso 3: Búsqueda en una tupla de cadenas
nombres: Tuple[str] = ("Alice", "Bob", "Charlie", "David")
indice: int = busqueda_lineal(nombres, "Charlie")
print(f"El nombre 'Charlie' se encontró en el índice {indice}.")
# Salida esperada: "El nombre 'Charlie' se encontró en el índice 2."
