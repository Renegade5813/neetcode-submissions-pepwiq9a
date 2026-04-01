class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []

        for x,y in points:
            sq = x*x +y*y
            dist.append([sq, x,y])
        heapq.heapify(dist)
        res =[]
        while k>0:
            sq, x, y = heapq.heappop(dist)
            res.append([x,y])
            k-=1
        return res