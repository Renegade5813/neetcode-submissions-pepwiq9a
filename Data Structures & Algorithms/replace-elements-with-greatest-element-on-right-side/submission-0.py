class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]
        maxx = -1

        for i in range(len(arr) - 1, -1, -1):
            temp = maxx
            maxx = max(arr[i] , maxx)
            arr[i] = temp
            
        return arr

            