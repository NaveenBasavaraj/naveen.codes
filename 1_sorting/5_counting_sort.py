def counting_sort(arr):
  """
    Sorts an array of non-negative integers using Counting Sort.

    Counting Sort is a linear-time sorting algorithm that works by counting the occurrences of each element in the
    input array, then using that information to determine the final position of each element in the sorted array.

    Args:
        arr: An array of non-negative integers.

    Returns:
        The sorted array.

    Example:
        >>> arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        >>> counting_sort(arr)
        [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    """
  # Find the maximum value in the input array
  max_val = max(arr)

  # Initialize a count array of size max_val+1, with all elements set to 0
  count = [0] * (max_val + 1)

  # Count the occurrences of each element in the input array
  for x in arr:
    count[x] += 1

  # Compute the cumulative sum of the count array
  for i in range(1, len(count)):
    count[i] += count[i - 1]

  # Create a result array of the same size as the input array, with all elements set to 0
  result = [0] * len(arr)

  # Iterate backwards over the input array, placing each element in its sorted position in the result array
  for x in reversed(arr):
    result[count[x] - 1] = x
    count[x] -= 1

  return result
