class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        bank = {}
        if len(s) != len(t):
            return False
        
        for char in s:
            if char in bank:
                bank[char] += 1
            else:
                bank[char] = 1
        
        for ch in t:
            if ch not in bank:
                return False
            else:
                bank[ch] -= 1
                if bank[ch] < 0:
                    return False
        return True
# algorithmically optimized 
# arrays > sorting 