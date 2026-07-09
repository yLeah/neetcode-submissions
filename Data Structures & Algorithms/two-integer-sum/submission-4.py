class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # my attempt at hashmap solution - add all to a dict 
        # why this question suggests hash: 
        dct = {}
        for i in range(len(nums)):
            look = target - nums[i]
            if look in dct:
                return [min(i, dct[look]), max(i, dct[look])]
            dct[nums[i]] = i
        
      