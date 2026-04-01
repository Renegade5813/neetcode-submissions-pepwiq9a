class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        close = []
        ceuc = 0

        for i,j in points:
            euc = i*i+ j*j
            close.append([euc, i,j])
        heapq.heapify(close)
        res = []
        while k>0:
            euc, i, j = heapq.heappop(close)
            res.append([i,j])
            k-=1
        return res