# Source: https://leetcode.com/problems/can-place-flowers/
# Author: Owen Cooke


class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        # Notes:
        # 1. order matters (once one is potted, it must be changed for next check)
        # 2. potential KeyErrors can be fixed by adding 0 onto each end of
        # the array (since the ends of the flowerbed are considered empty)
        numPlanted = 0
        flowerbed = [0, *flowerbed, 0]
        for i in range(1, len(flowerbed) - 1):
            if not flowerbed[i - 1] and not flowerbed[i] and not flowerbed[i + 1]:
                flowerbed[i] = 1
                numPlanted += 1
        return numPlanted >= n
