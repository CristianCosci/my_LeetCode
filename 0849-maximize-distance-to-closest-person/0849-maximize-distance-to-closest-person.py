class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        before, max_ending_here, max_so_far = 0, 0, 0
        for i in range(len(seats)):
            if seats[i]:
                if before:
                    max_ending_here = (max_ending_here+1) // 2
                    
                before = 1
                if max_ending_here > max_so_far:
                    max_so_far = max_ending_here
                max_ending_here = 0
            
            else:
                max_ending_here += 1
        
        
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
        
        return max_so_far
            