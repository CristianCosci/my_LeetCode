class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums, reverse=True)
        self.nums.append(-inf)

    def add(self, val: int) -> int:
        i = 0
        while True:
            if val >= self.nums[i]:
                self.nums.insert(i, val)
                break
            i += 1
            
        return self.nums[self.k-1]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)