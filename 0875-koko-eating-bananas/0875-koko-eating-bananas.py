class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        lo = 1
        hi = max(piles)
        ans = hi
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            total_hours = 0
            for p in piles:
                total_hours += (p + mid - 1) // mid
            if total_hours <= h:
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans