def encontrar_minimo(arreglo):
    if not arreglo:
        return None, -1
    valor_min = min(arreglo)
    posicion_min = arreglo.index(min(arreglo))
    
    """valor_min  = arreglo[0]
    posicion_min = 0

    for posicion in range(1, len(arreglo)):
        if arreglo[posicion] < valor_min:
            valor_min = arreglo[posicion]
            posicion_min = posicion"""
    
    return valor_min, posicion_min



def eliminar_maximo(arreglo):
    if not arreglo:
        prinf("El arreglo esta vacio, nada por eliminar")
        return arreglo
    valor_max = max(arreglo)
    arreglo.remove(valor_max)
    print("Se a eliminado el valor {}".format(valor_max))
    return arreglo

def agregarValor_Final(arreglo, valor):
    if not arreglo:
        print("El arreglo esta vacio, nada por eliminar")
        return arreglo
    arreglo.append(valor)


if __name__ == "__main__":
    arreglo = [2.3, 5.1, 1.7, 2.1, 1.6, 2.9, 4.7, 5.0, 1.5, 1.4,2.2,2.4, 0.9]
    minimo, posicion = encontrar_minimo(arreglo)
    if minimo is not None:
        print("El valoer minimo es {} y su posicion es {}".format(minimo, posicion))
    else:
        print("La lista esta vacia")
    
    eliminar_maximo(arreglo)
    agregarValor_Final(arreglo, 88)
    
    for i in arreglo:
        print(i)
    
