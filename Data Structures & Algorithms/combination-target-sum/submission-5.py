class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]

        subset=[]
        nums.sort()
        def dfs(i,total):

            if total ==target:
                result.append(subset.copy())
                return
            if total>target or i>=len(nums):
                return 

            total+=nums[i]
            subset.append(nums[i])
            dfs(i,total)

            total-=nums[i]
            subset.pop()
            dfs(i+1,total)

            return
        dfs(0,0)
        return result

        