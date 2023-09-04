# Source: https://leetcode.com/problems/reverse-vowels-of-a-string/
# Author: Owen Cooke


class Solution:
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    def reverseVowels(self, s: str) -> str:
        s = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] in self.vowels:
                if s[r] in self.vowels:
                    s[l], s[r] = s[r], s[l]
                    l += 1
                r -= 1
            else:
                l += 1
        return "".join(s)
