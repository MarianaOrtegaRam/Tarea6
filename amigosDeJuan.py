def ejes_cruzados(asignacion, ejes):
    cruzados = 0
    for u, v in ejes:
        if asignacion[u] != asignacion[v]:
            cruzados += 1
    return cruzados

def amigosJuan(nombres, conflictos):
    # Diccionarios para mapear nombres a índices y viceversa
    nombre_indice = {name: i for i, name in enumerate(nombres)}
    indice_nombre = {i: name for name, i in nombre_indice.items()}
    
    n = len(nombres)
    ejes = [(nombre_indice[u], nombre_indice[v]) for u, v in conflictos]
    asignacion = [0] * n
    
    # Cuenta de ejes cruzados iniciales
    max_cruzados = ejes_cruzados(asignacion, ejes)
    mejora = True
    
    while mejora:
        mejora = False
        for i in range(n):
            # Probar mover el vértice i al otro grupo
            grupo_original = asignacion[i]
            asignacion[i] = 1 - grupo_original
            nuevos_cruzados = ejes_cruzados(asignacion, ejes)
            
            # Si mejora, mantenemos el cambio; si no, revertimos
            if nuevos_cruzados > max_cruzados:
                max_cruzados = nuevos_cruzados
                mejora = True
            else:
                asignacion[i] = grupo_original
    
    group1 = [indice_nombre[i] for i in range(n) if asignacion[i] == 0]
    group2 = [indice_nombre[i] for i in range(n) if asignacion[i] == 1]
    
    return group1, group2


# Ejemplo de uso
amigos = ["Juan", "Pedro", "Maria", "Ana", "Luis"]
parejas_conflicto = [("Juan", "Pedro"), ("Juan", "Maria"), ("Pedro", "Ana"), ("Maria", "Luis"), ("Ana", "Luis")]

grupo1, grupo2 = amigosJuan(amigos, parejas_conflicto)
print("Grupo 1:", grupo1)
print("Grupo 2:", grupo2)
