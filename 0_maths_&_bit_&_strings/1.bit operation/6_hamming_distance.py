'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.

Example 1:

Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
Example 2:

Input: x = 3, y = 1
Output: 1
'''


class hammingDistance:

  def bitManipulation(self, x, y):
    """
    A function that calculates the Hamming distance between two integers.
    The Hamming distance is the number of differing bits between two integers
    when they are represented in binary.

    Args:
      x (int): An integer value.
      y (int): An integer value.

    Returns:
      int: The Hamming distance between x and y.

    Example:
      >>> obj = hammingDistance()
      >>> obj.bitManipulation(1, 4)
      2
    """
    result = x ^ y  # calculate the bitwise XOR of x and y
    count = 0
    while result > 0:
      count += result & 1  # check if the rightmost bit is set and increment count
      result >>= 1  # right shift the bits of result by 1 position
    return count


obj = hammingDistance()
x = 1
y = 4
print(obj.bitManipulation(x, y))
