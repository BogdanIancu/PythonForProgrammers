# this is a comment

# this
# will be
# a comment on
# multiple lines

"""
this is
a multiline string
"""
PI = 3.14  # this is a constant in Python (naming convention)

path = r"C:\User\Someone\folder"  # raw string
prompt = 'Please input user\'s name: '
prompt = prompt.rstrip()  # right strip
name = input(prompt)
s = f"Hello, {name}! 😀"
s = s.replace(",", "")
print(s)
print("-" * 20)
age = input("Please input your age: ")
birthdate_year = 2023 - int(age)
print(birthdate_year)
a = 3.5
b = int(a)
print(b)
is_it_true_or_not = "1" == 1
print(is_it_true_or_not)
is_containing_b = "B" in name
print(is_containing_b)
name_copy = name[:]
print(name)
index = prompt.find("input")  # will return -1 is not found
print(index)
sql_command = """SELECT * FROM students
WHERE student_id = 9"""
print(sql_command)
