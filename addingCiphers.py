# Description
# Given a natural number N as the parameter, write a function solution to return the sum of each digit of N.
# For example, if N = 123, return 1 + 2 + 3 = 6.

# Constraints
# Range of N : natural number less than or equal to 100,000,000.
def solution(n):
    answer = 0
    for i in str(n):
        answer += int(i)
    return answer
