import heapq

def baca_data(filename):
    file = open(filename,"r")
    graph = {}
    text = file.readline().replace("\n","")
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
        text = file.readline().replace("\n","") 
    file.close()
    return graph

def dijkstra(graph, start, finish):
    # Inisialisasi variabel
    distances = {node: {"cost": float('inf'),"path":[]} for node in graph}
    distances[start]["cost"] = 0
    visited = []
    heap = [(0, start)]
    
    for i in range(len(graph)):
        # Ambil node dengan jarak terpendek dari node awal
        (current_distance, current_node) = heapq.heappop(heap)
        
        # Jika node telah dikunjungi, lewati
        if current_node in visited:
            continue
        
        # Tandai node jika sudah dikunjungi
        visited.append(current_node)
        
        # Update jarak terpendek dari node awal ke tetangga-tetangganya
        for neighbor in graph[current_node]:
            cost = current_distance + graph[current_node][neighbor]
            if cost < distances[neighbor]["cost"]:
                distances[neighbor] = {"cost": cost, "path": distances[current_node]["path"] + [current_node]}
                heapq.heappush(heap, (cost, neighbor))
            
    
    print("Shortest distance:", distances[finish]["cost"])
    print("Shortest path:", distances[finish]["path"] + [finish])
    

Graph = baca_data("graph.txt")
print(Graph)
start = input("Masukkan start: ")
finish = input("Masukkan tujuan: ")
print(dijkstra(Graph, start, finish))

