# Source: https://leetcode.com/problems/valid-palindrome/
# Author: Owen Cooke


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(ch for ch in s if ch.isalnum()).lower()
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    result = Solution().isPalindrome(s)
    print(result)
