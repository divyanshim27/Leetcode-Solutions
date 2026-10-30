class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        
        for i, v in enumerate(nums[:-2]):
            if i > 0 and v == nums[i - 1]:
                continue
            
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                s = v + nums[lo] + nums[hi]
                if s < 0:
                    lo += 1
                elif s > 0:
                    hi -= 1
                else:
                    res.append([v, nums[lo], nums[hi]])
                    lo, hi = lo + 1, hi - 1
                    while lo < hi and nums[lo] == nums[lo - 1]: lo += 1
                    while lo < hi and nums[hi] == nums[hi + 1]: hi -= 1
                    
        return res
