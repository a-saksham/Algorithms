# Q's graph
graph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

adjacents = [['B', 'C', 'D', 'E'], ['A', 'F', 'I'],
             ['A', 'D'], ["A", "C", "E", "G"],
             ['A','D', 'F'], ['B','G', 'H', 'E', 'H', 'I'], ['D', 'F', 'H'],
             ['G', 'F', "I"], ["B", 'F', 'H']]

weights = [[4, 8], [11, 8],
           [7, 2, 4], [6, 14],
           [10], [2], [6, 1],
           [7], []]

visited = []
parent = [0]*len(graph)
cost = [-1]*len(graph)

# Element to start from
x = 'a'

# Until all Nodes are visited
while sorted(visited) != sorted(graph):
    visited.append(x)
    print(f"\nCurrent vertex -> {x}")
    index_x = graph.index(x)
    for i in range(len(adjacents[index_x])):

        if adjacents[index_x][i] not in visited:
            index_adj = graph.index(adjacents[index_x][i])

            # Cost Update
            if cost[index_adj] == -1 or cost[index_adj] > weights[index_x][i]:
                cost[index_adj] = weights[index_x][i]
                parent[index_adj] = x

            else:
                pass

    # Minimum Value of list Cost from non-visited nodes
    min = -1
    for i in range(len(cost)):
        if graph[i] in visited or cost[i] == -1:
            pass
        elif min == -1 or min > cost[i]:
            min = cost[i]
            index_min = i

    print("{:<14} -> {}".format("Visited list", str(visited)))
    print("{:<14} -> {}".format("Cost list", str(cost)))
    print("{:<14} -> {}".format("Parent list", str(parent)))

    if min != -1:
        print(f"Minimum cost = {min}, next vertex = {graph[index_min]}")

    # Shifting to Next Node
    x = graph[index_min]

cost[0] = 0

print("\n-----------------------------------------------------------------------------------------------------")
print("\nFINAL RESULTS:\n")
print("{:<14} -> {}".format("Visited list", str(visited)))
print("{:<14} -> {}".format("Cost list", str(cost)))
print("{:<14} -> {}".format("Parent list", str(parent)))
print("\nTotal Cost =", sum(cost))
print("\n-----------------------------------------------------------------------------------------------------")
