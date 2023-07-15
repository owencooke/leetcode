# Source: https://leetcode.com/problems/move-zeroes/
# Author: Owen Cooke


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[first_zero], nums[i] = nums[i], nums[first_zero]
                first_zero += 1


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    Solution().moveZeroes(nums)
    print(nums)
