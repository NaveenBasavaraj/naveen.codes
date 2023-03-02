def merge_sort_helper(array1, array2):
  """
  Helper function for merge sort that combines two sorted arrays into one sorted array

  Args:
  array1 (list): A sorted list of integers
  array2 (list): A sorted list of integers

  Returns:
  combined (list): A sorted list that combines elements of array1 and array2

  """
  combined = []
  i = 0
  j = 0
  while i < len(array1) and j < len(array2):
    if array1[i] < array2[j]:
      combined.append(array1[i])
      i += 1
    else:
      combined.append(array2[j])
      j += 1

  # Append any remaining elements from the arrays
  while i < len(array1):
    combined.append(array1[i])
    i += 1
  while j < len(array2):
    combined.append(array2[j])
    j += 1
  return combined


def merge_sort_main(array):
  """
  Recursive merge sort function that sorts a list of integers using divide and conquer

  Args:
  array (list): A list of integers to be sorted

  Returns:
  sorted_array (list): A sorted list of integers

  """
  # Base case: return the list if it only has one element
  if len(array) == 1:
    return array

  # Recursive case: divide the list in half and sort each half
  mid = int(len(array) / 2)
  left = array[:mid]
  right = array[mid:]
  return merge_sort_helper(merge_sort_main(left), merge_sort_main(right))


# Example usage
array = [3, 2, 8, 9, 1, 7, 5]
sorted_array = merge_sort_main(array)
print(sorted_array)
