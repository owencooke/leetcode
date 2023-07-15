# Source: https://leetcode.com/problems/move-zeroes/
# Author: Owen Cooke


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first_zero = True
        z = -1
        for i in range(len(nums)):
            if nums[i] == 0 and first_zero:
                z = i
                first_zero = False
            elif nums[i] != 0 and z != -1:
                nums[z] = nums[i]
                nums[i] = 0
                z += 1


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    # nums = [1, 0, 1]
    Solution().moveZeroes(nums)
    print(nums)
