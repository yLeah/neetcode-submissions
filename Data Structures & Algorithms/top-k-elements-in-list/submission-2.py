class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # make dictionary of numbers -> freq 
        # bucket those then by frequency 
        if len(nums) ==1:
            return [nums[0]]
        if k == len(nums):
            return nums
        
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        
        buckets = {}
        for i in range(len(nums)+1):
            buckets[i+1] = []
        
        for key, value in count.items():
            if value in buckets:
                buckets[value].append(key)
        
        freq = []
        i = len(nums)
        while len(freq) < k:
            for num in buckets[i]:
                freq.append(num)
            i-=1

        return freq
