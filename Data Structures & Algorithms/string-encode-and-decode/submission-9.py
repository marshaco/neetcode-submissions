class Solution:

    def encode(self, strs: List[str]) -> str:
        plain_string = ""

        for i in strs:
            plain_string += str(len(i)) + "/" + i
        
        encoded_string = ""
        for i in range(len(plain_string)):
            encoded_string += chr(ord(plain_string[i]) + 10)

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []

        decoded_str = ""
        for i in range(len(s)):
            decoded_str += chr(ord(s[i]) - 10)
        i=0
        n = ""
        while i < len(decoded_str):
            if decoded_str[i] != "/":
                n += decoded_str[i]
                i += 1
            else:
                decoded_strs.append(decoded_str[i+1:i+1+int(n)])
                i += int(n) + 1
                n=""
        return decoded_strs
