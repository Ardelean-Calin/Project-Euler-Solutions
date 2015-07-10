#!/usr/bin/python3

limit = 2000001
nums = [i for i in range(2, limit)]
x = [True for i in range(0, limit)]

# Sieve of Eratosthenes algorithm
for i, j in enumerate(nums):
    # Start from (i+2)^2 with a step of i+2
    for k in range((i + 2) * (i + 2), nums[-1] + 1, (i + 2)):
        x[k] = False

x.pop(0)
x.pop(0)
d = dict(zip(nums, x))

sum_ = 0
for key, value in d.items():
    if value is True:
        sum_ += key

print(sum_)
