class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # search row first
        rows= [i[0] for i in matrix]

        index = self.binarySearchR(rows, target)
        if matrix[index][0]==target:
            return True
        if self.binarySearchC(matrix[index], target):
            return True
        else:
            return False

    def binarySearchR(self, arr, target):
        if len(arr)==0:
            return -1
        left,right =0,len(arr)-1
        while left<=right:
            mid = (left+right)//2
            if arr[mid]==target:
                return mid
            elif arr[mid]>target:
                right =mid-1
            else:
                left =mid+1
        
        if target>arr[mid]:
            return  mid
        elif target<arr[mid]:
            return mid-1

    def binarySearchC(self, arr, target):
        left,right =0,len(arr)-1
        while left<=right:
            mid = (left+right)//2
            if arr[mid]==target:
                return mid
            elif arr[mid]>target:
                right =mid-1
            else:
                left =mid+1
        return False
                   