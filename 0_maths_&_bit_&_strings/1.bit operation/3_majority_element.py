'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''


class MajorityElement:

  # countApproach method implementation
  def countApproach(self, nums):
    #  Boyer-Moore Majority Vote Algorithm
    # Initialize the result and count variables
    res, count = 0, 0
    # Iterate through the input array
    for n in nums:
      # If the count is 0, set the current element as the majority element
      if count == 0:
        res = n
      # Increment the count if the current element is the majority element, else decrement it
      count += (1 if n == res else -1)
    # Return the majority element
    return res

  # bitApproach method implementation
  def countingBits(self, nums):
    # Initialize an array of 32 bits with 0's
    bits = [0] * 32
    # Iterate through the input array
    for n in nums:
      # For each element, update the count of 1's for each bit
      for i in range(32):
        bits[i] += (n >> i) & 1
    # Initialize the result variable
    res = 0
    # For each bit, set the i-th bit of the result to 1 if the count of 1's for that bit is odd
    for i in range(32):
      res |= (bits[i] % 2) << i
    # Return the result, which is the majority element
    return res
