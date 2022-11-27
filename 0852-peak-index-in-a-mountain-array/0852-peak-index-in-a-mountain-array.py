class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        lo, hi = 0, len(arr)-1
        
        while lo < hi:
            m = (lo + hi) // 2
            if arr[m] < arr[m + 1]:
                lo = m + 1
            else:
                hi = m
        
        return lo
        
            