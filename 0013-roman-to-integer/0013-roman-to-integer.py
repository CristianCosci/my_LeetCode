class Solution:
    def romanToInt(self, s: str) -> int:
        value_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        sum = 0
        i = 0
        while i < len(s):
            to_add = 0
            if i+1 < len(s):
                if value_dict[s[i]] < value_dict[s[i+1]]:
                    to_add = value_dict[s[i+1]] - value_dict[s[i]]
                    i += 1
                else:
                    to_add = value_dict[s[i]]
            else:
                to_add = value_dict[s[i]]
            
            sum += to_add
            i += 1 
        return sum