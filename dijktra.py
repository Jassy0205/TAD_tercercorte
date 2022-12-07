def dijkstra(Grafo, salida):
    dist, prev = {}, {}
    result = []
    recorrido = []

    for vertice in Grafo:
        dist[vertice] = float("inf")
        prev[vertice] = None
    dist[salida] = 0

    vertice_visited = [vertice for vertice in Grafo]

    while vertice_visited:
        u = min(vertice_visited, key=dist.get)
        print('hola', u, result, vertice_visited)
        vertice_visited.remove(u)
        result.append(u)

        for vecino in Grafo[u]:
            vector = []
            if vecino in vertice_visited and dist[vecino] > dist[u] + Grafo[u][vecino]:
                real = None
                index = -1
                for vertice in recorrido: 
                    actual_vector = vertice
                    i = len(actual_vector)
                    for valores in actual_vector:
                        if valores == u and actual_vector[i-1] == valores:
                            real = actual_vector
                        elif valores == vecino:
                            index = recorrido.index(actual_vector)
                if index != -1:
                    recorrido.pop(index)
                    index = -1
                
                if u != salida:
                    if real != None: 
                        vector = [salida]
                        vector.extend(real)
                        vector.append(vecino)
                    else: 
                        vector = [salida, u, vecino]
                else:
                    vector = [salida, vecino]

                recorrido.append(vector)
                print(Grafo[u][vecino], u, dist[vecino], dist[u], prev[vecino], vector)
                dist[vecino] = dist[u] + Grafo[u][vecino]
                prev[vecino] = u

    return result, dist, prev, recorrido

def verifica_antecesor(vector, actual, incial, vecino):
    real = []
    index = -1

    for vertice in vector: 
        actual_vector = vertice
        for valores in actual_vector:
            if valores == actual:
                real = actual_vector
            elif valores == vecino:
                index = vector.index(actual_vector)
        if index != -1:
            vector.pop(index)
            index = -1

    return False


grafo = {
    'San Andrés': {'Armenia': 100, 'Barranquilla': 50, 'Bucaramanga': 1000, 'Bogotá': 29, 'Cali': 880, 'Cartagena': 1096, 'Cúcuta': 12, 'Leticia': 959, 'Medellin': 215, 'Monteria': 758, 'Neiva': 345, 'Pereira': 958, 'Pasto': 648, 'Santa Marta': 1055, 'Valledupar': 648, 'Villavicencio': 364},
    'Armenia': {'San Andrés': 560, 'Barranquilla': 215, 'Bucaramanga':1025, 'Bogotá': 325, 'Cali': 648, 'Cartagena': 645, 'Cúcuta': 36, 'Medellin': 13, 'Monteria': 564, 'Neiva': 659, 'Pasto': 326, 'Santa Marta': 158, 'Valledupar': 458, 'Villavicencio': 478},
    'Barranquilla': {'San Andrés': 254, 'Armenia': 854, 'Bucaramanga': 515, 'Bogotá': 5447, 'Cali': 645, 'Cartagena': 887, 'Cúcuta': 5487, 'Leticia': 2154, 'Medellin': 325, 'Monteria': 169, 'Neiva': 698, 'Pereira': 57, 'Pasto': 13, 'Santa Marta': 125, 'Valledupar': 256, 'Villavicencio': 36},
    'Bucaramanga': {'San Andrés': 547, 'Armenia': 215, 'Barranquilla':255, 'Bogotá': 1025, 'Cali': 987, 'Cartagena': 985, 'Cúcuta': 745, 'Leticia': 652, 'Medellin': 324, 'Monteria': 329, 'Neiva': 603, 'Pereira': 569, 'Pasto': 763, 'Santa Marta': 1156, 'Valledupar': 378, 'Villavicencio': 906},
    'Bogotá': {'San Andrés': 129, 'Armenia': 1048, 'Barranquilla': 895, 'Bucaramanga': 645, 'Cali': 516, 'Cartagena': 19, 'Cúcuta': 325, 'Leticia': 22, 'Medellin': 658, 'Monteria': 756, 'Neiva': 1548, 'Pereira': 453, 'Pasto': 1001, 'Santa Marta': 132, 'Valledupar': 326, 'Villavicencio': 856},
    'Cali': {'San Andrés': 632, 'Armenia': 157, 'Barranquilla': 908, 'Bucaramanga': 564, 'Bogotá': 36, 'Cartagena': 75, 'Cúcuta': 504, 'Leticia': 95, 'Medellin': 958, 'Monteria': 345, 'Neiva': 632, 'Pereira': 623, 'Pasto': 632, 'Santa Marta': 1007, 'Valledupar': 1096, 'Villavicencio': 563},
    'Cartagena': {'San Andrés': 38, 'Armenia': 57, 'Barranquilla': 62, 'Bucaramanga': 79, 'Bogotá': 81, 'Cali': 1078, 'Cúcuta': 655, 'Leticia': 245, 'Medellin': 31, 'Monteria': 458, 'Neiva': 625, 'Pereira': 326, 'Pasto': 932, 'Santa Marta': 1013, 'Valledupar': 459, 'Villavicencio': 263},
    'Cúcuta': {'San Andrés': 1058, 'Armenia': 954, 'Barranquilla': 325, 'Bucaramanga': 423, 'Bogotá': 1053, 'Cali': 64, 'Cartagena': 139, 'Leticia': 5.2, 'Medellin': 695, 'Monteria': 425, 'Neiva': 319, 'Pereira': 769, 'Pasto': 632, 'Santa Marta': 546, 'Valledupar': 692, 'Villavicencio': 752}
}

s, distancia, previos, recorrido = dijkstra(grafo, 'Barranquilla')
#print(f"{s=}")
print(f"{distancia=}")
#print(f"{previos=}")
print(f"{recorrido=}")