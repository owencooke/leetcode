# Source: https://leetcode.com/problems/max-number-of-k-sum-pairs/
# Author: Owen Cooke


class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        if len(nums) == 1 or k == 1:
            return 0
        nums.sort()
        ops = 0
        l, r = 0, len(nums) - 1
        while l < r:
            total = nums[l] + nums[r]
            if k == total:
                ops += 1
                l += 1
                r -= 1
            elif total > k:
                r -= 1
            else:
                l += 1
        return ops


if __name__ == "__main__":
    nums = [1, 2]
    k = 1
    result = Solution().maxOperations(nums, k)
    print(result)
