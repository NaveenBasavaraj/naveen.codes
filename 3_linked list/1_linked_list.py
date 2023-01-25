# singly linked list
class Node:

  def __init__(self, value):
    self.value = value
    self.next = None


class LinkedList:

  def __init__(self, value):
    new_node = Node(value)
    self.head = new_node
    self.tail = new_node
    self.length = 1

  def append(self, value):
    # Add new node in the end
    new_node = Node(value)
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
    self.length += 1
    return True

  def prepend(self, value):
    # Add new value in the beginning
    new_node = Node(value)
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head = new_node
    self.length += 1
    return True

  def pop(self, value):
    # remove last node
    if self.length == 0:
      return None
    temp = self.head  # Fast pointer
    prev = self.head  # Slow pointer
    while temp.next:
      prev = temp
      temp = temp.next
    prev.next = None
    self.tail = prev
    self.length -= 1
    if self.length == 0:
      self.head = None
      self.tail = None
    return temp

  def pop_first(self):
    # Pop from the front
    if self.length == 0:
      return None
    temp = self.head
    self.head = self.head.next
    temp.next = None
    self.length -= 1
    if self.length == 0:
      self.tail = None
    return temp

  def print_list(self, value):
    temp = self.head
    while temp is not None:
      print(temp.value)
      temp = temp.next
