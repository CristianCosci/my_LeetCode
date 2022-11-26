class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums, reverse=True)
        self.nums.append(-inf)
        while len(self.nums) > self.k:
            self.nums.pop()

    def add(self, val: int) -> int:
        i = 0
        while i < self.k:
            if val >= self.nums[i]:
                self.nums.insert(i, val)
                
                if len(self.nums) > self.k:
                    self.nums.pop()
                
                break
                
            i += 1
            
        return self.nums[-1] #if len(self.nums)>0 else None

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)