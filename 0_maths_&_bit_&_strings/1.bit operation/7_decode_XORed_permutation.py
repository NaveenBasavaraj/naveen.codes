'''
There is an integer array perm that is a permutation of the first n positive integers, where n is always odd.

It was encoded into another integer array encoded of length n - 1, such that encoded[i] = perm[i] XOR perm[i + 1]. For example, if perm = [1,3,2], then encoded = [2,1].

Given the encoded array, return the original array perm. It is guaranteed that the answer exists and is unique.

Example 1:

Input: encoded = [3,1]
Output: [1,2,3]
Explanation: If perm = [1,2,3], then encoded = [1 XOR 2,2 XOR 3] = [3,1]
Example 2:

Input: encoded = [6,5,4,6]
Output: [2,4,1,5,3]
'''


class Solution:

  def decode(self, encoded):
    """
    A function that decodes an array encoded of length n - 1 where
    encoded[i] = arr[i] XOR arr[i+1] for all 0 <= i < n - 1, and
    arr is a permutation of the integers from 1 to n.

    Args:
      encoded (List[int]): A list of integers representing the encoded array.

    Returns:
      List[int]: A list of integers representing the original array arr.

    Example:
      >>> obj = Solution()
      >>> encoded = [3, 1]
      >>> obj.decode(encoded)
      [1, 2, 3]
    """
    n = len(encoded) + 1  # calculate the length of original array arr
    xor1 = 0
    for i in range(1, n + 1):
      xor1 ^= i  # calculate the XOR of all integers from 1 to n

    xor2 = 0
    for i in range(1, n - 1, 2):
      xor2 ^= encoded[
        i]  # calculate the XOR of alternate elements in encoded array

    ans = []
    ans.append(
      xor1 ^ xor2)  # calculate the first element of arr using xor1 and xor2

    for i in range(n - 1):
      ans.append(
        encoded[i]
        ^ ans[-1])  # calculate the remaining elements of arr using the formula

    return ans


obj = Solution()
encoded = [6, 5, 4, 6]
print(obj.decode(encoded))
