class Estado:

    numerosFueraLugar = 0
    numerosFueraLugarCuentaPosiciones = 0

    def __init__(self, matrizNumeros):
        self.matrizNumeros = matrizNumeros
        self.__numerosFueraDeLugar()
        self.__numerosFueraLugarCuentaPosiciones()
        self.padre = None

    def imprimeCuadro(self):
        print(self.matrizNumeros[0])
        print(self.matrizNumeros[1])
        print(self.matrizNumeros[2],'\n')

    # Numeros fuera de lugar.
    ##estadoInicial = Estado([[0,1,2],[3,4,5],[6,7,8]])
    ##estadoInicial = Estado([[0,2,7],[6,5,4],[3,8,1]])
    def __numerosFueraDeLugar(self):
        estadoFinal = [[1,2,3],[4,5,6],[7,8,0]]
        for i in range(0,3):
            for j in range(0,3):
                if(estadoFinal[i][j] != self.matrizNumeros[i][j]):
                    self.numerosFueraLugar+=1

    def __numerosFueraLugarCuentaPosiciones(self):
        posicionesFinales = [[0,0],[1,0],[2,0],[0,1],[1,1],[2,1],[0,2],[1,2],[2,2]]
        posicionesActuales = self.__encuentraPosicionesNumeros()
        for i in range(0,8):
            for j in range(0,2):
                self.numerosFueraLugarCuentaPosiciones += abs(posicionesActuales[i][j]-posicionesFinales[i][j])

    def __encuentraPosicionesNumeros(self):
        posicionesActuales = []
        for i in range(1,9):
            posicionesActuales.append(list(self.encuentraNumero(i)))
        return posicionesActuales

    # Encuentra la posicion X y Y del "numero" en el tablero.
    def encuentraNumero(self, numero):
        posicionY = 0
        for i in range(0,3):
            posicionX = 0
            for j in range(0,3):
                if(self.matrizNumeros[i][j] == numero):
                    return posicionX, posicionY
                posicionX+=1
            posicionY+=1

    # Regresa true si es un estado final
    def validaEstadoFinal(self):
        if self.numerosFueraLugar == 0:
            return True
        return False



