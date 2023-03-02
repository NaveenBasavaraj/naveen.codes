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

  def get_index(self, index):
    # returns the node at this index
    if index < 0 or index > self.length:
      return False
    temp = self.head
    for _ in range(index):
      temp = temp.next
    return temp

  def insert(self, index, value):
    # insert given value at given index
    if index < 0 or index > self.length:
      # this is checked in get_index
      # adding again for performance
      return False
    if index == 0:
      return self.prepend(value)
    if index == self.length:
      return self.append(value)
    new_node = Node(value)
    prev = self.get_index(index - 1)
    new_node.next = prev.next
    prev.next = new_node
    self.length += 1
    return True

  def remove(self, index):
    # Remove the node at given index
    if index < 0 or index > self.length:
      return None
    if index == 0:
      return self.pop_first()
    if index == self.length - 1:
      return self.pop()
    # get previous node
    pre = self.get(index - 1)
    # temp now becomes next node of previous
    temp = pre.next
    pre.next = temp.next
    temp.next = None
    self.lenght -= 1
    return temp

  def reverse(self):
    # first swap head and tail
    temp = self.head
    self.head = self.tail
    self.tail = temp
    # now take before and after pointer
    # iterate over list and make temp = after
    before = None
    after = temp.next
    for _ in range(self.length):
      after = temp.next
      temp.next = before
      before = temp
      temp = after

  def print_list(self, value):
    temp = self.head
    while temp is not None:
      print(temp.value)
      temp = temp.next
