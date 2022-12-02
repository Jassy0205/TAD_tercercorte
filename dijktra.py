def dijkstra(Grafo, salida):
    dist, prev = {}, {}
    result = []

    for vertice in Grafo:
        dist[vertice] = float("inf")
        prev[vertice] = None
    dist[salida] = 0

    vertice_visited = [vertice for vertice in Grafo]

    while vertice_visited:
        u = min(vertice_visited, key=dist.get)
        vertice_visited.remove(u)
        result.append(u)

        for vecino in Grafo[u]:
            if vecino in vertice_visited and dist[vecino] > dist[u] + Grafo[u][vecino]:
                dist[vecino] = dist[u] + Grafo[u][vecino]
                prev[vecino] = u

    return result, dist, prev


grafo = {
    'Armenia': {'Barranquilla': 4, 'Cali': 3},
    'Barranquilla': {'Pereira': 5},
    'Cali': {'Barranquilla': 2, 'Pereira': 3, 'Bogotá': 6},
    'Pereira': {'Bogotá': 5, 'Neiva': 1},
    'Bogotá': {'Medellín': 5},
    'Medellín': {'Santa Marta': 4},
    'Neiva': {'Medellín': 2, 'Santa Marta': 7},
    'Santa Marta': {}
}

s, distancia, previos = dijkstra(grafo, 'Armenia')
print(f"{s=}")
print(f"{distancia=}")