class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # while len(stones)>1:
        #     stones.sort()
        #     res = stones.pop()-stones.pop()
        #     if res:
        #         stones.append(res)
        # return stones[0] if stones else 0
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) >1:
            first = heapq.heappop(stones)
            sec = heapq.heappop(stones)
            if sec>first:
                heapq.heappush (stones, first-sec)
        
        stones.append(0)
        return abs(stones[0])