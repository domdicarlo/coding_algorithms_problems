# The N Steps Problem 

# The problem: Given a staircase of N number of steps, 
# if you can only take intervals of 1 or 2 steps, what 
# is the total number of permutations to get to the top?

# Further, extend this to a set of intervals X. For a given
# set of positive integers, what is the total number of
# permutations to get to the top?

# The basic problem, for X = {1, 2}:

# First, here is a (less than optimal) recursive solution:
def n_steps_basic_rec(n):
  if n < 0: # impossible staircase!
    return 0
  if n == 0: # if the staircase has no steps, there is only 1 way 
    return 1 
  if n == 1: # one step is also equal to 1
    return 1
  else:
    return n_steps_rec(n - 1) + n_steps_rec(n - 2)

# The basic idea is that at any point I can either take 1 step, or 
# 2 steps, so I follow those possible futures and add up their
# endings.

# This will take O(2^n) time, however. We are calculating the 
# same things multiple times.

# We can instead use a buffer to save numbers, while still
# more or less keeping the same algorithmic solution

def n_steps_basic_iter(n):
  if n < 0: # impossible staircase!
    return 0
  if n == 0: # if the staircase has no steps, there is only 1 way 
    return 1 
  if n == 1: # one step is also equal to 1
    return 1
  # else, we can utilize the buffer 
  # where for all other positive integer n,
  # f(n) = f(n-2) + f(n-1)
  else:
    buff = [1, 1, 1]
    for x in range (n - 1):
      buff[2] = buff[0] + buff[1]
      buff[0] = buff[1]
      buff[1] = buff[2]
    return buff[2]

# This changes our problem to one of O(n) time

# Now, we need to come up with a solution
# for a general set of numbers. 

# For x_0 to x_m in X, any given f(x) will be the
# summation of f(x - x_y) for y from 0 to x_m, using
# the same logic as our previous problem (following all possible
# futures, all possible step intervals from our vantage point). 
# For a more general solution, things will be somewhat tricker,
# since some values for N steps won't have any way up with
# our limits of intervals (e.g. take only even intervals for an odd N)

# Since we can't work out the base cases in advance, we must 
# change our solution some what. Rather for x not in X,
# f(n) = f(x - x_0) + f(x - x_1) + ... f(x - x_m) [for x - x_y > 0]

# and for x in X, the same thing, + 1 for the solution using one 
# interval of x length.
# f(n) = f(x - x_0) + f(x - x_1) + .. f(x - x_m) + 1 [for x - x_y > 0]


# Put in basic english, either the sum
# of all possible ways up the stairs after using one of the 
# available intervals in X, or that sum plus one fell swoop 
# of an interval that fits in perfectly (e.g. x = 6 for N = 6)

def n_steps_gen_rec(n, set_x):
  if (n < 0): # impossible staircase!
    return 0
  if (n == 0): # in this case, only one way up, do nothing!
    return 1
  elif (n in set_x):
    return 1 + sum(n_steps_gen_rec(n - x, set_x)
                   for x in set_x if n > x)
  else:
    return sum(n_steps_gen_rec(n - x, set_x)
               for x in set_x if n > x)

# which gives us an O(|set_x|^n) time solution
# again, this is not the most efficient solution. we need to do
# something iteratively to avoid so many repeated computations

# We can do something like we did before, with a buffer
# array of a bigger size.

def n_steps_gen_iter(n, set_x):
  # range n+1 since index[0] is 0 steps,
  # index[n] is for n steps
  buff = [0 for i in range(n + 1)]
  buff[0] = 1
  for i in range(n + 1):
    # essentially works out the base cases
    # for each member of the set_x
    if (i in set_x):
      buff[i] += 1 
    # computes using our algorithm
    buff[i] += sum(buff[i - x] for x in set_x if i - x > 0)
  return buff[-1]



