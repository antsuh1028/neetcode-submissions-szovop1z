class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        COLS,ROWS = len(matrix[0]), len(matrix)
        l, r = 0, (COLS * ROWS) -1

        while l <= r:
            mid = (l + r) // 2
            num = matrix[mid // COLS][mid % COLS]
            if num == target:
                return True
            elif num > target:
                r = mid - 1
            else:
                l = mid + 1
        return False