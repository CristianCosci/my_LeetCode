class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = -1e4 - 1
        max_ending_here = 0
        for i in range(len(nums)):
            max_ending_here += nums[i]
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
            if max_ending_here < 0:
                max_ending_here = 0
        
        return max_so_far