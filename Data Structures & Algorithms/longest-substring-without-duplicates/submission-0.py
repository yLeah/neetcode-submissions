class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # make the substring a set, sliding window problem
        substring = set()
        l = 0
        record = 0

        for r in range(len(s)):
            while s[r] in substring:
                substring.remove(s[l])
                l+= 1
            substring.add(s[r])
            record = max(record, r - l + 1)
        return record