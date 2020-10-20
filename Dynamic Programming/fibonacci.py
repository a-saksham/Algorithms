# Q1. FIBONACCI


# Brute Force Approach
def bruteForce(num):
    global bf_count
    bf_count += 1
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        fib_num = bruteForce(num-1) + bruteForce(num-2)
        return fib_num


# Dynamic Programming
def bottomUp(num):           # TABULATION : Bottom-Up Approach
    global bu_count
    bu_count += 1
    if num == 0:
        return 0
    if num == 1:
        return 1
    fib = []
    for i in range(num+1):
        fib.append(0)
    fib[0] = 0
    fib[1] = 1

    for i in range(2, num+1):
        fib[i] = fib[i-1] + fib[i-2]

    return fib[num]


def topDown(num):           # MEMOIZATION : Top-Down Approach
    global td_count
    td_count += 1
    if num in fib_dict:
        return fib_dict[num]
    else:
        fib_dict[num] = topDown(num-1) + topDown(num-2)
        return fib_dict[num]


# DRIVER CODE
print("* NOTE: Enter q to exit the Program *\n")
print("Enter nth term ::")

while True:
    try:
        td_count = 0
        bu_count = 0
        bf_count = 0

        fib_dict = {0: 0, 1: 1}
        num = int(input('>> '))
        print("The {}th Fibonacci term is {}".format(num, bottomUp(num)))

        topDown(num)
        print('\n{:38}:'.format('Total number of calls in TOP-DOWN'), td_count)

        print('{:38}:'.format('Total number of calls in BOTTOM-UP'), bu_count)


        bruteForce(num)
        print('{:38}:'.format('Total number of calls in BRUTE FORCE'), bf_count)
        print('')

    except:
        print('\nExecuted Successfully')
        break
