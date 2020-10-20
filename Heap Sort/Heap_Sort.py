import time
import random
import matplotlib.pyplot as plt
import psutil
import os


def max_heapify(arr, n, i):
    l = left(i)
    r = right(i)
    if l < n and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def build_max_heap(arr):
    n = len(arr)
    for i in range(n, -1,-1):
        max_heapify(arr,n, i)
    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        max_heapify(arr,i,0)


def memory_usage():
    process = psutil.Process(os.getpid())
    mem = process.memory_info()[0]/float(2**20)
    return mem


x = list(map(int, input("Enter all Array sizes with spaces(eg: 10 100 1000):: ").split()))
time_taken = []
memory_used = []
for n in x:
    print("Size of Array ->", n)

    arr = random.sample(range(n), n)
    # print('\nInput Array :', arr)

    start = time.time()
    build_max_heap(arr)
    end = time.time()
    tt = end-start
    mem = memory_usage()
    time_taken.append(tt)
    memory_used.append(mem)
    # print('Sorted Array :', arr)
    print("\nFor {} size of array, heap sort takes {:.4f} seconds".format(n, tt))
    print("For {} size of array, heap sort uses {:.4f} mb".format(n, mem))
    print('----------------------------------------------------------------------------------------------------------')


# Graph
ans = input("Heap sort Graph Representation (Enter M for memory graph or T for time Graph): ")
if ans == 'T' or ans == 't':
    plt.plot(x, time_taken, color='blue', marker='o', label='Heap Sort - Time Taken')
    plt.legend()
    plt.xlabel('Size of Array (n)')
    plt.ylabel('Time Taken (in sec)')
    plt.title('''\nTime vs Array Size - HEAP SORT''')
    plt.grid(True)
    plt.show()

elif ans == 'M' or ans == 'm':
    plt.plot(x, memory_used, color='red', marker='o', label='Heap Sort - Memory Used')
    plt.legend()
    plt.xlabel('Size of Array (n)')
    plt.ylabel('Memory Usage (in mb)')
    plt.title('''\nMemory vs Array Size - HEAP SORT''')
    plt.grid(True)
    plt.show()

else:
    print('Invalid Input')

print('\n')
print('{:<50}-*-Thank You-*-'.format(' '))