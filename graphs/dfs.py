def dfs(graph, start_node):
    visited = set()
    stack = [start_node]

    while(stack):
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
        
        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(neighbor)


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

dfs(graph, 'A')