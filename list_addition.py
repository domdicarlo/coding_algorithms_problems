# The problem:

# Given a list of numbers, determine whether
# any two of them will add up to a number k

# A basic solution:

def add_k(list_num, k):
  for index in range(len(list_num)):
    for other_index in range(len(list_num)):
      if index != other_index:
        if(list_num[index] + list_num[other_index] == k):
          return True
  else:
    return False

# This essentially works by going through each element in the list 
# and trying to add it to all other numbers in the list. While this
# works, we are at O(n^2) time for the worst case, in case it's the last
# numbers in the list where we find our addition. We are going through
# some calculations twice.

# Let's see if we can get it done in one pass without repeating ourselves

def add_k_plus_plus(list_num, k):
  for index in range(len(list_num)):
    for other_index in range(index):
      if(list_num[index] + list_num[other_index] == k):
        return True
  else:
    return False

# this time we only go up until that number, so that for x_y in 
# list_num, we only add numbers from x_0 to x_(y-1) to x_y 

# this way we go through with only one pass on the array, and 
# change our time to O((n-1)!)

# tests

list_ones = [1, 1, 1, 1]
list_basic = [1, 2, 3, 4, 5]
list_wild = [1, 2, -3, 4000, 0.5, 0]
empty_list = []



assert add_k(list_ones, 2) == True, "Should be True"
assert add_k(list_ones, 4) == False, "Should be False"
assert add_k(empty_list, 4) == False, "Should be False"
assert add_k(list_basic, 4) == True, "Should be True"
assert add_k(list_basic, 10) == False, "Should be False"
assert add_k(list_wild, 100) == False, "Should be False"
assert add_k(list_wild, 4000.5) == True, "Should be True"

assert add_k_plus_plus(list_ones, 2) == True, "Should be True"
assert add_k_plus_plus(list_ones, 4) == False, "Should be False"
assert add_k_plus_plus(empty_list, 4) == False, "Should be False"
assert add_k_plus_plus(list_basic, 4) == True, "Should be True"
assert add_k_plus_plus(list_basic, 10) == False, "Should be False"
assert add_k_plus_plus(list_wild, 100) == False, "Should be False"
assert add_k_plus_plus(list_wild, 4000.5) == True, "Should be True"


# A more efficient solution

