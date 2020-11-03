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


# Depth-first Search
def dfs(element):
    global count

    adjacents = graph[element]
    for i in adjacents:
        if i not in visited:
            stack.append(i)
            visited.append(i)
            count += 1
            pre_post[i].append(count)
            return

    if (all(x in visited for x in adjacents)):
        dfs_ls.append(stack[-1])
        count += 1
        pre_post[stack[-1]].append(count)
        stack.pop(-1)


# printAll function prints all the results
def printAll():

    print("\nDFS Traverse :", end= ' ')
    for i in dfs_ls:
        print(i, end=' ')

    print("\n\nPre and Post visited times -)")
    for i, values in pre_post.items():
        pre, post = values
        print("Node {}: Pre -> {}  Post -> {}".format(i, pre, post))
    print('\n')


global count
count = 0
pre_post = {}
for i in graph.keys():
    pre_post.update({i: []})

# First element to start traverse from
element = int(input("\nEnter element you want to start with: "))

# Check if given element is in Graph or not
if element not in graph.keys():
    print("Value not in Graph")

# DFS traverse from the given element
else:
    dfs_ls = []
    visited = []
    stack = []

    visited.append(element)
    stack.append(element)
    count += 1
    pre_post[element].append(count)

    while stack:
        dfs(stack[-1])

# Printing all results
printAll()
