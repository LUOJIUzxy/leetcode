from collections import deque

def bfs(graph, start):
     n = len(graph)
     visited = set([start]) # { }
     q = deque([start]) # []

     # when the queue is not empty
     while q:
          node = q.popleft()

          # loop around this array length?
          for nei in range(n):
               if graph[node][nei] == 1 and nei not in visited:
                    visited.add(nei)
                    q.append(nei)
          
     return visited

# O(n^2)
# 对于 n x n 的邻接矩阵，节点 i 的所有邻居可以通过扫描第 i 行得到。
def count_components_bfs(graph):
     n = len(graph)
     visited = set()
     count = 0

     for i in range(n):
          if i not in visited:
               count += 1
               queue = deque([i])
               visited.add(i)

               while queue:
                    node = queue.popleft()
                    for nei in range(n):
                         if graph[node][nei] == 1 and nei not in visited:
                              visited.add(nei)
                              queue.append(nei)
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

# start with node 0
print(bfs(graph_1, 0))
          

