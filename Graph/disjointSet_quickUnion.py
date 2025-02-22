# maintain an array
# root_array = [0, 0, 0, 1, 4, 5, 5, 5, 4, 9]
#root_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

class QuickUnion:
    # Add a constructor here for the root(parent)
    def __init__(self, size) -> None:
        # self.root_array = [0] * size
        # for i in range(size):
        #     self.root_array[i] = i
        
        self.root_array = [i for i in range(size)]

    # find the head of a node
    def find(self, node_index):
        node_value = self.root_array[node_index]
        # when index matches the value, this is a head node
        if node_index == node_value:
            return node_index
        else:
            return self.find(self.root_array[node_value])
        
    def is_connected(self, node1_index, node2_index):
        # root_index1 = self.find(node1_index)
        # root_index2 = self.find(node2_index)

        # if root_index1 == root_index2:
        #     return True
        # else:
        #     return False
        
        return self.find(node1_index) == self.find(node2_index)

    # input is two-element set
    def union(self, edge_tuple):
        if edge_tuple[0] < edge_tuple[1]:
            vertice1 = edge_tuple[0]
            vertice2 = edge_tuple[1]
        else:
            vertice1 = edge_tuple[1]
            vertice2 = edge_tuple[0]

        # if root_array[vertice1] == vertice1:
        #     root_array[vertice1] = vertice1
        # print(vertice1)
        self.root_array[vertice2] = vertice1
        print(self.root_array[vertice2])

    def connect(self, node1_index, node2_index):
        if node1_index < node2_index:
            # set node2 as the parent node of node1
            parent_of_node1 = self.find(node1_index)
            # and set the parent node of node 1 's parent to node2, so all the children nodes of it would have node2 as parent as well
            self.root_array[parent_of_node1] = node2_index
    

if __name__ == "__main__":
    number = 10
    edges = {(0, 1), (0, 2), (1, 3), (4, 8), (5, 6), (5, 7)}

    quickUnion = QuickUnion(10)
    

    print(quickUnion.root_array)
    for tuple in edges:
        quickUnion.union(tuple)
    print(quickUnion.root_array)

    print(quickUnion.find(3))

    vertices_tbchecked = {(0, 3), (1, 5), (7, 8)}
    for vertices in vertices_tbchecked:
        print(quickUnion.is_connected(vertices[0], vertices[1]))

    quickUnion.connect(7, 8)
    vertices_tbchecked = {(7, 8), (4, 6), (8, 5)}
    for vertices in vertices_tbchecked:
        print(quickUnion.is_connected(vertices[0], vertices[1]))