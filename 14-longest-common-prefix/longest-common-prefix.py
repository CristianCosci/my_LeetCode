class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) > 1:
            q = sorted(strs)
            s1 = q[0]
            s2 = q[-1]
            ans = ""
            for i in range(min(len(s1), len(s2))):
                if s1[i] != s2[i]:
                    return ans
                ans += s1[i]
            
            return ans

        return strs[0]