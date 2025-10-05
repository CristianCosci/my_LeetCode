class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        count = 0

        for i in range(len(nums)):
            if count == 0:
                candidate = nums[i]
            
            if candidate == nums[i]:
                count+= 1
            else:
                count -=1
            
            
        return candidate