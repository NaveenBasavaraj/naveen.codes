'''
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
'''


class CoutingBits:

  def countBits(self, n):
    """
    A function that counts the number of set bits in binary representation of all
    numbers from 0 to n (inclusive) and returns a list of counts.

    Args:
      n (int): An integer value.

    Returns:
      list: A list containing the number of set bits in binary representation
      of all numbers from 0 to n.

    Example:
      >>> obj = CoutingBits()
      >>> obj.countBits(5)
      [0, 1, 1, 2, 1, 2]
    """
    bits = [0] * (n + 1)  # initialize an array of size n+1 with all zeros
    offset = 1  # initialize the offset value to 1
    for i in range(1, n + 1):
      if offset * 2 == i:  # if the current index is twice the offset
        offset = i  # update the offset value to current index
      bits[i] = 1 + bits[i - offset]  # calculate the count of set bits using
      # previously calculated value and update
      # the bits array
    return bits


obj = CoutingBits()
n = 7
print(obj.countBits(n))
