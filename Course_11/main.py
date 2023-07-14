def fibonacci(maximum):
    a, b = 0, 1
    while a <= maximum:
        yield a
        a, b = b, a + b
    return a


generator = fibonacci(40)
for _ in range(0, 10):
    print(next(generator))


def say_hi():
    while True:
        the_name = yield
        yield f"Hi, {the_name}!"


generator2 = say_hi()
for _ in range(0, 3):
    next(generator2)
    name = input("Please enter your name: ")
    message = generator2.send(name)
    print(message)


def my_function():
    yield from fibonacci(20)


h = my_function()
for _ in range(0, 5):
    print(next(h))


