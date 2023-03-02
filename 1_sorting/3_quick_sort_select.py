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


qs = QuickSortSelect()
arr = [3, 7, 2, 1, 9, 4, 6, 8, 5]
qs.quickSort(arr, 0, len(arr) - 1)
print(arr)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
