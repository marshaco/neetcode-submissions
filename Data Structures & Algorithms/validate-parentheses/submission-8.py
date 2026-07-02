class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        validOpen = {"(", "{", "["}

        matches = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        chars = []

        for i in s:
            if i in validOpen:
                chars.append(i)
            else:
                if len(chars) == 0:
                    return False
                lastOpen = chars.pop()
                if matches[i] != lastOpen:
                    return False

        if len(chars) != 0:
            return False

        return True