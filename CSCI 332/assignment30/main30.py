"""
Madison Grace Austin
CSCI 332 Spring 2025
Programming Assignment # class30
I acknowledge that I have worked on this assignment independently, except where explicitly
noted and referenced. Any collaboration or use of external resources has been properly cited.
I am fully aware of the consequences of academic dishonesty and agree to abide by the
university's academic integrity policy. I understand the importance the consequences of
plagiarism.
"""

def connected_components(graph):
    visited = set()
    components = []

    # through every node in the graph 
    for node in graph:
        if node not in visited:
            # Start a new list 
            component = []
            stack = [node]
            visited.add(node)
            
            # DFS 
            while stack:
                current = stack.pop()
                component.append(current)
                
                # Check neighbors of the current node
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)
            
            components.append(component)
            
    return components