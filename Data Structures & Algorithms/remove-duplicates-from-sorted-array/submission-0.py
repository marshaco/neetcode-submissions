class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l,r = 0,1
        length = len(nums)
        
        while l + 1 < len(nums):
            lIndex = nums[l]
            
            while l + 1 < len(nums) and nums[l] == nums[l+1]:
                nums.pop(l+1)
            l += 1
        return len(nums)