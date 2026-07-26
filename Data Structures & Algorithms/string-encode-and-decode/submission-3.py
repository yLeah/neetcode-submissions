class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for item in strs:
            ln = len(item)
            encoded_string = encoded_string + str(ln) + "]" + item
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while len(s) > i:
            brak = s.index("]", i)
            jump = int(s[i:brak])
            decoded_strs.append(s[brak+1:brak+1+jump])
            i = brak+1+jump
        return decoded_strs

# this time use indices instead of splicing for decode 