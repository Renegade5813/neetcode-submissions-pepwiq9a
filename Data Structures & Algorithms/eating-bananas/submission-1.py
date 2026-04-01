class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        minn = r

        def numHours(rate, maxHours, arr):
            count = 0
            for i in arr:
                count += (i + rate - 1) // rate
            return count

        while l <= r:
            m = l + (r - l) // 2
            hrs = numHours(m, h, piles)

            if hrs <= h:
                minn = m
                r = m - 1
            else:
                l = m + 1

        return minn