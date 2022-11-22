import math
class Solution:
    def trailingZeroes(self, n: int) -> int:
        num = str(math.factorial(n))[::-1]
        count = 0
        for i in range(len(num)):
            if num[i] == '0':
                count += 1
            else:
                break
        return count