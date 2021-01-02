"""
# User Input Graph
n = int(input("No. of vertices: "))
graph = []

# Break when input is string
print("Enter vertex adjacent weight (space separated)")
while True:
    try:
        x = list(map(int, input().split()))
        graph.append(x)

    except:
        break
"""

# Hard Cored Input Graph
graph = [['g','h',1],
         ['e','i',2],
         ['f','g',2],
         ['a','b',4],
         ['c','f',4],
         ['g','i',6],['d','e',6],['h','i',7],['c','d',7],['b','c',8],['a','h',8],['e','f',10],['b','h',11],['d','f',14]]


# Sort the graph according to their weights
sorted_graph = graph
sorted_graph.sort(key = lambda x :x[2])


# MAIN
flag = []
kr_ls = []
for i in sorted_graph:
    if i[1] not in flag:
        kr_ls.append(i)
        flag.append(i[1])


# Printing part
kr_ls.sort(key = lambda x: x[1])

print("\n-----------------------------------------------------------------------------------------------------\n")
print("RESULT ::\n")
sum = 0
for i in kr_ls:
    print(f"Cost for vertex '{i[0]}' to vertex '{i[1]}' = {i[2]}")
    sum+=i[2]

print("\nTotal Cost =",sum)
print("\n-----------------------------------------------------------------------------------------------------")
