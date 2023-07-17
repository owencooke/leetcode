# Source: https://leetcode.com/problems/container-with-most-water/
# Author: Owen Cooke


class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        area = 0
        while l < r:
            h = min(height[l], height[r])
            width = r - l
            area = max(area, h * width)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return area


if __name__ == "__main__":
    height = [1, 3, 2, 5, 25, 24, 5]
    result = Solution().maxArea(height)
    print(result)
