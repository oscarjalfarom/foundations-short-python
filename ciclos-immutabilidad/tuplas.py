#!/usr/bin/python3

from typing import Any, Tuple

mi_tupla: Tuple[Any] = (1, 2, 3, 'a', 'b')
mi_tupla: Tuple[Union[int, str]] = (1, 2, 3, 'a', 'b')

for a in mi_tupla:
  print(a)
