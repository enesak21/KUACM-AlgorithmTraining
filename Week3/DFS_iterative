from queue import LifoQueue

adj_list = dict() #its actually a hashmap not list
visited_list = set() #its actually a set not list

num_edge = int(input("Enter the number of edges:"))

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

to_visit = LifoQueue(maxsize=num_edge) #thats a stack
to_visit.put(1)

# DFS algorithm
while not to_visit.empty():
    last_visited_node = to_visit.get()
    visited_list.add(last_visited_node)
    print(visited_list)
    for adj_nodes in adj_list[last_visited_node]:
        if adj_nodes not in visited_list:
            to_visit.put(adj_nodes)


