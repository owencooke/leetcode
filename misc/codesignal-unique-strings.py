# You are given a string s. Your task is to count the number of ways of splitting s into three non-empty parts
#  a, b and c (s = a + b + c) in such a way that a + b, b + c and c + a are all different strings.

def solution(s):
    unique = 0
    for i in range(1, len(s)-1):
        a = s[:i]
        sub = s[i:]
        for j in range(1, len(sub)):
            b = sub[:j]
            c = sub[j:]
            if (a+b)!=(b+c) and (b+c)!=(c+a) and (a+b)!=(c+a):
                unique += 1
    return unique