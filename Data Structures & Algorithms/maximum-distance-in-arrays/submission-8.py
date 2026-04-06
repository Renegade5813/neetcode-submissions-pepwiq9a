class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minn , maxx = arrays[0][0], arrays[0][-1]
        res = 0

        for i in range(1, len(arrays)):
            arr = arrays[i]
            res = max(res, maxx - arr[0], arr[-1] - minn)
            minn = min(minn, arr[0])
            maxx = max(maxx, arr[-1])
        return res