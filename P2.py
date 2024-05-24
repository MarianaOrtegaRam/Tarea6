def verify(D, P, R, x, X):
    """
    Verifica si se cumplen las condiciones dadas.
    
    Parámetros:
    D: Conjunto de días
    P: Conjunto de personas
    R: Relación (diccionario) de personas a días
    x: Entero que representa la cantidad máxima permitida de días en X
    X: Conjunto de días a verificar

    Retorno:
    booleano que indica si se cumplen las condiciones
    """
    # Verificar si el tamaño de X es menor o igual a x
    b = len(X) <= x
    
    # Verificar si todos los elementos de X están en D
    for d in X:
        b = b or d in D
    
    # Verificar que cada persona tenga al menos un día de X en la relación R
    for p in P:
        cp = False
        for d in X:
            cp = cp or (p, d) in R
        b = b and cp
    
    return b
