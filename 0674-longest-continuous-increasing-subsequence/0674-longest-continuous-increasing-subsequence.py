class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        count = 1
        max = 1
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                count += 1
                if max < count:
                    max = count
            else:
                count = 1
            
        return max