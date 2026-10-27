class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = {}
        
        for num in nums:
            if num in seen:
                return True
            seen[num] = 1
            
        return False