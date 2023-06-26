# Source: https://leetcode.com/problems/binary-search/
# Author: Owen Cooke


class Solution:
    def search(self, nums, target):
        l = 0
        split = 1
        while split != 0:
            split = len(nums) // 2
            if target == nums[split]:
                return split + l
            elif target > nums[split]:
                nums = nums[split:]
                l += split
            else:
                nums = nums[:split]
        return -1


if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    result = Solution().search(nums, target)
    print(result)
