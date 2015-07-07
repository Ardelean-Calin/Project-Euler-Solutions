#!/usr/bin/python3


def main():
    # a won't be bigger than 333, otherwise b >= 334 and c >= 335
    for a in range(1, 333):
        for b in range(a, 500):  # b wont be bigger than 500 otherwise c = 501
            for c in range(b, 1000):  # c can go up to 997

                if(a + b + c != 1000):
                    continue

                if(a * a + b * b == c * c):
                    print(a, b, c)
                    print(a * b * c)
                    return

if __name__ == '__main__':
    main()
