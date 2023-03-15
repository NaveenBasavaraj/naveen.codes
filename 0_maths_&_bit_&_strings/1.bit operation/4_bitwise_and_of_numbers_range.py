'''
Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: left = 5, right = 7
Output: 4
Example 2:

Input: left = 0, right = 0
Output: 0
Example 3:

Input: left = 1, right = 2147483647
Output: 0
'''


class bitWiseRangeAnd:

  def bitWiseRange(self, m, n):
    """
    Computes the bitwise AND of all integers in the range [m, n].
    
    Args:
        m (int): The lower bound of the range (inclusive).
        n (int): The upper bound of the range (inclusive).
        
    Returns:
        int: The bitwise AND of all integers in the range [m, n].
    """
    count = 0  # Initialize the counter variable to 0.

    # Right-shift m and n until they have the same value in their binary representation.
    while m < n:
      m = m >> 1
      n = n >> 1
      count += 1  # Increment the counter variable for each right-shift.

    # Left-shift m by the number of times it was right-shifted.
    return m << count


# Example input code
bw = bitWiseRangeAnd()
m = 5
n = 7
result = bw.bitWiseRange(m, n)
print(f"The bitwise AND of all integers in the range [{m}, {n}] is: {result}")
