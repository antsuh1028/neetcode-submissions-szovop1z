class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for i in range(len(matrix)):
        #     for j in  range(len(matrix[0])):
        #         if matrix[i][j] == target:
        #             return True
        # return False

        for row in matrix:
            if row[-1] == target:
                return True
            if row[-1] < target:
                continue
            else:
                l,r = 0,len(row)-1
                
                while l < r:
                    mid = (r+l)//2
                    if row[mid] > target:
                        r = mid
                    elif row[mid] < target:
                        l=mid+1
                    else:
                        return True
                return False
        return False


