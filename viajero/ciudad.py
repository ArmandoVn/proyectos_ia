class Ciudad:
    def __init__(self, numero_ciudad):
        self.numero_ciudad =  numero_ciudad
        self.hijos = []

    def agregarConexionCiudad(self, ciudad, distancia, euristica):
        self.hijos.append([ciudad, distancia, euristica])
        #self.ordenaMayorAMenorEuristica()
        self.ordenaMayorAMenorAmbas()

    def ordenaMayorAMenorEuristica(self):
        contador = 1
        for x in range(0, len(self.hijos)-1):
            for i in range(0, len(self.hijos)-contador):
                if(self.hijos[i][2] < self.hijos[i+1][2]):
                    aux = self.hijos[i]
                    self.hijos[i] = self.hijos[i+1]
                    self.hijos[i+1] = aux

    def ordenaMayorAMenorAmbas(self):
        contador = 1
        for x in range(0, len(self.hijos)-1):
            for i in range(0, len(self.hijos)-contador):
                if((self.hijos[i][1]+self.hijos[i][2]) < (self.hijos[i+1][1]+self.hijos[i+1][2])):
                    aux = self.hijos[i]
                    self.hijos[i] = self.hijos[i+1]
                    self.hijos[i+1] = aux

    def imprimeHijos(self):
        for i in range(0,len(self.hijos)):
            print(self.hijos[i][0].numero_ciudad)
        print()
