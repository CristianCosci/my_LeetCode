class Solution:
    def getSum(self, a: int, b: int) -> int:
        #convert into binary format to do bitshifting operation
        # https://www.youtube.com/watch?v=qq64FrA2UXQ&t=848s
        mask = 0xffffffff #because in python number has infinite lenght, this is to avoid infinite loop cause by << 1
        a = a & mask
        while b != 0:
            sum = (a ^ b) & mask
            b = ((a & b) << 1) & mask
            a = sum
            
        if (a>>31) & 1: # If a is negative in 32 bits sense
            return ~(a^mask)
        
        return a