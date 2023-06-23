# Source: https://leetcode.com/problems/maximum-average-subarray-i/
# Author: Owen Cooke
# Date: 06/10/2023


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        s = sum(nums[:k])
        max_s = s
        for l in range(len(nums) - k):
            s += nums[l + k] - nums[l]
            max_s = max(s, max_s)
        return max_s / k


if __name__ == "__main__":
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    result = Solution().findMaxAverage(nums, k)
    print(result)
