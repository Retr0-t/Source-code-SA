
def baca_data(filename):
    file = open(filename, "r")
    graph = {}
    text = file.readline().replace("\n", "")
    while text != "":
        if text.strip():
            text = text.strip().split()
            node1, node2, weight = text[0], text[1], int(text[2])
            if node1 not in graph:
                graph[node1] = {}
            if node2 not in graph:
                graph[node2] = {}
            graph[node1][node2] = weight
            graph[node2][node1] = weight
        text = file.readline().replace("\n", "")
    file.close()
    return graph

def floyd_warshall(graph, start, finish):
    # Inisialisasi matriks jarak
    nodes = list(graph.keys())
    n = len(nodes)
    distances = [[float('inf')] * n for _ in range(n)]
    next = [[None] * n for _ in range(n)]

    # Mengisi matriks jarak awal
    for i in range(n):
        distances[i][i] = 0
    for node1 in graph:
        for node2, weight in graph[node1].items():
            node1_index = nodes.index(node1)
            node2_index = nodes.index(node2)
            distances[node1_index][node2_index] = weight
            next[node1_index][node2_index] = node2

    # Algoritma Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
                    next[i][j] = next[i][k]

    # Membangun jalur terpendek dari start ke finish
    start_index = nodes.index(start)
    finish_index = nodes.index(finish)
    path = [start]
    distance = distances[start_index][finish_index]
    while start_index != finish_index:
        start_index = nodes.index(next[start_index][finish_index])
        path.append(nodes[start_index])

    print("Shortest path:", path)
    print("Shortest distance:", distance)

graph = baca_data("graph.txt")
print(graph)
start = input("Masukkan start: ")
finish = input("Masukkan finish: ")
floyd_warshall(graph, start, finish)




