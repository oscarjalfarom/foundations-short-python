from typing import Tuple, Union

def busqueda_binaria(tupla: Tuple[Union[int, str]], objetivo: Union[int, str]) -> int:
    """
    Realiza una búsqueda binaria en la tupla para encontrar el objetivo.
    
    Args:
        tupla (Tuple): La tupla ordenada en la que se realizará la búsqueda.
        objetivo (Any): El elemento que se busca en la tupla.
        
    Returns:
        int: El índice del objetivo si se encuentra, o -1 si no se encuentra.
    """
    izquierda: int = 0
    derecha: int = len(tupla) -1

    while izquierda <= derecha:
        medio: int = (izquierda + derecha) // 2
        valor_medio: int = tupla[medio]
        if valor_medio == objetivo:
            return medio
        elif valor_medio < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1

# Ejemplo de uso
datos: Tuple[int] = (1, 2, 3, 5, 8)
indice: int = busqueda_binaria(datos, 5)
print(f"El valor 5 se encontró en el índice {indice}.")

# Ejemplo de uso 1: Elemento encontrado en una tupla ordenada
datos: Tuple[int] = (1, 2, 3, 5, 8)
indice: int = busqueda_binaria(datos, 5)
print(f"El valor 5 se encontró en el índice {indice}.")
# Salida esperada: "El valor 5 se encontró en el índice 3."

# Ejemplo de uso 2: Elemento no encontrado en una tupla ordenada
datos: Tuple[int] = (1, 2, 3, 5, 8)
indice: int = busqueda_binaria(datos, 6)
print(f"El valor 6 se encontró en el índice {indice}.")
# Salida esperada: "El valor 6 se encontró en el índice -1."

# Ejemplo de uso 3: Búsqueda en una tupla de cadenas ordenada alfabéticamente
nombres: Tuple[str] = ("Alice", "Bob", "Charlie", "David", "Eva")
indice: int = busqueda_binaria(nombres, "Eva")
print(f"El nombre 'Eva' se encontró en el índice {indice}.")
# Salida esperada: "El nombre 'Eva' se encontró en el índice 4."
