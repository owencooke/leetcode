# Source: https://leetcode.com/problems/merge-strings-alternately/
# Author: Owen Cooke


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        p1, p2 = 0, 0
        n1, n2 = len(word1), len(word2)
        while p1 < n1 and p2 < n2:
            if p2 >= p1:
                s += word1[p1]
                p1 += 1
            else:
                s += word2[p2]
                p2 += 1
        s += word2[p2:]
        s += word1[p1:]
        return s


if __name__ == "__main__":
    word1 = "abcd"
    word2 = "pq"
    result = Solution().mergeAlternately(word1, word2)
    print(result)
