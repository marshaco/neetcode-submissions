class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashNumbers = set(numbers)
        print(hashNumbers)

        for i in range(len(numbers)):
            if (target - (numbers[i])) in hashNumbers:
                j=i+1
                for k in numbers[j:]:
                    if k == target-(numbers[i]):
                        print(k)
                        break
                    else:
                        j+=1
                return[i+1,j+1]
        return [0,1]
                
