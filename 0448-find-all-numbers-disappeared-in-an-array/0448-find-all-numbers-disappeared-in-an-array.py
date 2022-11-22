class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        to_return = []
        arr = set(nums) #convert into set beacuse 'in' operations take so much time
        for i in range(1, len(nums)+1):
            if i not in arr:
                to_return.append(i)
                
        return to_return