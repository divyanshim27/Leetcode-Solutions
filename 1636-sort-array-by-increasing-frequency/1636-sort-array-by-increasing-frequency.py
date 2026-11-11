class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        count = {}
        for x in nums:
            count[x] = count.get(x, 0) + 1
        nums.sort(key=lambda x: (count[x], -x))
        return nums