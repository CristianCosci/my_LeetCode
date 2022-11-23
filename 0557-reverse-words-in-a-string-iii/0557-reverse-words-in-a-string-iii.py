class Solution:
    def reverseWords(self, s: str) -> str:
        new_s = ""
        for i in s.split(" "):
            new_s += i[::-1] + " "
        
        return new_s[:-1]
        