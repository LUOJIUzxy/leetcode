def dfs(graph, node, visited):
    n = len(graph)
    visited.add(node)

    for nei in range(n):
        if graph[node][nei] == 1 and nei not in visited:
            dfs(graph, nei, visited)

def count_components(graph):
     n = len(graph)

     # visited 存的是整个graph里面被遍历过的nodes
     visited = set()
     # count how many independent islands etc.
     count = 0

     # 一次的dfs，代表了访问一个independent的island 所有连接起来的点, 和下方的每次循环可以联系起来
     def dfs1(node):
          visited.add(node)
          for nei in range(n):
               if graph[node][nei] == 1 and nei not in visited:
                    dfs1(nei)


     # dfs 能一次跑完的就是一个独立的 island， count + 1
     for i in range(n):
          if i not in visited:
               dfs1(i)
               count += 1
     
     return count


graph_1 = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
]

graph_2 = [
     [0, 1, 0, 0, 1, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 1, 0, 1, 1, 0],
     [1, 0, 1, 0, 0, 0, 0, 1],
     [0, 0, 0, 1, 0, 0, 1, 0],
     [0, 0, 0, 1, 0, 1, 0, 0],
     [1, 0, 0, 0, 1, 0, 0, 0],
]

# visited = set()
# dfs(graph_1, 0, visited)
# print(visited)   # {0, 1, 2, 3}

print(count_components(graph_2))