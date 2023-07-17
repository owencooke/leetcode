# Source: https://leetcode.com/problems/is-subsequence/
# Author: Owen Cooke


class Solution:
    def isSubsequence(self, sub: str, seq: str) -> bool:
        sub_i, seq_i = 0, 0
        while sub_i < len(sub) and seq_i < len(seq):
            if seq[seq_i] == sub[sub_i]:
                sub_i += 1
            seq_i += 1
        return len(sub) == sub_i


if __name__ == "__main__":
    sub = "abc"
    seq = "ahbgdc"
    result = Solution().isSubsequence(sub, seq)
    print(result)
