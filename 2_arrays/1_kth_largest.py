class QuickSortSelect:
  '''
  QuickSort and QuickSelect algorithm,
  with common partition method
  '''

  def partition(self, arr, left, right):
    # Select the pivot value as the last element in the array
    pivot_value = arr[right]
    # Initialize the swap index to the leftmost index
    swap_index = left
    # Loop through the array from left to right - 1
    for i in range(left, right):
      # If the current element is less than the pivot value,
      # swap it with the element at the swap index
      # and move the swap index one position to the right
      if arr[i] < pivot_value:
        arr[i], arr[swap_index] = arr[swap_index], arr[i]
        swap_index += 1
    # Swap the pivot value with the element at the swap index
    arr[swap_index], arr[right] = arr[right], arr[swap_index]
    # Now the value at swap index is in its correct place
    # Return the index of the pivot value
    return swap_index

  def quickSort(self, arr, left, right):
    # If there are at least two elements in the array
    if left < right:
      # Partition the array around a pivot
      pivot = self.partition(arr, left, right)
      # Recursively sort the left partition
      self.quickSort(arr, left, pivot - 1)
      # Recursively sor the right partition
      self.quickSort(arr, pivot + 1, right)

  def quickSelectSmallest(self, arr, left, right, k):
    # given K, find the kth smallest element in the list
    # If there is only one element in the array
    if left == right:
      return arr[left]
    # Partition the array around the pivot
    pivot = self.partition(arr, left, right)
    # If pivot is the kth smallest element is in the left partition,
    # recusively search the left partiton
    if k == pivot:
      return arr[k]
    # If the kth smallest elemnt is the left partition,
    # recursively search the left partition
    elif k < pivot:
      return self.quickSelectSmallest(arr, left, pivot - 1, k)
    # If the kth smallest element is the right partition,
    # recursively search the right partion
    else:
      return self.quickSelectSmallest(arr, pivot + 1, right, k)

  def quickSelectLargest(self, arr, left, right, k):
    # adjust k to find the k-th largest instead of the k-th smallest
    k = len(arr) - k
    if left == right:
      return arr[left]
    pivot = self.partition(arr, left, right)
    if k == pivot:
      return arr[k]
    elif k < pivot:
      return self.quickSelectLargest(arr, left, pivot - 1, k)
    else:
      return self.quickSelectLargest(arr, pivot + 1, right, k)


qs = QuickSortSelect()
arr = [3, 7, 2, 1, 9, 4, 6, 8, 5]
qs.quickSort(arr, 0, len(arr) - 1)
print(arr)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr = [3, 7, 2, 1, 9, 4, 6, 8, 5]
# Find the kth smallest element using quickSelect
k = 3
kth_smallest = qs.quickSelectSmallest(arr, 0, len(arr) - 1, k)
print(kth_smallest)  # Output: 3

kth_largest = qs.quickSelectLargest(arr, 0, len(arr) - 1, k)
print(kth_largest)  # Output: 7