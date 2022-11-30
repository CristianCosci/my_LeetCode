class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s = len(s)
        if len_s == 0:
            return True
        
        if len_s > len(t):
            return False
        
        count_subsequence=0
        
        for i in range(len(t)):
            if count_subsequence <= len_s -1:
                if s[count_subsequence]==t[i]:
                    count_subsequence+=1
        
        return  count_subsequence == len_s