import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = defaultdict(int)
        for i in nums:
            freq[i] += 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for n, v in freq.items():
            buckets[v].append(n)

        ans = []    
        
        for i in range(len(buckets) - 1, -1, -1):
            for j in range(len(buckets[i]) - 1, -1, -1):
                ans.append(buckets[i][j])
                if len(ans) == k:
                    return ans
        return []