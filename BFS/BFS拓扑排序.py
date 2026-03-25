from typing import List
from collections import deque 

# args: prerequisite, return 1-d graph
# graph[b] 里存所有依赖 b 的课程, 出度
# indegree[a] += 1，表示 a 还差一个前置条件
def build_graph(n: int, nodes_array: List[List[int]]):
     graph = [[] for _ in range(n)]
     indegree = [0] * n 
     for i in range(len(nodes_array)):
          graph[nodes_array[i][1]].append(nodes_array[i][0])
          indegree[nodes_array[i][0]] += 1
     
     return graph, indegree

def findOrder(numCourses: int, prerequisited: List[List[int]]):
     graph, indegrees = build_graph(numCourses, prerequisited)

     q = deque()
     result = []

     for i, indegree in enumerate(indegrees):
          if indegree == 0:
               q.append(i)

     while q:
          course = q.popleft()
          result.append(course)

          # 遍历course的所有后继，并给所有后继的indegree - 1
          for next_course in graph[course]:
               indegrees[next_course] -= 1
               if indegrees[next_course] == 0:
                    q.append(next_course)

     if len(result) < numCourses:
          return []
     else: 
          return result

numCourses = 2
prerequisites = [[1,0],[0, 1]]
print(findOrder(numCourses, prerequisites))     



     
