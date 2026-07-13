class Solution:
    def isPalindrome(self, s: str) -> bool:
        strip = ""

        for i in s:
            if i.isalnum():
                strip += i

        r = len(strip) - 1
        l = 0

        while l <= r:

            while not strip[l].isalnum():
                l +=1

            while not strip[r].isalnum():
                r -= 1

            print("s[l]", strip[l])
            print("s[r]", strip[r])

            if strip[l].lower() != strip[r].lower():
                return False
            l += 1
            r -= 1
        return True