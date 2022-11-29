class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_list = [None]*len(nums)
        sum_list[0] = nums[0]
        for i in range(1, len(nums)):
            sum_list[i] = nums[i] + sum_list[i-1]
            
        return sum_list