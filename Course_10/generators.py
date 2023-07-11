import random


def lucky_number():
    while True:
        yield random.randint(1, 49)


counter = 0
for n in lucky_number():
    counter += 1
    print(n)
    if counter >= 6:
        break

