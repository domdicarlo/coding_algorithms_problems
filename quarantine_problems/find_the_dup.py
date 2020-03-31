
# Practice Coding problem for 3/31/2020

# A Leetcode problem: https://leetcode.com/problems/find-the-duplicate-number/

#  Given an array nums containing n + 1 integers where 
#  each integer is between 1 and n (inclusive), prove that
#  at least one duplicate number must exist. Assume
#  that there is only one duplicate number, find the 
#  duplicate one.

# Constraints:
    # You must not modify the array (assume the array is read only).
    # You must use only constant, O(1) extra space.
    # Your runtime complexity should be less than O(n2).
    # There is only one duplicate number in the array, but it could be repeated more than once.

# I found this problem pretty hard, in particular to meet all the
# constraints. Two solutions lend themself close at hand that
# don't meet the constraints, namely sorting and using a hash
# set to keep track of numbers that have already appeared. 

# The proof that at least one duplicate exists is a simple application
# of the pigeonhole principle. Namely if you have more pigeon
#  holes than pigeons, (or slots in an array than unique numbers to meet
# those slots), you will have at least one hole without a pigeon
# (or slot with a non-unique number)

# The solution that meets all the constraints is one based on cycle detection.
# If we imagine the array as a graph where each index:value pair is an edge from
# index -> value, then we see that if two indices point to the same value, we will
# have a cycle. 

# Now we cannot build a graph from the array, since this would take
# up linear space, and we want O(1) extra space only. Instead, we need
# to use some obscure algo I learned from here: 
# https://www.youtube.com/watch?v=9YTjXqqJEFE&feature=youtu.be

# The algorithm is Floyd's Tortoise and Hare Algorithm. The idea is to
# keep track of two pointers, a slow and fast pointer, where you move the
# slow pointer by 1 and the fast by 2 every iteration. Eventually, the two 
# pointers will intersect (meet on the same value), 
# which means they are both within the cycle
# (since the fast pointer will have covered all the distance the slow
#  pointer already covered by the time they meet, and is on at least
#  its second loop through the cycle). 

#  This intersection point is not the duplicate value, but instead
# leads us to the duplicate value via some modular arithmetic (where things
# get complicated). I will leave the details to the linked video above.

# But for now, the algorithm works as follows:

# 1) Run the pointers until they intersect.
# 2) Leave the tortoise pointer where it's at. Move
#    the hare pointer to the start of the graph.
# 3) Move both pointers one space at a time. Where they
#    intersect next is the duplicate value

# Code: 

class Solution:
    def findDuplicate(self, nums):
        # setting tortoise and hare
        tortoise = nums[0]
        hare = nums[0]
        
        # first intersection point
        not_found = True
        while not_found:
            tortoise = nums[tortoise]
            # notice we move hare twice
            hare = nums[hare]
            hare = nums[hare]
            if (tortoise == hare):
                break

        # find the next intersect 
        p1 = tortoise
        p2 = nums[0]
        
        while not p1 == p2:
            p1 = nums[p1]
            p2 = nums[p2]
        
        return p1
1