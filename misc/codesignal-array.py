# Given an array a, your task is to apply the following mutation to it:
# Array a mutates into a new array b of the same length
# For each i from 0 to a.length - 1 inclusive, b[i] = a[i - 1] + a[i] + a[i + 1]
# If some element in the sum a[i - 1] + a[i] + a[i + 1] does not exist, it is considered to be 0
# For example, b[0] equals 0 + a[0] + a[1]

def solution(a):
    b = []
    for i in range(len(a)):
        if i != 0:
            b.append(sum(a[i-1:i+2]))
        else:
            b.append(sum(a[i:i+2]))
    return b