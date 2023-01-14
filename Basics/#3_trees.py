'''
1) Full Binary Tree: Each node has 0 or 2 children
2) Perfect: At each level, each node has 2 children
3) Complete: 
   * filling the tree from left to right at each level with no gaps
   * Can be a full binary tree
   * Can be a perfect binary tree
   * A tree can be complete and not full or perfect.
root: Top most node. There can be only one root node

parent: A node which has zero or upto two chidren.
A parent can be a child to another node.

child: A parent can have two child nodes. A child node can be a parent node.

Child: A child without leaf node.

BST: Binary search tree
* Value less than root is on the left sub tree
* value greater than root is on the right sub tree
* Same rule applies to each node

No of nodes at root --> 
'''


class Node:

  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


class BST:

  def __init__(self):
    # we dont have to add node at the time of creation
    # we can use insert to do that
    self.root = None

  def insert(self, value):
    new_node = Node(value)
    if not self.root:
      self.root = new_node
      return True
    temp = self.root
    while True:
      if new_node.value == temp.value:
        return False
      
      
