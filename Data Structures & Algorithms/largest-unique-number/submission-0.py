class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for i in nums:
            freq[i] += 1
        maxx = -1
        for i in nums:
            if freq[i] > 1:
                continue
            maxx = max(i, maxx)
        return maxx