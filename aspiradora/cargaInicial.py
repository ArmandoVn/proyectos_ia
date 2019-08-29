# Este archivo realiza la carga inicial del arbol
# previamente definido en clase.
from nodo import Nodo

nodo1 = Nodo(1, False, "( sucio, sucio, izquierda )")
nodo2 = Nodo(2, False, "( sucio, sucio, derecha )")
nodo3 = Nodo(3, False, "( limpio, sucio, izquierda )")
nodo4 = Nodo(4, False, "( limpio, sucio, derecha )")
nodo5 = Nodo(5, False, "( sucio, limpio, izquierda )")
nodo6 = Nodo(6, False, "( sucio, limpio, derecha )")
nodo7 = Nodo(7, True, "( limpio, limpio, izquierda )")
nodo8 = Nodo(8, True, "( limpio, limpio, derecha )")

# Agregamos los nodos hijo de cada nodo.
nodo1.agregaHijo(nodo3)
nodo1.agregaHijo(nodo2)
nodo2.agregaHijo(nodo6)
nodo2.agregaHijo(nodo1)
nodo3.agregaHijo(nodo4)
nodo4.agregaHijo(nodo8)
nodo4.agregaHijo(nodo3)
nodo5.agregaHijo(nodo7)
nodo5.agregaHijo(nodo6)
nodo6.agregaHijo(nodo5)
nodo7.agregaHijo(nodo8)
nodo8.agregaHijo(nodo7)

# Utilzamos un arreglo con todos los nodos del arbol
# para identificar mas rapido el estado inicial
arbol = [nodo1, nodo2, nodo3, nodo4, nodo5, nodo6, nodo7, nodo8]


    