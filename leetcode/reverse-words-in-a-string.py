# Runtime: 24 ms, faster than 97.01% of Python3 online submissions for Reverse Words in a String.
# Memory Usage: 14.2 MB, less than 97.34% of Python3 online submissions for Reverse Words in a String.

def reverseWords(s):
  return ' '.join(s.split()[::-1])

print(reverseWords("the sky is blue"))