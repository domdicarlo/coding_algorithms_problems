# Practice Coding problem for 3/28/2020

# Given a positive integer n, find the smallest number of squared integers which sum to n.

# For example, given n = 13, return 2 since 13 = 32 + 22 = 9 + 4.

# Given n = 27, return 3 since 27 = 32 + 32 + 32 = 9 + 9 + 9.

# Solution (Dynamic Programming)

# So for this problem we want to use memoization,
# where the sub problems are smaller and smaller values for n
# We can find the smallest number of squared integers for
# small values of n, and then use these to help solve for larger
# values of n

# For any n, we go through all numbers for which we can subtract their
# square from n, starting from the largest such number. Then, for the remainder
# of the subtraction, we look through our memoization matrix and see what the
# smallest number of squared integers for that value was.

# Time Analysis: At worst we will have to compute n squaring operations
#                per int (altho we will actually have to do something like half
#                that number). We have to do this a total of n times
#                (this is seen in the code with the two for loops). So we have
#                O(n^2) ops if we consider the multiplication to be of unit cost.

# Space Analysis: We will have to keep the full memo matrix all the way through,
#                 so the space complexity is simply O(n)                  

def findSizeOfSum(n: int):
    memo_mat = [0 for i in range(0, n + 1)] # set the number to 0 for int 0
    for i in range(1, n + 1):
        soln = float("inf")
        for j in range(i, 0, -1):
            if j * j <= i:
                sub_problem = i - (j * j)
                new_soln = memo_mat[sub_problem] + 1
                soln = min(new_soln, soln)
        memo_mat[i] = soln
    return memo_mat[-1]

print("Sum size for 27: " + str(findSizeOfSum(27)))
print("Sum size for 13: " + str(findSizeOfSum(13)))
print("Sum size for 0: " + str(findSizeOfSum(0)))
print("Sum size for 1: " + str(findSizeOfSum(1)))
print("Sum size for 100: " + str(findSizeOfSum(100)))
print("Sum size for 10,000: " + str(findSizeOfSum(10000)))