import sys
import random


if __name__ == '__main__':
    if len(sys.argv) < 2:
        iteration = 1000
    else:
        iteration = int(sys.argv[1])
    print(iteration, type(iteration))
    cnt = 0
    for _ in range(iteration):
        x = random.random()
        y = random.random()
        if y > x:
            cnt += 1
    print('1 x 1 retangle area: %.4f' % (cnt / iteration))
