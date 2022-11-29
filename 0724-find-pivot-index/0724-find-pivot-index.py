class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if sum(nums[1:]) == 0:
            return 0
        
        sum_left = 0
        sum_right = sum(nums) - nums[0]
        for i in range(1, len(nums)-1):
            sum_left += nums[i-1]
            sum_right -= nums[i]
            
            if sum_left == sum_right:
                return i
            

        if sum(nums[:-1]) == 0:
            return len(nums)-1
        
        return -1