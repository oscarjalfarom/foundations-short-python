from typing import Tuple, Union

def quick_sort(tupla: Tuple[Union[int, str]]) -> Tuple[Union[int, str]]:
    """
    Implementa el algoritmo Quick Sort en una tupla.
    
    Args:
        tupla (Tuple): La tupla que se desea ordenar.
        
    Returns:
        Tuple: La tupla ordenada.
    """
    if len(tupla) == 0:
        return ()

    right: Tuple[Union[int, str]] = ()
    left: Tuple[Union[int, str]] = ()
    pivot: Union[int, str] = tupla[0]

 
    for i in range(1, len(tupla)):
        if tupla[i] < pivot:
            left += (tupla[i],)
        else:
            right += (tupla[i],)
    
    # tupla_ordenada = (quick_sort(left) + (pivot,) + quick_sort(right))
    return (quick_sort(left) + (pivot,) + quick_sort(right))

# Ejemplo de uso 1: Ordenamiento de una tupla de enteros
datos: Tuple[int] = (5, 1, 8, 3, 2)
datos_ordenados: Tuple[int] = quick_sort(datos)
print(f"Tupla ordenada: {datos_ordenados}")
# Salida esperada: "Tupla ordenada: (1, 2, 3, 5, 8)"

# Ejemplo de uso 2: Ordenamiento de una tupla de cadenas
nombres: Tuple[int] = ("Alice", "Bob", "Charlie", "David")
nombres_ordenados: Tuple[int] = quick_sort(nombres)
print(f"Tupla ordenada: {nombres_ordenados}")
# Salida esperada: "Tupla ordenada: ('Alice', 'Bob', 'Charlie', 'David')"

# Ejemplo de uso 3: Ordenamiento de una tupla vacia
datos: Tuple[int] = ()
datos_ordenados: Tuple[int] = quick_sort(datos)
print(f"Tupla ordenada: {datos_ordenados}")
# Salida esperada: "Tupla ordenada: ()"
