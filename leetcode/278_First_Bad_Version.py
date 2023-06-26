# Source: https://leetcode.com/problems/first-bad-version/description/
# Author: Owen Cooke


# Mock API function for problem
def isBadVersion(version: int) -> bool:
    return version >= BAD


class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1 if isBadVersion(1) else 0
        l, r = 1, n
        while l <= r:
            v = (l + r) // 2
            if isBadVersion(v):
                r = v - 1
            else:
                l = v + 1
        return l


if __name__ == "__main__":
    n = 3
    BAD = 2
    result = Solution().firstBadVersion(n)
    print(result)
