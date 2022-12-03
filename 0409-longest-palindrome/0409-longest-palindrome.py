class Solution:
    def longestPalindrome(self, s: str) -> int:
        a = defaultdict(int)
        for i in s:
            a[i] += 1
        
        count = 0
        for i in a.values():
            count += i // 2 * 2
        
        if count < len(s):
            count += 1
            
        return count