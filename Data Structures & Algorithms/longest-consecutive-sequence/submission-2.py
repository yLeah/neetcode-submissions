class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(set(nums)) == 1 or len(set(nums)) == 0:
            return len(set(nums))
        st = set(nums)
        top = 1
        streak = 1
        for num in st:
            streak = 1
            nxt = num + 1
            if nxt in st and (num - 1) not in st:
                while nxt in st:
                    streak += 1
                    nxt += 1
                    if top < streak:
                        top = streak 
        return top 

