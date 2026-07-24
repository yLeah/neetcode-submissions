class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        if len(st) == 0:
            return 0
        top = 0
        streak = 1
        for num in st:
            streak = 1 
            nxt = num + 1 
            if num - 1 not in st:
                while nxt in st:
                    streak += 1
                    nxt += 1
            if top < streak:
                top = streak
        return top 
