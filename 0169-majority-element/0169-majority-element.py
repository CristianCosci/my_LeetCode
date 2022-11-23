class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        floor_size = len(nums) // 2
        
        for i in set(nums):
            if nums.count(i) > floor_size:
                return i