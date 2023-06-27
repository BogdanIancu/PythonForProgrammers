import os
from pathlib import Path

file = open("file.txt", "w")
print(file.mode)

file.write("Hello, world!")
file.close()

with open("file.txt", "r") as g:
    g.seek(4)
    print(g.tell())
    text = g.read()
    print(text)

mac = "usr/bin"
windows = "usr\\bin"
location = os.path.join("usr", "bin")
print(location)

path = Path("usr") / "bin"
print(path)
path = Path("file.txt")
print(path.read_text())

a = 3
b = 0
if b != 0:
    c = a / b
    print(c)
else:
    print("You cannot divide by 0")

my_list = [1, 7, 2]
my_dictionary = {}
b = 2


def my_function():
    try:
        c = a / b
        print(c)
        print(my_list[2])
        print(my_dictionary["key"])
        return 0
    except (ArithmeticError, IndexError) as e:
        print(e)
        return -1
    except:
        print("Something else happened")
        return -1
    finally:
        print("Computation done")


def division(value1, value2):
    if value2 == 0:
        raise AttributeError("value is 0")
    else:
        return value1 / value2


print(my_function())


def caller():
    try:
        division(4, 2)
    except AttributeError as e:
        print(e)
    else:
        print("All good")
    finally:
        print("Finally")


caller()
