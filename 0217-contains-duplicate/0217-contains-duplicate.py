class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = {}
        for i in nums:
            if i in seen:
                 return True

            seen[i]=True
        return False