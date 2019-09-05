class Estado:
    def __init__(self, matrizNumeros):
        self.matrizNumeros = matrizNumeros
        self.__numerosFueraDeLugar()
        self.ruta = []

    def imprimeCuadro(self):
        print(self.matrizNumeros[0])
        print(self.matrizNumeros[1])
        print(self.matrizNumeros[2],'\n')

    def __numerosFueraDeLugar(self):
        self.numerosFueraLugar = 0
        estadoFinal = [[1,2,3],[4,5,6],[7,8,0]]
        for i in range(0,3):
            for j in range(0,3):
                if(estadoFinal[i][j] != self.matrizNumeros[i][j]):
                    self.numerosFueraLugar+=1

    def imprimeRuta(self):
        for estado in self.ruta:
            estado.imprimeCuadro()






