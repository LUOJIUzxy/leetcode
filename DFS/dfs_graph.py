# 图和树最大的不同在于：图可能有环，所以通常要 visited。
def dfs(node, graph, visited):
    if node in visited:
        return

    visited.add(node)

    # 处理当前节点
    print(node)

    for nei in graph[node]:
        dfs(nei, graph, visited)

# use stack
def dfs_iter(start, graph):
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        print(node)

        for nei in reversed(graph[node]):
            if nei not in visited:
                stack.append(nei)

# 很多题不是给你一个固定起点，而是让你遍历整张图。
# 这时候就需要一个外层循环，来遍历图的每个节点，如果这个节点没有被访问过，就从这个节点开始DFS。
# 这个外层循环的作用是确保我们能够访问图中的每个节点，无论它们是否在同一个连通分量中。
# 例如，如果图中有两个独立的部分（两个连通分量），外层循环可以确保我们从每个部分的一个节点开始DFS，从而访问整个图。

# count_components()函数的作用是计算图中有多少个连通分量。
# 它通过遍历图中的每个节点，如果发现一个未访问过的节点，就从这个节点开始DFS，并将计数器加1。
# 这样，每当我们遇到一个新的连通分量时，计数器就会增加，最终返回连通分量的总数。
def count_components(graph) -> int:
     visited = set()
     count = 0

     # 循环graph这个dict的keys
     for node in graph:
        if node not in visited:
            dfs(node, graph, visited)
            count += 1
            # visited.add(node), 不需要，因为dfs()函数里面已经add()了

     return count

    


# 
graph = {
    "A": [ "C"],
    "B": ["D", "E"],
    "C": ["F",],
    "D": ["E"],
    "E": [],
    "F": []
}

# visited = set()
# dfs("A", graph, visited)
print(count_components(graph))
