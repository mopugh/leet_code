class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = ''.join(reversed(str(x)))
        return str(x) == y