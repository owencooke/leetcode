# Source: https://leetcode.com/problems/greatest-common-divisor-of-strings/
# Author: Owen Cooke


class Solution:
    def isDivisible(self, s: str, x: str) -> str:
        return "" == "".join(s.split(x))

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        x = ""
        max_length_x = min(len(str1), len(str2))
        for i in range(1, max_length_x + 1):
            div = str1[:i]
            if self.isDivisible(str1, div) and self.isDivisible(str2, div):
                x = div
        return x


if __name__ == "__main__":
    str1 = "ABABAB"
    str2 = "ABAB"
    result = Solution().gcdOfStrings(str1, str2)
    print(result)
