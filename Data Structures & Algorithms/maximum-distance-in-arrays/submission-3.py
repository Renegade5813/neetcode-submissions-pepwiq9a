class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_val = float('inf')
        min_idx = -1
        
        for i, arr in enumerate(arrays):
            if arr[0] < min_val:
                min_val = arr[0]
                min_idx = i
        
        max_val1 = float('-inf')
        for i, arr in enumerate(arrays):
            if i != min_idx:
                max_val1 = max(max_val1, arr[-1])
        
        dist1 = abs(max_val1 - min_val)
        
        # Second pass: find global max, exclude its array, find min from others
        max_val = float('-inf')
        max_idx = -1
        
        for i, arr in enumerate(arrays):
            if arr[-1] > max_val:
                max_val = arr[-1]
                max_idx = i
        
        min_val2 = float('inf')
        for i, arr in enumerate(arrays):
            if i != max_idx:
                min_val2 = min(min_val2, arr[0])
        
        dist2 = abs(max_val - min_val2)
        
        return max(dist1, dist2)