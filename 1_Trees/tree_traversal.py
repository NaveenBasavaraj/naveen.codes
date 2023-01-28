from tree import BinaryTree


class TreeTraversal(BinaryTree):

  def breadthFirstSearch(self):
    # We need a queue list and results list
    # We queue the next node to be appended to the results
    queue, results = [], []
    curr_node = self.root
    queue.append(self.root)  # start with root
    while len(queue) > 0:  # repeat as long as values in queue
      curr_node = queue.pop(0)
      results.append(curr_node)  # pop first value and append to results
      if curr_node.left is not None:
        queue.append(curr_node.left)
      if curr_node.right is not None:
        queue.append(curr_node.right)
    return results

  # Depth First Search Algorithms

  # for dfs recursive algos, we don't need queue
  # only results is enough
  # we append value to results recursively

  def pre_order(self):
    # ROOT - LEFT - RIGHT (RLR)
    results = []

    def traverse(curr_node):
      results.append(curr_node.value)
      if curr_node.left is not None:
        traverse(curr_node.left)
      if curr_node.right is not None:
        traverse(curr_node.right)

    traverse(self.root)
    return results

  def post_order(self):
    # RIGHT - LEFT - ROOT (RLR)
    results = []

    def traverse(curr_node):
      if curr_node.left is not None:
        traverse(curr_node.left)
      if curr_node.right is not None:
        traverse(curr_node.right)
      results.append(curr_node.value)

    traverse(self.root)
    return results

  def in_order(self):
    # LEFT- ROOT -RIGHT (LRR)
    results = []

    def traverse(curr_node):
      if curr_node.left is not None:
        traverse(curr_node.left)
      results.append(curr_node.value)
      if curr_node.right is not None:
        traverse(curr_node.right)

    traverse(self.root)
    return results
