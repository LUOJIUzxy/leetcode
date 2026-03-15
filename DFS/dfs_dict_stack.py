


def dfs_iterative(start, graph):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            print(node)

            # reverse to keep left-to-right order similar to recursive DFS
            for neighbor in reversed(graph[node]):
                stack.append(neighbor)

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}


dfs_iterative("A", graph)
