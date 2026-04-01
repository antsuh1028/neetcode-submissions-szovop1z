class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix[0]), len(matrix)
        l, r = 0, (m * n) -1

        while l <= r:
            if l == r:
                mid = (l + r) // 2
                num = matrix[mid // m][mid % m]
                return num == target

            mid = (l + r) // 2
            print(mid)
            num = matrix[mid // m][mid % m]
            if num == target:
                return True
            elif num > target:
                r = mid
            else:
                l = mid + 1
        return False