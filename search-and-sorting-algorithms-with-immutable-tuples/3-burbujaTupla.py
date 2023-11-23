from typing import Tuple, Union

def ordenamiento_burbuja(tupla: Tuple[Union[str, int]]) -> Tuple[Union[str, int]]:
    """
    Implementa el algoritmo de ordenamiento de burbuja en una tupla.
    
    Args:
        tupla (Tuple): La tupla que se desea ordenar.
        
    Returns:
        Tuple: La tupla ordenada.
    """
    lista: List[Union[int, str]] = list(tupla)
    longi: int = len(lista)
    for i in range(longi - 1):
        for j in range(0, longi - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
  
    return tuple(lista)

# Ejemplo de uso
datos: Tuple[int] = (5, 1, 8, 3, 2)
datos_ordenados: Tuple[int] = ordenamiento_burbuja(datos)
print(f"Tupla ordenada: {datos_ordenados}")
# Salida esperada: "Tupla ordenada: (1, 2, 3, 5, 8)"

# Ejemplo de uso 2: Ordenamiento de una tupla de cadenas
nombres: Tuple[str] = ("Alice", "Bob", "Charlie", "David")
nombres_ordenados: Tuple[str] = ordenamiento_burbuja(nombres)
print(f"Tupla ordenada: {nombres_ordenados}")
# Salida esperada: "Tupla ordenada: ('Alice', 'Bob', 'Charlie', 'David')"
