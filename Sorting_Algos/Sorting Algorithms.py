import sys                                              # Importing necessary libraries
import random
import time
import matplotlib.pyplot as plt
sys.setrecursionlimit(100000000)                        # Increasing / setting new recursion limit


def insertionsort(A):                                  # Insertion Sort
    start = time.time()                     # time counter starts
    for j in range(1, len(A)):              # loop iterating 'length of Array' times
        key = A[j]                          # updating key
        i = j-1
        while i > -1 and A[i] > key:        # iterating until the array is empty and A[i] greater than key
            A[i+1] = A[i]
            A[i] = key                      # swapping values if previous values is greater than current
            i = i - 1
    end = time.time()                       # time counter ends
    return (end-start)                      # returning time taken by Insertion Sort


def bubble_sort(A):                                     # Bubble Sort
    start = time.time()                     # time counter starts
    for i in range(0, len(A)):              # iterating for 'size of array' times
        j = len(A)                          # setting j as last index + 1
        while j > i+1:                      # iterating until the index reaches to len(A)
            j = j - 1                       # decrementing j
            if A[j] < A[j-1]:               # swapping elements
                temp = A[j]
                A[j] = A[j-1]
                A[j-1] = temp
    end = time.time()                       # time counter ends
    return (end-start)                      # returning time taken by Bubble Sort


def selection_sort(A):                                  # Selection Sort
    start = time.time()                     # time counter starts
    for i in range(len(A)):                 # iterating 'size of array' times
        min = i                             # updating minimum index over every iteration
        for j in range(i+1, len(A)):        # loop to iterate unsorted part of array
            if A[j] < A[min]:               # finding the lowest value in the unsorted part of array
                min = j                     # updating min index to the index of lowest element
        A[min], A[i] = A[i], A[min]         # swapping minimum element
    end = time.time()                       # time counter ends
    return (end-start)                      # returning time taken by Selection Sort


def quick_sort(arr, low, high):                           # Quick Sort
    start=time.time()                       # time counter starts
    i = low
    j = high
    p = arr[low + (high - low) // 2]        # pivot element in the middle
    while i <= j:                           # until all elements are checked
        while arr[i] < p:
            i += 1
        while arr[j] > p:
            j -= 1
        if i <= j:                          # swap elements
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    if low < j:                             # sort left side of array
        quick_sort(arr, low, j)
    if i < high:                            # sort right side of array
        quick_sort(arr, i, high)
    end=time.time()                         # time counter ends
    return end-start


def mergeSort(A):                                       # Merge Sort
    start = time.time()                     # time counter starts
    if len(A) > 1:                          # checking if array is empty or not
        mid = len(A) // 2                   # splitting array into two - LEFT AND RIGHT
        left = A[:mid]
        right = A[mid:]

        mergeSort(left)                     # recurring left side
        mergeSort(right)                    # recurring right side
        Merge(left, right, A)               # merging/rejoining the array - calling Merge function
    end = time.time()                       # time counter ends
    return (end-start)                      # returning time taken by Merge Sort


def Merge(left, right, A):                  # Merges or combines array elements
    i = j = k = 0
    while i < len(left) and j < len(right): # iteration until any one of left and right is empty
        if left[i] < right[j]:              # if 'left array element' is smaller than 'right array element'
            A[k] = left[i]                  # appending 'left array element' to main array
            i += 1                          # incrementing in order to point next element of left array
        else:                               # Similarly if 'left array element' is greater than 'right array element'
            A[k] = right[j]                 # appending 'right array element' to main array
            j += 1                          # incrementing in order to point next element of left array
        k += 1                              # incrementing main array index
    # Checking if any elements left
    while i < len(left):
        A[k] = left[i]                      # if any element found then appending it to the main array
        i += 1
        k += 1
    while j < len(right):
        A[k] = right[j]                     # if any element found then appending it to the main array
        j += 1
        k += 1


# Driver Code Starts Here
insertion_time = []                         # Initialising lists for storing time taken by sort function
bubble_time = []
selection_time = []
quick_time = []
merge_time = []

# Input for 'size of array' - all values of n at once
x = list(map(int, input("Enter all Array sizes with spaces(eg: 10 100 1000):: ").split()))
# x=[10, 5212]
# Initialising list which stores time taken by all sort functions in nested list format
n_time = []
print('\n')
for n in x:                                                 # Loop that iterates over list containing sizes of array
    print("Number of Elements :", n)
    arr = random.sample(range(n), n)                        # Making Random Array

    # List containing sort time of all sort functions (calling all sort functions) for current array size
    timetaken = [insertionsort(arr), quick_sort(arr, 0, n - 1), bubble_sort(arr),
                 selection_sort(arr), mergeSort(arr)]
    sort_name = ['Insertion Sort', 'Quick Sort', 'Bubble Sort', 'Selection Sort', 'Merge Sort']

    print('\nTime Taken ::')                                # Printing time taken for current array size
    for i in range(5):
        print('{:<15}{} {}'.format(sort_name[i], ':', timetaken[i]))

    n_time.append(timetaken)                                # Adding current time storage list to global list (n_time)

    # Just for partitioning for different array sizes
    print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

for i in range(len(n_time)):                                # splitting time taken for each sort from main list(n_time)
    insertion_time.append(n_time[i][0])
    quick_time.append(n_time[i][1])
    bubble_time.append(n_time[i][2])
    selection_time.append(n_time[i][3])
    merge_time.append(n_time[i][4])


# Plotting Starts here
# Plotting time on x-axis and time taken by each sort on y-axis

plt.yscale('log')                                        # For log graph
plt.plot(x, insertion_time, color='blue', marker='o', label='Insertion Sort')
plt.plot(x, bubble_time, color='orange', marker='o', label='Bubble Sort')
plt.plot(x, selection_time, color='red', marker='o', label='Selection Sort')
plt.plot(x, quick_time, color='green', marker='o', label='Quick Sort')
plt.plot(x, merge_time, color='yellow', marker='o', label='Merge Sort')
plt.legend()

plt.xlabel('Size of Array (n)')                             # Labelling both axes
plt.ylabel('Time Taken (in sec)')
# Title of Graph
plt.title('''
Time Complexity Comparision between the Given Sorting Algorithms
          (Time vs Array Size)
          ''')
plt.grid(True)                                              # Adding background grids

plt.show()                                                  # Showing Final graph

#----------------------------------Program Ends Here----------------------------------
