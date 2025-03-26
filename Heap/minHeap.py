# Implementing "Min Heap"
import math

class MinHeap:
    
    def __init__(self, heapSize, array):
        # Create a complete binary tree using an array
        # Then use the binary tree to construct a Heap
        if heapSize + 1 != len(array):
            print("Array size does not match!")
            return
        self.heapSize = heapSize 
        # the number of elements is needed when instantiating an array
        # heapSize records the size of the array
        #self.minheap = [0] * (heapSize + 1)
        self.minheap = array
        # realSize records the number of elements in the Heap
        self.realSize = 0
    
    # level of this complete binary tree
    def length(self):
        return self.heapSize.bit_length()

    def heapify(self, node_index):
        smallest = node_index
        left = smallest * 2
        right = smallest * 2 + 1

        if left > self.heapSize or right > self.heapSize:
            return

        if self.minheap[smallest] > self.minheap[left] or self.minheap[smallest] > self.minheap[right] :
            if self.minheap[left] >= self.minheap[right] :
                self.minheap[smallest], self.minheap[right] = self.minheap[right], self.minheap[smallest]
                
                self.heapify(right)
            else:
                self.minheap[smallest], self.minheap[left] = self.minheap[left], self.minheap[smallest]
                
                self.heapify(left)
            
        

    # O(logN)
    # Function to add an element
    def add(self, element):
        self.realSize += 1
        # If the number of elements in the Heap exceeds the preset heapSize
        # print "Added too many elements" and return
        if self.realSize > self.heapSize:
            print("Added too many elements!")
            self.realSize -= 1
            return
        # Add the element into the array
        self.minheap[self.realSize] = element
        # Index of the newly added element
        index = self.realSize
        # Parent node of the newly added element
        # Note if we use an array to represent the complete binary tree
        # and store the root node at index 1
        # index of the parent node of any node is [index of the node / 2]
        # index of the left child node is [index of the node * 2]
        # index of the right child node is [index of the node * 2 + 1]
        parent = index // 2
        # If the newly added element is smaller than its parent node,
        # its value will be exchanged with that of the parent node 
        # Do a swap
        while (self.minheap[index] < self.minheap[parent] and index > 1):
            self.minheap[parent], self.minheap[index] = self.minheap[index], self.minheap[parent]
            # 一直往上寻找比较
            index = parent
            parent = index // 2
    
    # Get the top element of the Heap
    # O(1)
    def peek(self):
        return self.minheap[1]
    

    # Delete the top element of the Heap
    def pop(self):
        # If the number of elements in the current Heap is 0,
        # print "Don't have any elements" and return a default value
        if self.heapSize < 1:
            print("Don't have any element!")
            return 
            #return sys.maxsize
        else:
            # When there are still elements in the Heap
            # self.realSize >= 1
            removeElement = self.minheap[1]
            # Put the last element in the Heap to the top of Heap
            self.minheap[1] = self.minheap[self.heapSize]
            self.heapSize -= 1
            index = 1
            # When the deleted element is not a leaf node
            while (index <= self.heapSize // 2):
                # the left child of the deleted element
                left = index * 2
                # the right child of the deleted element
                right = (index * 2) + 1
                # If the deleted element is larger than the left or right child
                # its value needs to be exchanged with the smaller value
                # of the left and right child
                if (self.minheap[index] > self.minheap[left] or self.minheap[index] > self.minheap[right]):
                    if self.minheap[left] < self.minheap[right]:
                        self.minheap[left], self.minheap[index] = self.minheap[index], self.minheap[left]
                        index = left
                    else:
                        self.minheap[right], self.minheap[index] = self.minheap[index], self.minheap[right]
                        index = right
                else:
                    break
            return removeElement
    
    # o(1)
    # return the number of elements in the Heap
    def size(self):
        return self.heapSize
    
    def __str__(self):
        return str(self.minheap[1 : self.heapSize + 1])
        

if __name__ == "__main__":
    	# Test cases
        num_nodes = 5
        arr = [3, 1, 2, 6, 5]

        # add a 0 in the front
        arr.insert(0, 0)

        minHeap = MinHeap(num_nodes, arr)
        # minHeap.add(3)
        # minHeap.add(1)
        # minHeap.add(2)
     
        level = minHeap.length()
        print(level)
        print(minHeap.minheap)

        for j in range(1, level):
            for i in range(pow(2, (level - 1 - j)), pow(2, (level - j))):
                print(i)
                minHeap.heapify(i)

        # [1,3,2]
        print(minHeap.minheap)
        # 1
        print(minHeap.peek())
        # 1
        print(minHeap.pop())
        # 2
        print(minHeap.pop())
        # 3
        print(minHeap.pop())
        minHeap.add(4)
        minHeap.add(5)
        # [4,5]
        print(minHeap.minheap)