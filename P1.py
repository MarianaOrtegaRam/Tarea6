def verify(T: set, C: set, x: int, X: set) -> bool:
    # Comprueba que para todas las intersecciones en C, hay al menos una cámara en X que cubre la calle.
    for c in C:
        f = False
        for n in X:
            if c[0] == n or c[1] == n:
                f = True
                break
        if not f:
            return False
    return len(X) <= x

from typing import Tuple, Set


T = {(0, 0), (1, 1), (2, 2), (3, 3)}  # Conjunto de intersecciones
C = {((0, 0), (1, 1)), ((1, 1), (2, 2)), ((2, 2), (3, 3))}  # Conjunto de calles
x = 3  # Cota de la cantidad de intersecciones permitidas
X = {(0, 0), (2, 2), (3, 3)}  # Conjunto de intersecciones donde se ubicarán cámaras

# Llamada a la función
result = verify(T, C, x, X)
print(result)  # Debería imprimir True si las cámaras cubren todas las calles y el tamaño de X <= x
