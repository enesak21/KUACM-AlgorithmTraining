def Edge_List():
    edge_list = [] #stores edges as tuples (a,b) --> an edge from a to b
    num_edge = int(input("Enter the number of edges: "))
    print("Enter the edges: ")
    for i in range(num_edge):
        a, b = [int(x) for x in input().split()]
        edge_list.append((a, b))

def Adjacency_Matrices():
    # first node is the 0th node.
    num_node = int(input("Enter the number of nodes: "))
    # num_node by num_node 2-D array (matrix).
    # Mark as 1 if there is an edge or 0
    adjacency_matrix = [[0 for x in range(num_node)] for x in range(num_node)]

    num_edge = int(input("Enter the number of edges: "))
    print("Enter the edges: ")
    for i in range(num_edge):
        a, b = [int(x) for x in input().split()]
        # If the graph is undirected!
        adjacency_matrix[a][b] = 1
        adjacency_matrix[b][a] = 1

def Adjacency_List():
    adjacency_list = dict() # suprise, it is actually a dictionary :-)

    num_edge = int(input("Enter the number of edges: "))
    num_node = int(input("Enter the number of nodes: "))

    # Here it is assumed that nodes are numbered from 0 to num_edge - 1.
    for i in range(num_node):
        adjacency_list[i] = []
    print("Enter the edges: ")
    for i in range(num_edge):
        a, b = [int(x) for x in input().split()]

        # If the graph is undirected!
        adjacency_list[a].append(b)
        adjacency_list[b].append(a)


# OOP is another way to implement.

