class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numbers = set()

        for n in nums:
            numbers.add(n)
        print(numbers)
        longestSequence = 0

        for i in numbers:
            if i-1 not in numbers:
                currentSequence = 0
                while i in numbers:
                    currentSequence += 1
                    i += 1
                if currentSequence > longestSequence:
                    longestSequence = currentSequence            

        return longestSequence