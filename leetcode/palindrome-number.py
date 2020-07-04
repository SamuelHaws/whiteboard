# Runtime: 52 ms, faster than 91.04% of Python3 online submissions for Palindrome Number.
# Memory Usage: 13.6 MB, less than 96.72% of Python3 online submissions for Palindrome Number.

def isPalindrome(x: int) -> bool:
  x = str(x)
  return x == x[::-1]

print(isPalindrome(121))
print(isPalindrome(-121))