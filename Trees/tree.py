class Node:

  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


class BinaryTree:
  '''
  Binary Tree has less than or equal to 2 child nodes
  All values less than the current node will be on the left sub tree
  All value greater than current node will be on the right sub tree
  The above rule must be followed to insert or search a node in the tree
  '''

  def __init__(self):
    self.root = None  # dont have to create node at this point, as I have insert method for that

  def contains(self, value):
    if self.root is None:
      return False
    # If no root, means not nodes exist. Hence return False
    temp = self.root
    while temp:
      if value < temp.value:
        # If value less than root
        # Then most likely it is in left sub tree
        temp = temp.left
      elif value > temp.value:
        # If value greater than root
        # Most likely the value is on the right sub tree
        temp = temp.right
      else:
        return True
    # if we exit while loop, then value does not exist
    return False

  def insert(self, value):
    newnode = Node(value)
    if self.root is None:
      # If root does not exist, then this is the first node
      self.root = newnode
      return True
    temp = self.root
    while True:
      if temp.value == newnode.value:
        # already exists
        # cannot return duplicates
        return False
      if temp.value > newnode.value:
        # If value less than root, it should be inserted in left subtree
        if temp.left is None:
          # no left node, then insert the new node
          temp.left = newnode
          return True
        temp = temp.left
      else:
        # If value greater than root, it should be inserted in right subtree
        if temp.right is None:
          temp.right = newnode
          return True
        temp = temp.right
