class Solution:
    def check(self,flowerbed, i, n):
        flowerbed[i] = 1
        n -= 1
        return flowerbed, n
    
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) > 1:
            for i in range(len(flowerbed)):
                if n == 0:
                    return True
                if i == 0:
                     if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                        flowerbed, n = self.check(flowerbed, i, n)
                elif i == len(flowerbed)-1:
                     if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                        flowerbed, n = self.check(flowerbed, i, n)
                else:
                    if flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i-1] == 0:
                        flowerbed, n = self.check(flowerbed, i, n)    
        
        elif len(flowerbed) == 1:
            if n == 0:
                    return True
                
            if flowerbed[0] == 0:
                flowerbed[0] = 1
                n -= 1
        
        return n == 0