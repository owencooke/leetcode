# Source: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
# Author: Owen Cooke


class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        result = []
        most = max(candies)
        for candy in candies:
            result.append(candy + extraCandies >= most)
        return result
