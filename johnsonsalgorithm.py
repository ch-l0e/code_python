import heapq

# Define the graph as an adjacency list, where each node points to a list of (neighbor, weight) tuples.
# For example, graph = {0: [(1, 3), (2, 8)], 1: [(2, -4)], 2: []}
def johnson(graph):
    # Step 1: Add a new node 's' that connects to all other nodes with weight 0
    n = len(graph)
    new_graph = {i: edges[:] for i, edges in graph.items()}
    new_graph[n] = [(i, 0) for i in range(n)]

    # Step 2: Run Bellman-Ford from the new node to calculate potential values
    def bellman_ford(source, graph):
        distances = {node: float('inf') for node in graph}
        distances[source] = 0
        for _ in range(len(graph) - 1):
            for u in graph:
                for v, weight in graph[u]:
                    if distances[u] + weight < distances[v]:
                        distances[v] = distances[u] + weight
        # Check for negative-weight cycles
        for u in graph:
            for v, weight in graph[u]:
                if distances[u] + weight < distances[v]:
                    return None  # Negative cycle detected
        return distances

    potential = bellman_ford(n, new_graph) #runs above funtion
    if potential is None:
        print("Graph contains a negative-weight cycle")
        return None

    # Step 3: Reweight the edges to remove negative weights
    reweighted_graph = {}
    for u in graph:
        reweighted_graph[u] = []
        for v, weight in graph[u]:
            new_weight = weight + potential[u] - potential[v]
            reweighted_graph[u].append((v, new_weight))

    # Step 4: Run Dijkstra's algorithm for each node using the reweighted edges
    def dijkstra(source):
        distances = {node: float('inf') for node in graph}
        distances[source] = 0
        min_heap = [(0, source)]
        while min_heap:
            current_dist, u = heapq.heappop(min_heap)
            if current_dist > distances[u]:
                continue
            for v, weight in reweighted_graph[u]:
                distance = current_dist + weight
                if distance < distances[v]:
                    distances[v] = distance
                    heapq.heappush(min_heap, (distance, v))
        return distances

    # Step 5: Adjust the distances back using the potential values
    all_pairs_shortest_paths = {}
    for u in graph:
        dist_from_u = dijkstra(u)
        all_pairs_shortest_paths[u] = {v: dist_from_u[v] + potential[v] - potential[u] for v in graph}

    return all_pairs_shortest_paths

# Example usage
graph = {
    0: [(1, 3), (2, 8)],
    1: [(2, -4), (3, 2)],
    2: [(3, 1)],
    3: []
}
shortest_paths = johnson(graph)
if shortest_paths:
    print("All pairs shortest paths:")
    for u in shortest_paths:
        for v in shortest_paths[u]:
            print(f"Shortest path from {u} to {v}: {shortest_paths[u][v]}")
