def do_sum(first_value, second_value=1):
    """
    A function to compute the sum of two numbers
    :param first_value: first number
    :param second_value: second number
    :return: the sum
    """
    return first_value + second_value


print(do_sum(2, 5))


def interchange(a, b):
    aux = a[0]
    a[0] = b[0]
    b[0] = aux


x = [3]
y = [5]
interchange(x, y)
print(x, y)

result = do_sum(second_value=x[0], first_value=y[0])
print(result)

print(do_sum(9))


def multiply(*numbers):
    if len(numbers) == 0:
        return 0
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(5, 6, 7))
print(multiply())


def print_employee_details(**employee):
    x = 7  # this is a local variable that will shadow the global one
    print(employee, x)
    print(employee["id"], employee["name"], employee["salary"])


def do_operation(operation, value1, value2):
    return operation(value1, value2)


if __name__ == "__main__":
    print_employee_details(id=1, name="John", salary=3000)
    print(do_operation(multiply, 5, 6))
    print(do_operation(lambda v1, v2: v1 ** v2, 5, 3))
