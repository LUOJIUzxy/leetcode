# maintain an array
# root_array = [0, 0, 0, 1, 4, 5, 5, 5, 4, 9]
root_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# find the head of a node
def find(node_index):
    node_value = root_array[node_index]
    # when index matches the value, this is a head node
    if node_index == node_value:
        return node_index
    else:
        return find(root_array[node_value])
    
def is_connected(node1_index, node2_index):
    root_index1 = find(node1_index)
    root_index2 = find(node2_index)

    if root_index1 == root_index2:
        return True
    else:
        return False

# input is two-element set
def union(edge_tuple):
    if edge_tuple[0] < edge_tuple[1]:
        vertice1 = edge_tuple[0]
        vertice2 = edge_tuple[1]
    else:
        vertice1 = edge_tuple[1]
        vertice2 = edge_tuple[0]

    # if root_array[vertice1] == vertice1:
    #     root_array[vertice1] = vertice1
    # print(vertice1)
    root_array[vertice2] = vertice1
    print(root_array[vertice2])
    

if __name__ == "__main__":
    number = 10
    edges = {(0, 1), (0, 2), (1, 3), (4, 8), (5, 6), (5, 7)}


    print(root_array)
    for tuple in edges:
        union(tuple)
    print(root_array)

    print(find(3))

    vertices_tbchecked = {(0, 3), (1, 5), (7, 8)}
    for vertices in vertices_tbchecked:
        print(is_connected(vertices[0], vertices[1]))