class Node:

  def __init__(self, value):
    self.value = value
    self.next = None  # next node points to node below the current node


# Stack using linked list


class Stack:

  def __init__(self, value):
    new_node = Node(value)
    self.top = new_node
    self.height = 1

  def append(self, value):
    new_node = Node(value)
    if self.height == 0:
      self.top = new_node
    else:
      # next should point to the top node on the stack
      # the top node will now be under new node
      new_node.next = self.top
      self.top = new_node
    self.height += 1
    return True

  def pop(self):
    if self.height == 0:
      return None
    temp = self.top
    self.top = self.top.next  # top now points to the bottom node
    temp.next = None
    self.height -= 1
    return temp

  def print_stack(self):
    if self.height == 0:
      return None
    temp = self.top
    while temp is not None:
      print(temp.value)
      temp = temp.next

  def is_empty(self):
    if self.height == 0:
      return True
    return False

  def peek(self):
    if self.is_empty():
      return None
    return self.top.value
