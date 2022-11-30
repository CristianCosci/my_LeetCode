class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mappatura = {}
        for i in range(len(s)):
            if s[i] not in mappatura and t[i] not in mappatura.values():
                mappatura[s[i]] = t[i]
            elif s[i] not in mappatura or mappatura[s[i]] != t[i]:  
                return False
            
        return True