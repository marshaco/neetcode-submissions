class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenVals = set()

        for i in nums:
            if i in seenVals:
                return True
            seenVals.add(i)
        return False