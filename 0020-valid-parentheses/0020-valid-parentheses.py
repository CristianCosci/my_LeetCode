class Solution:
    def isValid(self, s: str) -> bool:
        value_dict = {'(': ')', '[':']', '{':'}'}
        if len(s) < 2 or s[0] in value_dict.values():
            return False
        else:
            result =  True
            to_close = []
            for i in s:
                if i in value_dict.keys():
                    to_close.insert(0, value_dict[i])
                else:
                    if len(to_close) > 0 and to_close[0] == i:
                        to_close.pop(0)
                    else:
                        result = False
            
            if len(to_close) !=0:
                result = False 
            return result