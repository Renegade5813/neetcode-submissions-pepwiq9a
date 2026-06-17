class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist=[]
        for i,p in enumerate(points):
            distance_origin = (p[0]**2+p[1]**2)**0.5
            dist.append([distance_origin,p])
        sorted_dist = self.mergeSort(dist)
        res = [item[1] for item in sorted_dist[:k]]
        return res
        
    def mergeSort(self, arr):
        if len(arr)<=1:
            return arr
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]
        left_sorted = self.mergeSort(left_arr)
        right_sorted = self.mergeSort(right_arr)
        return self.merge(left_sorted, right_sorted)
    
    def merge(self, a,b):
        res=[]
        i,j=0,0
        while i < len(a) and j < len(b):
            if a[i][0]<b[j][0]:
                res.append(a[i])
                i+=1
            else:
                res.append(b[j])
                j+=1
        
        if i< len(a):
            res.extend(a[i:])
        if j<len(b):
            res.extend(b[j:])
        return res