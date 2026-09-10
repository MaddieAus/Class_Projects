"""
Madison Grace Austin
CSCI 332 Spring 2025
Programming Assignment # class27
I acknowledge that I have worked on this assignment independently, except where explicitly
noted and referenced. Any collaboration or use of external resources has been properly cited.
I am fully aware of the consequences of academic dishonesty and agree to abide by the
university's academic integrity policy. I understand the importance the consequences of
plagiarism.
"""
import heapq

def dijkstra(graph, start):
    # If the start node isn't in the graph, return empty or handle
    if start not in graph and not graph:
        return{}

    # Initialize distances with infinity, start node at 0 
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Priority queue stores tuples
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        #  skip it,If we found a longer path then started with
        if current_distance > distances[current_node]:
            continue
            
        # Explore neighbors ("next to")
        for neighbor, weight in graph.get(current_node, []):
            distance = current_distance + weight
            
            # If a shorter path to the neighbor is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return {node: dist for node, dist in distances.items() if dist != float('inf')}

if __name__ == "__main__": # little test
    example_graph = {
        "A": [("B", 4), ("C", 2)],
        "B": [("C", 1), ("D", 5)],
        "C": [("B", 3), ("D", 8), ("E", 10)],
        "D": [("E", 2)],
        "E": []
    }
    print(dijkstra(example_graph, "A"))