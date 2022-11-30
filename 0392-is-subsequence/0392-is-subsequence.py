class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        
        count_subsequence=0
        for i in range(0,len(t)):
            if count_subsequence <= len(s) -1:
                if s[count_subsequence]==t[i]:
                    count_subsequence+=1
        
        return  count_subsequence == len(s) 