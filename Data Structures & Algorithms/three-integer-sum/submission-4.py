class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        count = Counter(nums)
        usedNums = set()

        triplets = []

        for i in range(len(nums)):
            j = i+1
            while j < len(nums):
                k=0
                target = -(nums[i] + nums[j])
                if nums[i] == target:
                    k+=1
                if nums[j] == target:
                    k+=1

                triplet = tuple(sorted([nums[i],nums[j],target]))

                if count[target] >= 1 + k and triplet not in usedNums:
                    usedNums.add(triplet)
                    triplets.append([nums[i],nums[j],target]) 
                j+=1

        return triplets