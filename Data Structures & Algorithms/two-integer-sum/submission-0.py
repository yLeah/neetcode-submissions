class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # two pointer 
        # take the first one and check all the ones past it 
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
