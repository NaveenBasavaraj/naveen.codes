class BasicSorts:
  '''
  Quick view of Bubble, Selection, Insertion Sort
  '''

  def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp
    return my_list

  def bubbleSort(self, my_list):
    for i in range(len(my_list) - 1, 0, -1):
      for j in range(i):
        if my_list[j] > my_list[j + 1]:
          my_list = self.swap(my_list, j, j + 1)
    return my_list

  def selection_sort(self, my_list):
    for i in range(len(my_list) - 1):
      min_index = i
      for j in range(i + 1, len(my_list)):
        if my_list[j] < my_list[min_index]:
          min_index = j
        if i != min_index:
          my_list = self.swap(my_list, i, min_index)
    return my_list

  def insertionSort(self, my_list):
    for i in range(1, len(my_list)):
      temp = my_list[i]
      j = i - 1
      while temp < my_list[j] and j > -1:
        my_list[j + 1] = my_list[j]
        my_list[j] = temp
        j -= 1
    return my_list
