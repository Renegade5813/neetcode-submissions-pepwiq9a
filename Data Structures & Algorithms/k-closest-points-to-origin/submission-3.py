class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance=[]
        for point in points:
            dist = (point[0]**2+point[1]**2)**(1/2)
            distance.append([dist,point])
        heapq.heapify(distance)
        result=[]
        for i in range(k):
            result.append(heapq.heappop(distance)[1])
        return result