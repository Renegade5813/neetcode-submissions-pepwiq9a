class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums)
        longest = 0
        for num in lookup:
            if num - 1 not in lookup:
                curr = num
                curr_streak = 1
                while curr + 1 in lookup:
                    curr +=1
                    curr_streak += 1
                longest = max(curr_streak, longest)

            
        return longest
        