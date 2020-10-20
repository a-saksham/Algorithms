# Qs 3rd - Fining all unique combinations where sum of candidate no.'s results target


# Finding Sum of all possible combinations
def combinationSum(candidates, target):
    result = []
    resList = []

    def backtracking(start, rest):
        if rest == 0:
            temp = resList[:]
            result.append(temp)
        for i in range(start, len(candidates)):
            if candidates[i] <= rest:
                resList.append(candidates[i])

                # Backtrack count
                global bt_count
                bt_count += 1
                backtracking(i, rest - candidates[i])       # BACKTRACKING
                resList.pop()


    backtracking(0, target)
    return result


# Print functions
def printCombinations(answer):
    for i in range(len(answer)):
        print("{:>4}. {}".format(i+1, answer[i]))


# DRIVER CODE
print('')
bt_count = 0
candidates = list(map(int, input('All Candidates space separated:: ').split()))
target = int(input("Target:: "))
answer = combinationSum(candidates, target)
print("\n-> All possible combinations where sum equals {} are:".format(target))
printCombinations(answer)

print('\n-> Total Backtrack Count =',bt_count)