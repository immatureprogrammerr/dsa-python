from collections import deque

def bfs(graph, start_node):
    queue = deque([start_node])
    visited = set()

    while(queue):
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

bfs(graph, 'A')