# coding: utf-8
import sys

def prime_numbers(n):
    l = [*range(n+1)]
    for i in range(2, n+1):
        if l[i] < 1: continue
        for j in range(2*i, n+1, i):
            l[j] = 0
    return l


if __name__ == '__main__':
    if len(sys.argv) < 2:
        n = 100
    else:
        n = int(sys.argv[1])
    primes = prime_numbers(n)
    print('prime numbers')
    for p in primes[2:]:
        if p > 0: print(p)
