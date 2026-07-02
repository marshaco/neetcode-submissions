class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numbers = set()

        for n in nums:
            numbers.add(n)
        
        longestSequence = 0

        for i in numbers:
            currentSequence = 0
            while i in numbers:
                currentSequence += 1
                i += 1
            if currentSequence > longestSequence:
                longestSequence = currentSequence            

        return longestSequence