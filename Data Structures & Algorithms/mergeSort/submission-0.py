# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        
        if len(pairs)<=1:
            return pairs
        
        left_arr= pairs[:len(pairs)//2]
        right_arr= pairs[len(pairs)//2:]

        left_sorted = self.mergeSort(left_arr)
        right_sorted = self.mergeSort(right_arr)

        return self.merge(left_sorted,right_sorted)
    
    def merge(self, a,b):
        result =[]
        i,j=0,0
        while i< len(a) and j < len(b):
            if a[i].key > b[j].key:
                result.append(b[j])
                j+=1
            else:
                result.append(a[i])
                i+=1
        
        if i< len(a):
            result.extend(a[i:])
        if j< len(b):
            result.extend(b[j:])
        
        return result


