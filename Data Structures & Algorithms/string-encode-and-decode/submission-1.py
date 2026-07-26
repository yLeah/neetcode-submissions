class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for item in strs:
            ln = len(item)
            encoded_string = encoded_string + str(ln) + "]" + item
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        while len(s) != 0:
            jump = int(s[0:s.index("]")])
            decoded_strs.append(s[s.index("]")+1:s.index("]")+1 + jump])
            s = s[s.index("]")+1 + jump:]
        return decoded_strs