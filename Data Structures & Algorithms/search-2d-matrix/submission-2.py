class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # search row first

        index = self.binarySearchR(matrix, target)
        if matrix[index][0]==target:
            return True
        elif self.binarySearchC(matrix[index], target):
            return True
        else:
            return False

    def binarySearchR(self, arr, target):
        if len(arr)==0:
            return -1
        left,right =0,len(arr)-1
        while left<=right:
            mid = (left+right)//2
            if arr[mid][0]==target:
                return mid
            elif arr[mid][0]>target:
                right =mid-1
            else:
                left =mid+1
        
        if target>arr[mid][0]:
            return  mid
        elif target<arr[mid][0]:
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
                   