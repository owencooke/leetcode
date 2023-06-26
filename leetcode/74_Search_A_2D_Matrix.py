# Source: https://leetcode.com/problems/search-a-2d-matrix/
# Author: Owen Cooke


class Solution:
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        length = m * n - 1 if n != 0 else m - 1
        l = 0
        while length != 0:
            length = length // 2
            val = matrix[(length + l) // n][(length + l) % n]
            if target == val:
                return True
            elif target > val:
                l += length
        return False


if __name__ == "__main__":
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    result = Solution().searchMatrix(matrix, target)
    print(result)
