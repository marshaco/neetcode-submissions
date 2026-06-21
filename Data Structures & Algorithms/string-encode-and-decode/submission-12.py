class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for i in strs:
            encoded_string += str(len(i)) + "/" + i

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []

        i=0
        n = ""
        while i < len(s):
            if s[i] != "/":
                n += s[i]
                i += 1
            else:
                decoded_strs.append(s[i+1:i+1+int(n)])
                i += int(n) + 1
                n=""
        return decoded_strs
