class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        counts = {}
        
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            
        for num in nums:
            if counts[num] == 1:
                return num
                
        return 0