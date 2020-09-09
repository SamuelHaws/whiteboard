# Runtime: 32 ms, faster than 84.36% of Python3 online submissions for Reverse Words in a String III.
# Memory Usage: 14.1 MB, less than 84.10% of Python3 online submissions for Reverse Words in a String III.

def reverseWords(s):
  return ' '.join([x[::-1] for x in s.split()])

print(reverseWords("Let's take LeetCode contest"))