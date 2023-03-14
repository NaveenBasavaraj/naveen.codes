'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
'''


class SingleNumber:

  def bitWiseOperation(self, nums):
    '''
      This approach uses the XOR (^) operator to find the single number. The idea is that the XOR operation of any number with itself results in 0. Therefore, if we XOR all the numbers in the list, then the result will be the single number that is not repeated in the list.
  
  For example, if we have a list [2, 3, 4, 3, 2], then the bitwise operation approach will work as follows:
  
  2 ^ 3 = 1
  1 ^ 4 = 5
  5 ^ 3 = 6
  6 ^ 2 = 4
  So, the single number is 4.
    '''
    res = 0
    for num in nums:
      res = num ^ res
    return res

  def sumApproach(self, nums):
    '''
    This approach uses the formula 2*(sum of unique numbers) - (sum of all numbers) to find the single number. This formula works on the concept of arithmetic progression. By finding the sum of unique numbers in the list and multiplying it by 2, we get the sum of all numbers in the list without the repeated number. Finally, we subtract the sum of all numbers in the list from the sum of all unique numbers to get the single number.

For example, if we have a list [2, 3, 4, 3, 2], then the sum approach will work as follows:

Sum of unique numbers: 2 + 3 + 4 = 9
2 * 9 = 18
Sum of all numbers: 2 + 3 + 4 + 3 + 2 = 14
Single number: 18 - 14 = 4
    '''
    return 2 * sum(set(nums)) - sum(nums)

  def countingApproach(Self, nums):
    '''
    This approach uses a dictionary to count the occurrence of each number in the list. We then iterate over the list again and return the number that has a count of 1.

For example, if we have a list [2, 3, 4, 3, 2], then the counting approach will work as follows:

Count dictionary: {2: 2, 3: 2, 4: 1}
Return 4 as it has a count of 1.
Bitwise operations are preferred for this problem because they have a time complexity of O(n) and do not require any extra space, whereas the other two approaches require additional space or have a higher time complexity.
    '''
    count = {}
    for num in nums:
      count[num] = 1 + count.get(num, 0)
    for num in nums:
      if count[num] == 1:
        return num


sn = SingleNumber()

input_list = [2, 3, 4, 3, 2]


result = sn.bitWiseOperation(input_list)
print(result)
result = sn.sumApproach(input_list)
print(result)
result = sn.countingApproach(input_list)
print(result)
