from typing import List
import ast

class disjointSet:
    def __init__(self) -> None:
        self.isConnected = self.input_matrix()
        self.number_of_N = len(self.isConnected)
        self.root_array = [i for i in range(len(self.isConnected))]
        self.rank_array = [1] * len(self.isConnected)

    def input_matrix(self) -> List[List[int]]:
        """
        Function to input an n x n matrix in the format [[1,1,0],[1,1,0],[0,0,1]].
        """
        while True:
            input_str = input("Enter the matrix in the format [[1,1,0],[1,1,0],[0,0,1]]: ").strip()
            
            try:
                # Parse the input string into a Python list
                isConnected = ast.literal_eval(input_str)
                
                # Validate that the input is a list of lists of integers
                if isinstance(isConnected, list) and all(isinstance(row, list) for row in isConnected):
                    n = len(isConnected)
                    if all(len(row) == n for row in isConnected) and all(x in {0, 1} for row in isConnected for x in row):
                        return isConnected
                    else:
                        print("Error: The matrix must be square (n x n) and contain only 0s and 1s.")
                else:
                    print("Error: The input must be a list of lists.")
            except (ValueError, SyntaxError):
                print("Error: Invalid input format. Please enter a valid nested list.")
    
    def find(self, index):
        if index == self.root_array[index]:
            return self.root_array[index]
        if index != self.root_array[index]:
            return self.find(self.root_array[index])
        
    def union(self, index1, index2):
        root1 = self.find(index1)
        root2 = self.find(index2)

        if self.rank_array[root1] > self.rank_array[root2]:
            self.root_array[root2] = root1
        elif self.rank_array[root1] < self.rank_array[root2]:
            self.root_array[root1] = root2
        elif self.rank_array[root1] == self.rank_array[root2]:
            self.root_array[root2] = root1
            self.rank_array[root1] += 1
            #print(self.rank_array[root1])
    
    def findCircleNum(self) -> int:
        circleNum = 1

        for i, row in enumerate(self.isConnected):
            for j in range(i + 1, self.number_of_N):
                if row[j] == 1:
                    self.union(i, j)
                    # print(self.root_array)

            
        for i, value in enumerate(self.root_array):
            # Get the real root values for every index in the parent array   
            root = self.find(i)
            #print(root)
            self.root_array[i] = root


        unique_set = set(self.root_array)
        circleNum = len(unique_set)
        # Check how many different numbers are there in 
            
            
        return circleNum
    
if __name__ == "__main__":
    quickUnion = disjointSet()
    print(quickUnion.root_array)

    print(quickUnion.findCircleNum())


                


        


        