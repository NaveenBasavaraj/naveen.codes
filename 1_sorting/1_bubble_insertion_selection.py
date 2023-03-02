class BasicSorts:
  """
    This class provides implementation of basic sorting algorithms such as Bubble Sort,
    Selection Sort, and Insertion Sort.
    """

  def swap(self, my_list, index1, index2):
    """
        Swaps the elements of my_list at the given index positions.

        Parameters:
        my_list (list): A list of elements to swap
        index1 (int): An index position of the first element
        index2 (int): An index position of the second element

        Returns:
        list: A list with swapped elements
        """
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp
    return my_list

  def bubbleSort(self, my_list):
    """
        Sorts the elements of my_list in ascending order using Bubble Sort algorithm.

        Parameters:
        my_list (list): A list of elements to sort

        Returns:
        list: A list of sorted elements
        """
    # Traverse through all array elements
    for i in range(len(my_list) - 1, 0, -1):

      # Last i elements are already in place
      for j in range(i):

        # Swap if the element found is greater than the next element
        if my_list[j] > my_list[j + 1]:
          my_list = self.swap(my_list, j, j + 1)

    return my_list

  def selection_sort(self, my_list):
    """
        Sorts the elements of my_list in ascending order using Selection Sort algorithm.

        Parameters:
        my_list (list): A list of elements to sort

        Returns:
        list: A list of sorted elements
        """
    # Traverse through all array elements
    for i in range(len(my_list) - 1):

      # Find the minimum element in the unsorted part of the array
      min_index = i
      for j in range(i + 1, len(my_list)):
        if my_list[j] < my_list[min_index]:
          min_index = j

      # Swap the found minimum element with the first element
      # of the unsorted part of the array
      if i != min_index:
        my_list = self.swap(my_list, i, min_index)

    return my_list

  def insertionSort(self, my_list):
    """
        Sorts the elements of my_list in ascending order using Insertion Sort algorithm.

        Parameters:
        my_list (list): A list of elements to sort

        Returns:
        list: A list of sorted elements
        """
    # Traverse through all array elements
    for i in range(1, len(my_list)):
      key = my_list[i]
      j = i - 1

      # Move elements of my_list[0..i-1], that are greater than key,
      # to one position ahead of their current position
      while j >= 0 and key < my_list[j]:
        my_list[j + 1] = my_list[j]
        j -= 1

      # Place the key element at its correct position
      my_list[j + 1] = key

    return my_list


bs = BasicSorts()
my_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bs.bubbleSort(my_list)
print(sorted_list)
my_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bs.selection_sort(my_list)
print(sorted_list)
my_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bs.insertionSort(my_list)
print(sorted_list)
