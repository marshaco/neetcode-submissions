class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Search the first indexes
        # Then search each array

        lo = 0
        hi = len(matrix) - 1

        while lo <= hi:
            index = (lo + hi) // 2
            print(matrix[index])
            if target == matrix[index][0]:
                return True
            #elif target > matrix[index][0] and target < matrix[index+1][0]:
                #break
            elif target > matrix[index][0]:
                lo = index + 1
            elif target < matrix[index][0]:
                hi = index - 1
                index = hi

        foundList = matrix[index]
        lo = 0
        hi = len(foundList) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if target > foundList[mid]:
                lo = mid + 1
            elif target < foundList[mid]:
                hi = mid - 1
            else:
                return True
        return False

