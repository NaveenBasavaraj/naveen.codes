'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.
Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]
'''


def sort_colors(nums):
  """
    Sorts an array of integers in-place using the Dutch National Flag algorithm.

    Given an array nums containing only 0's, 1's, and 2's, sort the array in-place so that all 0's come before all 1's,
    which come before all 2's. This is known as the Dutch National Flag problem.

    The algorithm works by using three pointers to partition the array into three sections:
    - a section containing all 0's, represented by a pointer l at the beginning of the array
    - a section containing all 1's, represented by a pointer i that scans through the array
    - a section containing all 2's, represented by a pointer r at the end of the array

    We start by initializing l and i to the beginning of the array, and r to the end of the array. We then scan through
    the array using i, swapping elements as necessary to move all 0's to the left of l and all 2's to the right of r.
    At the end of the scan, we are left with a sorted array.

    Args:
        nums: An array of integers containing only 0's, 1's, and 2's.

    Returns:
        None. The input array is sorted in-place.

    Example:
        >>> nums = [2,0,2,1,1,0]
        >>> sort_colors(nums)
        >>> nums
        [0, 0, 1, 1, 2, 2]
    """
  # Initialize two pointers, l and r, to the beginning and end of the array respectively
  l = 0
  r = len(nums) - 1

  # Initialize a pointer i to the beginning of the array
  i = 0

  # Loop through the array until i is greater than r
  while i <= r:
    # If the current element is 0, swap it with the element at index l
    if nums[i] == 0:
      nums[i], nums[l] = nums[l], nums[i]
      # Increment l since we have swapped a 0 to the left of the array
      l += 1
    # If the current element is 2, swap it with the element at index r
    elif nums[i] == 2:
      nums[i], nums[r] = nums[r], nums[i]
      # Decrement r since we have swapped a 2 to the right of the array
      r -= 1
      # Decrement i since we need to check the element at the new index i again
      i -= 1
    # If the current element is 1, move on to the next element by incrementing i
    i += 1

  # Return the sorted array
  return nums
