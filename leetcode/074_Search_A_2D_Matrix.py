# Source: https://leetcode.com/problems/search-a-2d-matrix/
# Author: Owen Cooke


class Solution:
    def searchMatrix(self, matrix, target):
        n = len(matrix[0])
        l = 0
        r = len(matrix) * n - 1
        while l <= r:
            mid = (l + r) // 2
            val = matrix[mid // n][mid % n]
            if val == target:
                return True
            elif val < target:
                l = mid + 1
            elif val > target:
                r = mid - 1
        return False


if __name__ == "__main__":
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    result = Solution().searchMatrix(matrix, target)
    print(result)
