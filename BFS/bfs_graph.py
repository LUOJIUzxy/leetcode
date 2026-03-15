from collections import deque

def bfs_graph(start, graph):
     q = deque([start])
     visited = set([start])

     while q:
          node = q.popleft()
          print(node)

          for nei in graph[node]:
               if nei not in visited:
                    visited.add(nei) 
                    q.append(nei)

graph = {
    "A": ["B", "C"],
    "B": ["D", "E", "F"],
    "C": ["F", "A", "B"],
    "D": ["B", "E", "F"],
    "E": ["F"],
    "F": []
}

bfs_graph("A", graph)
