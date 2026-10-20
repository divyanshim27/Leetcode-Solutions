class Solution:
    def sortArray(self, nums):
        lo = min(nums)
        hi = max(nums)

        count = [0] * (hi - lo + 1)

        for n in nums:
            count[n - lo] += 1

        i = 0
        for spot in range(len(count)):
            while count[spot] > 0:
                nums[i] = spot + lo
                i += 1
                count[spot] -= 1

        return nums