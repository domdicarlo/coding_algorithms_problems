# The problem:

# Given a root to a binary tree, implement serialize(tree) which
# turns the tree into a string representation. The kicker is 
# that you must implement deserialize(tree), which turns the 
# the string back into its former tree

# Relevant data structure:
class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

# Algorithm:

# For serialize:
# 1) We need to do a breadth first search of the tree
#    in order to maintain an order for the string
# 2) We build the string breadth first, and in doing so
#    we need to store pointers to each generation of children
#    so we can go back and distribute children 
# 3) Empty node will need to be assigned some value,
#    other wise the order of the tree will be lost
#    if the tree is not evenly distributed
# 4) Because of 3), we will have an extra generation of None
#    values encoded for every tree that gets serialized
# 5) We need to seperate values in the string somehow

# For deserialize:
# 1) serialize did most of the work here, now we 
#    just need to unpack the string
# 2) we need to first split the string into 
#    an array for ease of exploration
# 3) we need to store pointers to tree children
#    as we build the tree, so we can populate one
#    node and then go back to the next node in the generation

# ASSUMPTIONS:
# !) A val for Node can't be ""
# 2) No commas can be used in a string value for Node.val


def serialize(tree):
  # a queue for putting in node_queue. we need to do 
  # a breadth-first search

  node_queue = [tree.left, tree.right]

  serialized = str(tree.val) 

  # a temp variable for traversing the tree
  # a temp variable for traversing node_queue
  current_index = 0

  while node_queue:
    # add the separator. putting it here prevents it from
    # an extra comma at the end of the string
    serialized += ","

    if (node_queue[0] != None):
      node_queue.append(node_queue[0].left)
      node_queue.append(node_queue[0].right)
      serialized += str(node_queue[0].val) 
    # empty string will represent node = None
    else:
      serialized += ""

    node_queue.pop(0) 
  
  return(serialized)

def deserialize(tree_string):
  # turning the tree string into a list
  tree_list = tree_string.split(",")

  # initialize the return tree to have the same value
  # as the first item in the tree list

  if (tree_list[0] != ""):
    return_tree = Node(tree_list[0], None, None)
  else:
    print("Error, this string was never a tree!")
    return None

  # get rid of first value
  tree_list.pop(0)

  # initialize the node queue
  node_queue = [return_tree]

  while tree_list:
    # change the current working node
    current_node = node_queue[0]

    # set left of tree 
    if (tree_list[0] != ""):
      current_node.left = Node(tree_list[0], None, None)
    # otherwise, no need to change it from None

    # set right of tree
    if (tree_list[1] != ""):
      current_node.right = Node(tree_list[1], None, None)
    # otherwise, no need to change it from None

    # remove from the list of tree elements
    tree_list.pop(0)
    tree_list.pop(0)

    # add to our list of node_queue nodes
    node_queue.append(current_node.left)
    node_queue.append(current_node.right)

    # remove node we have worked out from node_queue list
    node_queue.pop(0)
    # change the current working node
    current_node = node_queue[0]
  
  return return_tree



  

    



  



# Testing (not thorough)

left_left = Node("left_left", None, None)
left_right = Node("left_right", None, None)
right_left = Node("right_left", None, None)
right_right = Node("right_right", None, None)
left = Node("left", left_left, left_right)
right = Node("right", right_left, right_right)

tree = Node("root", left, right)

tree_string = serialize(tree)

print(serialize(deserialize(serialize(tree))))
print(serialize(tree))
print("".split(","))





  
