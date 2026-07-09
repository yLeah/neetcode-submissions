class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        dct = {}
        for word in strs:
            if "".join(sorted(word)) in dct:
                dct["".join(sorted(word))].append(word)
            else:
                dct["".join(sorted(word))] = [word]
        ls = []
        for item in dct: 
            ls.append(dct[item])
        return ls
# remember sorted() returns each character as a list if done to a string