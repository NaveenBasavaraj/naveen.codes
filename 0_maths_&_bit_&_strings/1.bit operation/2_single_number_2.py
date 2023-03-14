'''
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,3,2]
Output: 3

Example 2:
Input: nums = [0,1,0,1,0,1,99]
Output: 99
'''


class SingleNumber2:

  def bitManipulation(self, nums):
    # Initialize two variables to keep track of the count of 1's in each bit position
    ones, twos = 0, 0
    # Iterate through the numbers in the array
    for num in nums:
      # Update the count of 1's in each bit position that have appeared once
      ones = (ones ^ num) & ~twos
      # Update the count of 1's in each bit position that have appeared twice
      twos = (twos ^ num) & ~ones
    # Return the count of 1's in each bit position that have appeared only once,
    # which corresponds to the single element in the array
    return ones


sn = SingleNumber2()
result = sn.bitWiseApproach([2, 2, 3, 2])
print(result)
result = sn.bitWiseApproach([0, 1, 0, 1, 0, 1, 99])
print(result)
'''
Explanation for Example 1:

Input: nums = [2,2,3,2]
Output: 3

Initially, ones and twos are set to 0. We iterate through the numbers in the array as follows:

num = 2:
ones = (0 ^ 2) & ~0 = 2 & ~0 = 2
twos = (0 ^ 2) & ~2 = 2 & ~2 = 0

num = 2:
ones = (2 ^ 2) & ~0 = 0 & ~0 = 0
twos = (0 ^ 2) & ~0 = 2 & ~0 = 2

num = 3:
ones = (0 ^ 3) & ~2 = 3 & ~2 = 1
twos = (2 ^ 3) & ~1 = 1 & ~1 = 0

num = 2:
ones = (1 ^ 2) & ~0 = 3 & ~0 = 3
twos = (0 ^ 2) & ~3 = 2 & ~3 = 2
'''
