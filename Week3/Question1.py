# DFS algorithm
def dfs(v):
    visited_list.add(v)
    for adj_of_v in adj_list[v]:
        if not adj_of_v in visited_list:
            dfs(adj_of_v)

adj_list = dict() #its actually a hashmap not list
visited_list = set() #its actually a set not list

num_edge = int(input("Enter the number of edges: "))
num_node = int(input("Enter the number of nodes: "))

# Creating adj_list
for i in range(num_edge):
    n1, n2 = [int(x) for x in input("Enter the edge:").split()]
    if n1 in adj_list:
        adj_list[n1].append(n2)
    else:
        adj_list[n1] = [n2]
    if n2 in adj_list:
        adj_list[n2].append(n1)
    else:
        adj_list[n2] = [n1]

dfs(1) # You can start from any point
connected = True
for a_node in range(1, num_node + 1):
    if a_node not in visited_list:
        connected = False
        print(a_node, "is not connected to", 1)
if connected:
    print("Connected")
