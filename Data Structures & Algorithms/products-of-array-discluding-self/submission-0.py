import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prods = []
        for i in range(len(nums)):
            prods.append(math.prod(nums[0:i])*math.prod(nums[i+1:]))
        return prods