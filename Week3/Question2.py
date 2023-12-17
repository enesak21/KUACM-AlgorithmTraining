import queue
from queue import Queue

def bfs(start, end):
    visited_queue = Queue(maxsize=num_node)
    visited_queue.put((start, 0)) # (the_node, distance_to_start)
    visited_list.add(start)
    while not visited_queue.empty():
        a_node = visited_queue.get()
        if end == a_node[0]:
            print("The length of the shortest path between", start, "and", end, "is", a_node[1])
            return
        for adj_nodes in adj_list[a_node[0]]:
            if adj_nodes in visited_list:
                continue
            visited_list.add(adj_nodes)
            visited_queue.put((adj_nodes, a_node[1] + 1)) # (next_node, distance + 1)


adj_list = dict() #its actually a hashmap not list
visited_list = set() #its actually a set not list

num_edge = int(input("Enter the number of edges:"))
num_node = int(input("Enter the numer of nodes:"))

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

bfs(1, 7)
