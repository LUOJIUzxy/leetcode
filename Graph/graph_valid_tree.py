
# 1. Check if there's only one set, meaning number of unique set = 1
# 2. Check if there're cycles in the graph

class GraphValidTree:
    def __init__(self) -> None:
        self.root_array = []
        self.rank_array = []

    def find(self, index):
        if index != self.root_array[index]:
            self.root_array[index] = self.find(self.root_array[index] )
        return self.root_array[index]
    
    def union(self, index1, index2):
        root1 = self.find(index1)
        root2 = self.find(index2)
        if root1 == root2:
            return False

        if self.rank_array[root1] > self.rank_array[root2]:
            self.root_array[root2] = root1
        elif self.rank_array[root1] < self.rank_array[root2]:
            self.root_array[root1] = root2
        else:
            self.root_array[root2] = root1
            self.rank_array[root1] += 1
        return True
    

    
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        # Check if there's only one set, meaning number of unique set = 1
        # Check if there're cycles in the graph
        if len(edges) != n - 1:
            return False
        
        self.root_array = [i for i in range(n)]
        self.rank_array = [1 for _ in range(n)]

        for edge in edges:
            if not self.union(edge[0], edge[1]):
                return False
        return True


    
