import random


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

