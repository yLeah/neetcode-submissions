class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        i = 1
        while i < len(nums):
            left.append(left[i-1]*nums[i-1])
            i+=1
        
        right = [1]
        j = len(nums)-1
        while j > 0:
            right.append(right[-1]*nums[j])
            j-=1
        right = right[::-1]
        tg= [x*y for x,y in zip(right,left)]
        return tg

# product of the left x product of the right