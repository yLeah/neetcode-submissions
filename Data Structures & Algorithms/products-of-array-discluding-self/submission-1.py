class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right = [1]
        i = 1
        while i < len(nums):
            right.append(right[i-1]*nums[i-1])
            i+=1
        
        left = [1]
        j = len(nums)-1
        while j > 0:
            left.insert(0,left[0]*nums[j])
            j-=1
        tg= [x*y for x,y in zip(right,left)]
        return tg

# product of the left x product of the right