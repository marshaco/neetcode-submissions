class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}
        
        for i,val in enumerate(nums):
            print(i, val)
            diff = target - val
            if diff in numsMap:
                return [numsMap[diff], i]
            numsMap[val] = i
        return [0,1]