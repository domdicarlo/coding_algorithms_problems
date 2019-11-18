# This problem was solved on LeetCode:
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# The problem:
# Given a binary tree, find the maximum depth of the tree.
# The furthest path down the tree.

# The recursive solution
# While this problem lends itself to a recursive solution,
# such a solution might prove a problem. If we had a huge tree, 
# we might need to store a large number of values on the stack, and 
# possibly trigger a stack overflow. Nonetheless, the solution
# at least looks nice and here it is:

# Time complexity: We will travel to every node in the tree, so for n nodes, it's
# just O(n). 

# Space complexity: Imagine we had a full binary tree. In that case, we wouldn't 
# reach root==0 until the last leaves in the tree. So space complexity
# becomes O(n) in the worst case.

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # Base case
        if root == None:
            return 0
        # Recursive case, tree has at least depth 1, then we take
        # the depth of whichever subtree is bigger
        answer = 1 + max(Solution.maxDepth(self, root.left), 
                         Solution.maxDepth(self, root.right))
        return answer

# The stack/queue based solution:
# This version turned out to save some time on leet code, (44 -> 40 ms)
# but saved even more memory, going from 14.4 MB in aux space to 13.9 MB
# which was better than 100% of submissions on LeetCode, supposedly.

# Time complexity is still as O(n), because we have to touch 
# every node in the tree.

# Space complexity saves space, because we only
# ever store a maximum of the current generation. Of course,
# the last generation of a tree can hold n/2 + 1 nodes, which means
# techincally the space complexity is still O(n) in the worst case
# when we discard the constant. What we do avoid 
# here is a stack overflow, which is the benefit of this solution.

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        current_gen = []
        next_gen = []
        max_depth = 0
        found_one = 0
        
        if root != None:
            # have at least depth 1
            max_depth += 1

            # check left and right of root, add to
            # current gen list
            if root.left != None:
                current_gen.append(root.left)
                # we only want to add one
                # to max_depth once per generation,
                # hence this found_one routine
                if not found_one:
                    found_one = 1
                    max_depth += 1
            if root.right != None:
                current_gen.append(root.right)
                if not found_one:
                    found_one = 1
                    max_depth += 1
            # set found_one equal to 0 as
            # we advance generation
            found_one = 0

        while(current_gen != []):
            # take the next node in the queue
            cur_node = current_gen[-1]

            # check both of left and right children
            if cur_node.left != None:
                if(not found_one):
                    max_depth += 1
                    found_one = 1
                next_gen.append(cur_node.left)

            if cur_node.right != None:
                if(not found_one):
                    max_depth += 1
                    found_one = 1
                next_gen.append(cur_node.right)

            # onto the next node or generation,
            # depending
            current_gen.pop(-1)
            if current_gen == []:
                current_gen = next_gen
                next_gen = []
                found_one = 0

        return max_depth
                
                