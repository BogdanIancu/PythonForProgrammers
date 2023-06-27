import os
from pathlib import Path

file = open("file.txt", "w")
file.write("Hello, world!")
file.close()

with open("file.txt", "r") as g:
    g.seek(4, 0)
    print(g.tell())
    print(g.read())

windows = r"\\usr\\bin"
mac = "user/bin"
print(os.path.join("usr", "bin"))

path = Path("user") / "bin"
print(path)

file_path = Path("file.txt")
content = file_path.read_text()
print(content)

a = 3
b = 1

if b != 0:
    print(a/b)
else:
    print("b is 0")

my_list = [1, 2, 3]


def function(index):
    try:
        r = a / b
        print(r)
        if 0 <= index < len(my_list):
            print(my_list[index])
        else:
            raise IndexError
        return 0
    except (ZeroDivisionError, LookupError) as e:
        print(e)
        raise
    except:
        print("Something bad happened")
        return -1
    finally:
        print("Finally code")


try:
    print(function(2))
except IndexError as e:
    print("Exception handled globally", e)
else:
    print("NO ERROR TO HANDLE")
