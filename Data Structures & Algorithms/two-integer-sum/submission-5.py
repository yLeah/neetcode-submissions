class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for i in range(len(nums)):
            look = target - nums[i]
            if look in dct:
                return [dct[look], i]
            dct[nums[i]] = i
        
      