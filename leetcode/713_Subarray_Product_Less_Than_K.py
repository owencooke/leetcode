# Source: https://leetcode.com/problems/subarray-product-less-than-k/
# Author: Owen Cooke


class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prod = 1
        combos = l = 0
        for r, val in enumerate(nums):
            prod *= val
            while l <= r and prod >= k:
                prod /= nums[l]
                l += 1
            combos += r - l + 1
        return combos


if __name__ == "__main__":
    nums = [10, 5, 2, 6]
    k = 100
    result = Solution().numSubarrayProductLessThanK(nums, k)
    print(result)
