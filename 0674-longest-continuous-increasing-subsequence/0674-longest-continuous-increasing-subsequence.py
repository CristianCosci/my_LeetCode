class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_ending_here, max_so_far = 1, 1
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                max_ending_here += 1
                if max_so_far < max_ending_here:
                    max_so_far = max_ending_here
            else:
                max_ending_here = 1
            
        return max_so_far