def merge_sort_helper(array1, array2):
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

  while i < len(array1):
    combined.append(array1[i])
    i += 1
  while j < len(array2):
    combined.append(array2[j])
    j += 1
  return combined


def merge_sort_main(array):
  '''
  We pass single array, which is split in the middle
  and sorted using merger_sort_helper.
  we recursively call merge_sort_main on each split till there only one element left
  '''
  if len(array) == 1:
    return array
  mid = int(len(array) / 2)
  left = array[:mid]
  right = array[mid:]
  return merge_sort_helper(merge_sort_main(left), merge_sort_main(right))


print(merge_sort_main([3, 2, 8, 9, 1, 7, 5]))
