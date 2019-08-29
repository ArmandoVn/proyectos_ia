from cargaInicial import arbol

# Realiza una busqueda dentro del arreglo arbol
# para obtener el nodo incial.
def encuentraNodo(estado_inicial):
    for nodo in arbol:
        if estado_inicial == nodo.estado:
            return nodo

# Lista todos los nodos que conforman el arbol.
def listaArbol(arbol):
    contador = 0
    for nodo in arbol: 
        contador += 1
        print("Estado : " + str(contador))
        nodo.obtenerHijos()

# Realiza la busqueda en profundidad dentro del arbol.
# El algoritmo funciona de la siguiente manera:
#   Ingresa a un nodo incial, comprueba si ya ha sido visitado
#   si el nodo no ha sido visitado lo marca como visitado,
#   imprime el estado actual y valida si el nodo actual tiene
#   hijos, en caso de tener accede al nodo de la izqueirda y
#   se vuelve a llamar la funcion (bfs), si el nodo no tiene
#   hijos y es final se regresa.
def bfs(nodo):
    if nodo.visitado != True:
        nodo.visitado = True
        print(nodo.descripcion)
        if len(nodo.hijos) != 0:
            bfs(nodo.hijos.pop(0))
        if nodo.es_final == True:
            return

#   Funcion main que solicita un estado inicial.
def main():
    print("#############################################\n")
    print("#        Problema de la aspiradora          #")
    print("\n#############################################\n")
    print("Indique el estado inicial seleccionando un numero:")
    print("Los valores dentro del parentesis indican lo siguiente:\n")
    print("( cuarto izquerdo, cuarto derecho, posicion aspiradora )\n")
    print("1.- ( sucio, sucio, izquierda )")
    print("2.- ( sucio, sucio, derecha )")
    print("3.- ( limpio, sucio, izquierda )")
    print("4.- ( limpio, sucio, derecha )")
    print("5.- ( sucio, limpio, izquierda )")
    print("6.- ( sucio, limpio, derecha )")
    print("7.- ( limpio, limpio, izquierda )")
    print("8.- ( limpio, limpio, derecha )")
    estado_inicial = int(input())
    print("\nEl recorrido del arbol es:\n")
    bfs(encuentraNodo(estado_inicial))

main()




