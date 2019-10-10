from ciudad import Ciudad

# Realiza la busqueda de una sola ciudad en la
def buscaCiudad(ruta, ciudad):
    for i in range(0, len(ruta)):
        if ruta[i] == ciudad:
            return True
    return False

def contieneTodasLasCiudades(ruta, ciudadesAVisitar):
    for i in range(0, len(ciudadesAVisitar)):
        if not buscaCiudad(ruta, ciudadesAVisitar[i]):
            return False
    return True

# def generaRuta(ciudad, ruta, ciudadesAVisitar):
#     ruta.append(ciudad.numero_ciudad)
#     if len(ciudad.hijos) > 0:
#         if contieneTodasLasCiudades(ruta, ciudadesAVisitar):
#             return ruta
#         generaRuta(ciudad.hijos.pop(0)[0], ruta, ciudadesAVisitar)
#     return ruta

def existeCiudadQueDeseoVisitar(ciudades, ciudadesAVisitar):
    for i in range(0, len(ciudadesAVisitar)):
        for j in range(0, len(ciudades)):
            if ciudadesAVisitar[i] == ciudades[j][0].numero_ciudad:
                aux = ciudades.pop(j)
                ciudades.append(aux)
                return ciudades
    return ciudades

def recorreEnProfundida(ciudad, ruta, ciudadesPorVisitar, ciudadesAVisitar):
    ruta.append(ciudad.numero_ciudad)
    if not contieneTodasLasCiudades(ruta, ciudadesAVisitar):
        # ciudadesPorVisitar += existeCiudadQueDeseoVisitar(ciudad.hijos, ciudadesAVisitar)
        ciudadesPorVisitar += ciudad.hijos
        # for i in range(0, len(ciudadesPorVisitar)):
        #     print(ciudadesPorVisitar[i][0].numero_ciudad)
        # print()
        ciudad.hijos = []
        return ruta, ciudadesPorVisitar 
    else:
        return ruta, []

def imprimeRuta(ruta):
    for i in range(0, len(ruta)):
        print(ruta[i])

def main():
    ciudadesPorVisitar = []
    ruta = []
    #ciudadesAVisitar = [5]
    #ciudadesAVisitar = [2,3]
    #ciudadesAVisitar = [2,5]
    #ciudadesAVisitar = [4,3,5]
    ciudadesAVisitar = [3]

    ciudad1 = Ciudad(1)
    ciudad2 = Ciudad(2)
    ciudad3 = Ciudad(3)
    ciudad4 = Ciudad(4)
    ciudad5 = Ciudad(5)
    
    # AgregaConexionCiudad recibe 3 argumentos, la ciudad, la distancia y la euristica
    ciudad1.agregarConexionCiudad(ciudad2,2,1)
    ciudad1.agregarConexionCiudad(ciudad3,3,2)
    ciudad1.agregarConexionCiudad(ciudad4,1,3)
    ciudad2.agregarConexionCiudad(ciudad1,2,1)
    ciudad2.agregarConexionCiudad(ciudad3,1,2)
    ciudad2.agregarConexionCiudad(ciudad5,8,4)
    ciudad3.agregarConexionCiudad(ciudad1,3,2)
    ciudad3.agregarConexionCiudad(ciudad2,1,2)
    ciudad3.agregarConexionCiudad(ciudad4,3,2)
    ciudad3.agregarConexionCiudad(ciudad5,2,2)
    ciudad4.agregarConexionCiudad(ciudad1,1,3)
    ciudad4.agregarConexionCiudad(ciudad3,3,2)
    ciudad4.agregarConexionCiudad(ciudad5,5,3)
    ciudad5.agregarConexionCiudad(ciudad2,8,4)
    ciudad5.agregarConexionCiudad(ciudad3,2,2)
    ciudad5.agregarConexionCiudad(ciudad4,5,3)

    ciudadesPorVisitar.append([ciudad1,0,0])
    while len(ciudadesPorVisitar) > 0:
        c1 = ciudadesPorVisitar.pop()[0]
        ruta, ciudadesPorVisitar = recorreEnProfundida(c1, ruta, ciudadesPorVisitar, ciudadesAVisitar)

    print(ruta)
main()