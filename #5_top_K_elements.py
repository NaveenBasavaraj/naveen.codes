'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
'''


def top_K_elements(nums, k):
  count = {}
  freq = [[] for i in range(len(nums) + 1)]

  for n in nums:
    # count dict has key(number) and value(frequency)
    count[n] = 1 + count.get(n, 0)
  for n, c in count.items():
    # use bucket sort to keep index as frequency and number list as value
    freq[c].append(n)
  result = []
  for i in range(len(freq) - 1, 0, -1):
    for num in freq[i]:
      result.append(num)
      if len(result) == k:
        return result
  return []


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(top_K_elements(nums, k))
