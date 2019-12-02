class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = int(''.join(reversed(str(-x))))
            x = -x
        else:
            x = int(''.join(reversed(str(x))))
            
        if x > 2**31 - 1 or x < -(2**31):
            x = 0
            
        return x