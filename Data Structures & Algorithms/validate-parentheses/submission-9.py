class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        validOpen = {"(", "{", "["}
        matches = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        chars = []

        for c in s:
            if c in validOpen:
                chars.append(c)
            else:
                if not chars:
                    return False

                lastOpen = chars.pop()

                if matches[c] != lastOpen:
                    return False

        return len(chars) == 0