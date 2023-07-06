# Source: https://leetcode.com/problems/valid-parentheses/
# Author: Owen Cooke


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        brackets = {"}": "{", "]": "[", ")": "("}
        stack = []
        for char in s:
            if char in "({[":
                stack.append(char)
            elif not stack or brackets[char] != stack.pop():
                return False
        return not stack


if __name__ == "__main__":
    s = "){"
    result = Solution().isValid(s)
    print(result)
