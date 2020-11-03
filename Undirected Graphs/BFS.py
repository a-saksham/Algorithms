# Given Graph
graph = {1: [2, 3],
         2: [1, 4],
         3: [1, 4, 5],
         4: [2, 3],
         5: [3, 6],
         6: [5]}


# User input Graph
"""
print("Enter node and edge space separated..."
      "Press enter 2 times if no more values to insert")
graph = {}
while True:
    try:
        node, edge = map(int, input("").split())
        if node in graph.keys():
            if edge in list(graph[node]):
                pass
            else:
                x = list(graph[node])
                x.append(edge)
                graph[node] = x
        else:
            graph.update({node: [edge]})
    except:
        break
print(graph)
"""


# Breadth-first Search
def bfs(element):
    adjacents = graph[element]
    for i in adjacents:
        if i not in visited:
            visited.append(i)
            queue.append(i)


# printAll function prints all the results
def printAll():

    print("\nBFS Traverse :", end=' ')
    for i in bfs_ls:
        print(i, end=' ')
    
    print('\n')


global count
count = 0

# First element to start traverse from
element = int(input("\nEnter element you want to start with: "))

# Check if given element is in Graph or not
if element not in graph.keys():
    print("Value not in Graph")

# BFS traverse from the given element
else:
    bfs_ls = []
    visited = []
    queue = []

    visited.append(element)
    queue.append(element)

    while queue:
        bfs(queue[0])
        x = queue.pop(0)
        bfs_ls.append(x)

# Printing all results
printAll()
