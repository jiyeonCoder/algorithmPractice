# Description
# ※ Use Standrad input and output to solve this challenge

# Print a n by m grid of asterisks.

# Constrratins
# The first line contains 2-separated integers, n and m.

# 1 ≤ n, m ≤ 1,000
# Examples
# Input

# 5 3
# Output

# *****
# *****
# *****

a, b = map(int, input().strip().split(' '))
for i in range(b):
    print(a*('*'))
