#!/usr/bin/python3
import math


def is_prime(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def main():
    sum = 0
    for i in range(2, 2000001):
        sum += i if is_prime(i) else 0
    print(sum)

if __name__ == '__main__':
    main()
