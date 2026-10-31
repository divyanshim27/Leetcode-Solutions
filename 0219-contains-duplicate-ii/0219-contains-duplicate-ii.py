class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        seen = {}
        
        for i,j in enumerate(nums):
            if j in seen and i - seen[j]<=k:
                return True
            seen[j]=i
        return False