class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            number = str(x)
            for i in range(len(number)):
                if not number[i] == number[-i-1]:
                    return False

            return True
        return False