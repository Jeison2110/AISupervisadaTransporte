"""
Creado por:
    IdBanner:100098659
    Nombre: Esperanza Castro Lombana 

    IdBanner:100096167
    Nombre: Jeison Valencia Sanchez

    Fecha: 2024-04-02, ©/ todos los derechos reservados
    Corporación Universitaria Iberoamericana

    Identifique y describa fuentes de datos relacionadas con el proyecto del transporte masivo propuesto en las actividades anteriores,
    con el fin de desarrollar modelos de aprendizaje supervisado. En caso de no existir dichas fuentes de datos, desarrolle un dataset
    con una muestra de dichos datos.
"""
# Bibliotecas utilizadas
from collections import defaultdict #Biblioteca para almacenar elementos clave valor (Tipo diccionario)
from heapq import heappop, heappush #Biblioteca para procesos de colas con prioridad en árboles binarios

# Lista con las estaciones del sistema de transporte
estaciones = (
    "Bello",
    "Madera",
    "Centromed",
    "Poblado",
    "Itagui",
    "Sabaneta",
    "Estrella",
)

# Diccionario de adyacencia con las distancias de las estaciones entre sí
adyacencia = defaultdict(dict)
adyacencia["Bello"]["Madera"] = 5
adyacencia["Madera"]["Bello"] = 5

adyacencia["Bello"]["Centromed"] = 10
adyacencia["Centromed"]["Bello"] = 10

adyacencia["Madera"]["Centromed"] = 3
adyacencia["Centromed"]["Madera"] = 3

adyacencia["Madera"]["Poblado"] = 15
adyacencia["Poblado"]["Madera"] = 15

adyacencia["Centromed"]["Itagui"] = 8
adyacencia["Itagui"]["Centromed"] = 8

adyacencia["Centromed"]["Sabaneta"] = 11
adyacencia["Sabaneta"]["Centromed"] = 11

adyacencia["Centromed"]["Estrella"] = 14
adyacencia["Estrella"]["Centromed"] = 14

adyacencia["Poblado"]["Itagui"] = 6
adyacencia["Itagui"]["Poblado"] = 6

adyacencia["Poblado"]["Sabaneta"] = 9
adyacencia["Sabaneta"]["Poblado"] = 9

adyacencia["Itagui"]["Sabaneta"] = 5
adyacencia["Sabaneta"]["Itagui"] = 5

adyacencia["Sabaneta"]["Estrella"] = 3
adyacencia["Estrella"]["Sabaneta"] = 3


# Función para obtener el predecesor de una estación en la ruta
def ObtenerPredecesor(distancias, estacion):
    for predecesor, distanciaestaciones in adyacencia.items():
        if estacion in distanciaestaciones and distancias[estacion] == distancias[predecesor] + distanciaestaciones[estacion]:
            return predecesor


# Función para reconstruir la ruta desde el origen al destino
def RealizarRuta(distancias, origen, destino):
    ruta = []
    estacionactual = destino

    # Recorrer la ruta desde el destino al origen
    while estacionactual != origen:
        ruta.append(estacionactual)
        estacionactual = ObtenerPredecesor(distancias, estacionactual)

    # Añadir el origen al inicio de la ruta
    ruta.append(origen)

    # Invertir la ruta para obtener el orden correcto
    ruta.reverse()

    return ruta


# Función para encontrar la mejor ruta
def EncontrarMejorRuta(origen, destino):
    # Cola de prioridad para almacenar las estaciones a explorar
    colaprioridad = [(0, origen)]

    # Diccionario para almacenar las distancias desde el origen a cada estación
    distancias = {origen: 0}

    # Bucle para explorar las estaciones
    while colaprioridad:
        # Obtener la estación con la menor distancia actual
        distanciaactual, estacionactual = heappop(colaprioridad)

        # Si se ha llegado al destino, devolver la ruta
        if estacionactual == destino:
            return RealizarRuta(distancias, origen, destino)

        # realizamos un bucle para cada vecino de la estación actual de la busquedad
        for vecino, distanciaestaciones in adyacencia[estacionactual].items():
            # Calcular la distancia total al vecino
            distanciatotal = distanciaactual + distanciaestaciones

            # verificamos si el vecino no se ha explorado o se encuentra una ruta más corta
            if vecino not in distancias or distanciatotal < distancias[vecino]:
                # Actualizamos la distancia al vecino
                distancias[vecino] = distanciatotal

                # añadimos al vecino a la cola de prioridad
                heappush(colaprioridad, (distanciatotal, vecino))

    # En caso de no encontrar una ruta entre los dos puntos, devolvemos None
    return None


# Le mostramos al usuario las estaciones disponibles del transporte masivo
print("""--==========Bienvenido Al Transporte Masivo BUSMED==========--
Actual mentes el transporte cuenta con las siguientes estaciones:""")
for Estaciones in estaciones:
    print(f"Estacione: {Estaciones}")


print("\n")
# Validamos que el usuario ingrese las estaciones de origen y fin correctamente
while True:    
    EstacionA = str(input("Ingrese la estacion de inicio: "))
    EstacionB = str(input("Ingrese la estacion final: "))

    EstacionInicio = EstacionA.title().lstrip().rstrip()
    EstacionFinal = EstacionB.title().lstrip().rstrip()

    if EstacionInicio not in estaciones:
        print ("La estacion de inicio no corresponde con una estacion valida del sistema BUSMED")  
    elif EstacionFinal not in estaciones:
        print ("La estacion de destino no corresponde con una estacion valida del sistema BUSMED")            
    else:
        break
       

# Ejecutamos la funcion que contiene el algoritmo supervisado de KNN (K vecinos mas cercanos)
ruta = EncontrarMejorRuta(EstacionInicio, EstacionFinal)

# Ejecutamos los print para verificar por cuales estaciones se debe pasar para llegar desde punto inicial al punto final 
i = 1
print("\n"f"""El camino mas corto desde la estacion: "{EstacionInicio}" hasta la estacion: "{EstacionFinal}" es: """)
for Rutas in ruta:
    print(f"{i}°Estacion: {Rutas}")
    i +=1