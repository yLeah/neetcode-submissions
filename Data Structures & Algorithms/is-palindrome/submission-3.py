class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(s.lower().strip())
        left = 0
        right = len(s)-1
        while left < right:
            if not s[left].isalnum():
                while s[left].isalnum() == False:
                    if left == len(s) -1:
                        return True
                    left+=1
            if not s[right].isalnum():
                while s[right].isalnum() == False:
                    right-=1
            if s[left].isalnum() and s[right].isalnum():
                if s[left] != s[right]:
                    return False
            left+=1
            right-=1
        return True
            



