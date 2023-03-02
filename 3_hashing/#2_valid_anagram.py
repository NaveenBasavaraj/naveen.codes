'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: s = "anagram", t = "nagaram"
Output: true

'''


def valid_anagram(s, t):
  if len(s) != len(t):
    return False
  sd, td = {}, {}
  # for char in s:
  #   sd[char] = 1 + sd.get(char, 0)
  # for char in t:
  #   td[char] = 1 + td.get(char, 0)
  # since now we know length is same, we can do the below
  for i in range(len(s)):
    sd[s[i]] = 1 + sd.get(s[i], 0)
    td[t[i]] = 1 + td.get(t[i], 0)
  # return sd == td
  for char in sd:
    if not sd[char] == td.get(char, 0):
      return False
  return True


print(valid_anagram(s="anagram", t="nagaram"))
print(valid_anagram(s="rat", t="car"))
