#Clase nodo: Define la estructura de datos a utilizar.
class Nodo:
    # Contructor, recibe tres argumentos:
    # - estado: Numero del estado dentro del arbol.
    # - es_final: Indica si el nodo es nodo hoja.
    # - descripcion: Descripcion del estado que ayuda a la interfaz.
    def __init__(self, estado, es_final, descripcion):
        self.visitado = False
        self.hijos = []
        self.estado = estado
        self.es_final = es_final
        self.descripcion = descripcion
    
    # agregaHijo: Agrega el nodo recibido como hijo
    # del nodo que invoco la funcion.
    def agregaHijo(self, hijo):
        if len(self.hijos) < 2:
            self.hijos.append(hijo)

    #obtenerHijos: Obtiene todos los hijos del nodo.
    def obtenerHijos(self):
        for hijo in self.hijos:
            print(hijo.estado)




