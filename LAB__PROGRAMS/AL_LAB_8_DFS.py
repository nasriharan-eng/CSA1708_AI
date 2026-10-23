
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

visited = set()

def dfs(node):
    if node not in visited:
        visited.add(node)
        print(node, end=" ")
        for neighbour in graph[node]:
            dfs(neighbour)

dfs('A')
