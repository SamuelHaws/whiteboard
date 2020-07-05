# Runtime: 32 ms, faster than 78.28% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 13.7 MB, less than 97.48% of Python3 online submissions for Longest Common Prefix.

def longestCommonPrefix(strs):
  if len(strs) == 0:
    return ''
  i = 0
  ans = ''
  shortestLen = min([len(s) for s in strs])
  while i < shortestLen:
    chars = [s[i] for s in strs]
    if chars.count(chars[0]) != len(chars):
      break
    i += 1
    ans += chars[0]
  return ans



print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))