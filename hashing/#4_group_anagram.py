'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''

import collections


def groupAnagram_sorted(strs):
  sorted_words_dict = collections.defaultdict(list)

  for s in strs:
    sorted_word = ''.join(sorted(s))
    if sorted_word in sorted_words_dict:
      sorted_words_dict[sorted_word] += [s]
    else:
      sorted_words_dict[sorted_word] = [s]
  return [l for l in sorted_words_dict.values()]


def groupAnagram(strs):
  ans = collections.defaultdict(list)  #so if nothing return empty list

  for s in strs:
    count = [0] * 26  #counting each letter in alphabet
    for c in s:
      count[ord(c) - ord("a")] += 1
    ans[tuple(count)].append(s)
    print(tuple(count))
  return list(ans.values())


print(groupAnagram_sorted(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(groupAnagram(["eat", "tea", "tan", "ate", "nat", "bat"]))
