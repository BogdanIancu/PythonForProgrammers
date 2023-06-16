# Some different ways to split a long line
a = (2 + 2) * 3 + \
    4 * 12 \
    + 24

b = ((2 + 2) * 3 +
     4 * 12
     + 24)

c = [1, 2, 3,
     4, 5, 6]

x = 20
y = 3
z = x / y
print(z)

# How to compare two floats
if abs(z - 6.6666) < 0.009:
    print("They are equal")
else:
    print("They are not equal")

w = x // y
print(w)
q = x % y
print(q)
print(q ** 3)
x += 1
ok = "Ana" < "Anca"
print(ok)

s = "Something "
s += str(1)
print(s)

print(s != "something")

print(f"x = {x} y = {y}")
x, y = y, x
print(f"x = {x} y = {y}")

print(bool("False"))

drivers_age = 21
has_driving_license = True

if drivers_age >= 18 and has_driving_license:
    print("We can rent you a car")
elif drivers_age < 18:
    print("You do not have the legal age")
else:
    if not has_driving_license:
        print("You need a driving license")
    else:
        print("We CANNOT rent you a car")

# 1 New food order
# 2 Check please
# 3 Something to drink

option = int(input("Please select your option: "))
if option == 1:
    print("New food order")
elif option == 2:
    print("Check please")
elif option == 3:
    print("Something to drink")
else:
    print("Invalid option")

match option:
    case 1:
        print("New food order")
    case 2:
        print("Check please")
    case 3:
        print("Something to drink")
    case _:
        print("Invalid option")

age = drivers_age if 21 <= drivers_age <= 65 else -1
print(age)
print()

age = 60
while age < 65:
    print(age)
    age += 1

for i in range(3, 0, -2):
    print(i)

for c in s:
    print(c)

result = [c.lower() for c in s]
print(result)

while True:
    print("Inside the first while loop")
    while True:
        pass
        print("Inside the second while loop")
        break
    break

for item in range(0, 8, 2):
    if item % 2 == 1:
        print("Even number found")
        break
else:
    print("Even number not found")
