# Source: https://leetcode.com/problems/asteroid-collision/
# Author: Owen Cooke


class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        addedStack = False
        stack = []
        prev_stack = []
        while len(asteroids) > 1 and (prev_stack != asteroids or addedStack):
            prev_stack = list(asteroids)
            a1 = asteroids.pop()
            a2 = asteroids.pop()
            if a1 < 0 and a2 > 0:
                # signs different (negative) and facing each other (negative after positive), one cancels unless equal
                if abs(a1) > abs(a2):
                    asteroids.append(a1)
                elif abs(a2) > abs(a1):
                    asteroids.append(a2)
                # if equal, both explode -> remove both
                stack.reverse()
                asteroids += stack
                stack = []
                addedStack = True
            else:
                asteroids.append(a2)
                stack.append(a1)
                addedStack = False
        stack.reverse()
        return asteroids + stack
