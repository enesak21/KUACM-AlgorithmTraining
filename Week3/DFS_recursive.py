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

# DFS algorithm
def dfs(v):
    visited_list.add(v)
    print(visited_list) #watch how it is changed in each step
    for adj_of_v in adj_list[v]:
        if not adj_of_v in visited_list:
            dfs(adj_of_v)

dfs(1)
