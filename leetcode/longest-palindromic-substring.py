# Note: The below solution is inefficient and will be optimized at a later date.

# Runtime: 3788 ms, faster than 35.37% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 20.6 MB, less than 22.14% of Python3 online submissions for Longest Palindromic Substring.

class Solution: 
  # Ex: {"aba": 3}
  palindromes = {}

  def isPalindrome(self, s):
    if s in self.palindromes:
      return True
    if s == s[::-1]:
      self.palindromes[s] = len(s)
      return True
    return False

  def longestPalindrome(self, s: str) -> str:
    if len(s) <= 1:
      return s
    longest = ''
    for i, v in enumerate(s):
      substr = v
      l = i - 1
      r = i + 1
      while True:
        # If valid, expand left and right from center
        if l >= 0 and r < len(s) and (self.isPalindrome(substr) and s[l] == s[r]):
          substr = s[l] + substr + s[r]
          l -= 1
          r += 1
        # Else if valid, expand to the left (example case: "bb")
        elif l >= 0 and self.isPalindrome(s[l] + substr):
          substr = s[l] + substr
          l -= 1
        else:
          break
      
      if len(substr) > len(longest):
        longest = substr
    return longest

  def test(self):
    print(self.longestPalindrome("ba"))
    print(self.longestPalindrome("babad"))
    print(self.longestPalindrome("babab"))
    print(self.longestPalindrome("cbbd"))
    print(self.longestPalindrome("bbbd"))
    print(self.longestPalindrome("dbbb"))
    print(self.longestPalindrome("cbbd"))
    print(self.longestPalindrome("aaabaaaa"))
    print(self.longestPalindrome("aaabaaaaaaaaaaaa"))
    print(self.longestPalindrome("aaaabaaa"))
    print(self.longestPalindrome("bb"))

Solution().test()
