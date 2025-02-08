import heapq

def dijkstra(graph, start):
    # Initialize the priority queue
    queue = []
    heapq.heappush(queue, (0, start))
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    shortest_path = {}

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                shortest_path[neighbor] = current_vertex
                heapq.heappush(queue, (distance, neighbor))

    return distances, shortest_path

if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    start_vertex = 'A'
    distances, shortest_path = dijkstra(graph, start_vertex)

    print("Distances from start vertex:", distances)
    print("Shortest path tree:", shortest_path)