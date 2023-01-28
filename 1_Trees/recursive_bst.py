from tree import BinaryTree


class recursive_BST(BinaryTree):

  def __r_contains(self, curr_node, value):
    if curr_node == None:
      return False
    if value == curr_node.value:
      return True
    if value < curr_node.value:
      return self.__r_contains(curr_node.left, value)
