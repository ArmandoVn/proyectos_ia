from estado import Estado
import copy, sys

# Genera los hijos de cada nuevo estado
def generaHijos(estado, posicionX, posicionY):
    hijos = []
    movimientos = [1,-1]
    for i in movimientos:
        _matriz = copy.deepcopy(estado.matrizNumeros)
        i+=posicionX
        if(i >= 0 and i <= 2):
            aux = _matriz[posicionY][i]
            _matriz[posicionY][i] = 0
            _matriz[posicionY][posicionX] = aux
            hijos.append(Estado(_matriz))
    for i in movimientos:
        _matriz = copy.deepcopy(estado.matrizNumeros)
        i+=posicionY
        if(i >= 0 and i <= 2):
            aux = _matriz[i][posicionX]
            _matriz[i][posicionX] = 0
            _matriz[posicionY][posicionX] = aux
            hijos.append(Estado(_matriz))
    return hijos

# Ordena los hijos de cada estado de mayor a menor para insertarlos en la pila.
def ordenaMayorAMenor(estados):
    contador = 1
    for x in range(0,len(estados)-1):
        for i in range(0,len(estados)-contador):
            if(estados[i].numerosFueraLugar < estados[i+1].numerosFueraLugar):
                aux = estados[i]
                estados[i] = estados[i+1]
                estados[i+1] = aux
        contador+=1
    return estados

# Ordena los hijos de cada estado de mayor a menor para insertarlos en la pila.
def ordenaMayorAMenor2(estados):
    contador = 1
    for x in range(0,len(estados)-1):
        for i in range(0,len(estados)-contador):
            if(estados[i].numerosFueraLugarCuentaPosiciones < estados[i+1].numerosFueraLugarCuentaPosiciones):
                aux = estados[i]
                estados[i] = estados[i+1]
                estados[i+1] = aux
        contador+=1
    return estados

# Si la matrz1 es igual a la mariz2 regresa True
def comparaMatrices(matriz1, matriz2):
    for i in range(0,3):
        for j in range(0,3):
            if(matriz1[i][j] != matriz2[i][j]):
                return False
    return True

# Si el nuevo estado ya fue visitado regresa True
def validaEstadosVisitados(estadosVisitados, estado):
    for x in estadosVisitados:
        if(comparaMatrices(x.matrizNumeros, estado.matrizNumeros)):
            return True
    return False

# Valida que el estado pasado como argumento no sea estado final y
# valida que el estado pasado como argumeno no haya sido visitado antes,
# en caso de no cumplir con las dos anteriores el nuevo estado se agregara
# al cola de estados visitados y se le cargara la ruta que tuvo que seguir
# para llegar al estado actual.
def busquedaEnProfundidad(pilaEstados, estadosVisitados, estado):
    if(not estado.validaEstadoFinal()):
        if(not validaEstadosVisitados(estadosVisitados, estado)):
            estadosVisitados.append(estado)
            posicionX, posicionY = estado.encuentraNumero(0)
            hijos = ordenaMayorAMenor2(generaHijos(estado, posicionX, posicionY))
            aux = hijos[:]
            for i in range(0, len(aux)-1):
                if(validaEstadosVisitados(estadosVisitados, aux[i])):
                   hijos.pop(i)
            for i in hijos:
                i.padre = estado
            pilaEstados+=hijos
            return pilaEstados, estadosVisitados, None
        else:
            return pilaEstados, estadosVisitados, None
    else:
        return [], estadosVisitados, estado

def generaRuta(estado, ruta): 
    while estado.padre != None:
        ruta.append(estado)
        estado = estado.padre
    ruta.append(estado)

def imprimeRuta(ruta):
    while len(ruta) > 0:
        if len(ruta) == 1:
            print("¡Solucion!")
        ruta.pop().imprimeCuadro()

def main():
    pilaEstados = []
    estadosVisitados = []
    estadoFinal = None
    ruta = []
    #estadoInicial = Estado([[1,2,3],[4,5,6],[7,8,0]])
    #estadoInicial = Estado([[1,2,3],[4,5,6],[0,7,8]])
    #estadoInicial = Estado([[1,2,3],[0,5,6],[4,7,8]])
    #estadoInicial = Estado([[4,0,7],[8,1,5],[6,3,2]])
    estadoInicial = Estado([[5,7,2],[0,6,8],[1,3,4]])
    pilaEstados.append(estadoInicial)
    while (len(pilaEstados)>0):
        e1 = pilaEstados.pop()
        pilaEstados, estadosVisitados, estadoFinal = busquedaEnProfundidad(pilaEstados, estadosVisitados, e1)
    
    if(estadoFinal != None):
        generaRuta(estadoFinal, ruta)
        hijos = len(ruta)
        imprimeRuta(ruta)
        print(hijos)

main()



