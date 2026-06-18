class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        srtdList = sorted(nums)

        for i in range(len(srtdList)-1):
            if srtdList[i] == srtdList[i+1]:
                return True
        return False
        