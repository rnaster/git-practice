import random


def power(x):
    return x * x


if __name__ == '__main__':
    print('print random number: %d' % random.randint(0, 100))
    rand = random.random()
    if rand < 0.3:
        print('not bad')
    elif rand < 0.6:
        print('good')
    elif rand < 0.9:
        print('great')
    else:
        print('excellent')
    print('power operation')
    rand_list = [random.randint(0, 20) for _ in range(5)]
    print('origin:', *rand_list)
    print('power:', *map(power, rand_list))
    print('random number list')
    print(*[round(random.random(), 4) for _ in range(10)])
