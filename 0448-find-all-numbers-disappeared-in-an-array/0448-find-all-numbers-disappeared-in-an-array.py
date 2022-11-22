class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        to_return = []
        arr = set(nums)
        for i in range(1, len(nums)+1):
            if i not in arr:
                to_return.append(i)
                
        return to_return