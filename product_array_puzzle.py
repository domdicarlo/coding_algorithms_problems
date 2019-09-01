# The problem:

# Based on an array of integers, create a new array where new_array[i]
# is equal to the product of all the values in old_array except at 
# old_array[i]

# Better yet, do it without division and in O(n) time. Also, do it
# with auxilliary space complexity O(1).

# The algorithm:

# 1) Calculate the array product to the left of every index 
#    excluding that index
# 2) Calculate the array product to the right of every index
#    excluding that index
# 3) Multiply these two arrays together to get the product
#    excluding the one index. Can save space by combining steps
#    2 and 3.

def product_array(base_array):
  # grab this for ease of reference
  n = len(base_array)

  # if the array is empty, return empty array
  if n == 0:
    return []

  # if the array is of size 1, it's 0
  if n == 1:
    return [0]

  # initialize the product return array 
  prod_array = [1 for i in range(n)]
  
  # initialize initial value for temp values, standing in 
  # for previous left and right product values as we loop through
  # and calculate these products 
  previous_left = 1 # the product of the left up to i (here i = 0)
  previous_right = 1 # the product of the right down to i (here i = n-1)

  for i in range(1, n):
    prod_array[i] *= previous_left * base_array[i - 1]
    previous_left *= base_array[i - 1] 
  
  for i in range(n - 2, -1, -1):
    prod_array[i] *= previous_right * base_array[i + 1]
    previous_right *= base_array[i + 1]

  return prod_array


# Tests

test_array_basic = [1, 1, 1, 1]
test_array_basic2 = [1, 2, 3, 4]
test_array_base1 = [1]
test_array_base2 = []

assert product_array(test_array_basic) == test_array_basic
assert product_array(test_array_basic2) == [24, 12, 8, 6]
assert product_array(test_array_base1) == [0]
assert product_array(test_array_base2) == []

  
  
    
