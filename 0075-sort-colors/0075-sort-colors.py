class Solution:
    def sortColors(self, nums):
        count = [0, 0, 0]

        for n in nums:
            count[n] += 1

        i = 0
        for color in range(3):
            for _ in range(count[color]):
                nums[i] = color
                i += 1