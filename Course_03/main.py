from array import array
from collections import deque

empty_list = []
my_list = [1, 4, 7, 9, 10]
print(my_list)
my_list.append(12)
print(my_list)
my_list.insert(1, 99)
print(my_list)
print(len(my_list))
my_list.remove(10)
print(my_list)
del my_list[2]
print(my_list)
other_list = my_list
other_list[0] = -1
print(my_list)

deep_copied_list = my_list[:]

another_list = [-1, 99, 7, 9, 12]
print(my_list == another_list)
list2 = ["abc", "abcd", "xyz"]

list3 = my_list + (list2 * 2)
print(list3)
list4 = list(list2[1])
print(list4)

list5 = list4[::-2]
print(list5)

first, *other, last = list4
print(first, last, other)
list4.reverse()
reversed(list4)
print(list4)
t = " ".join(reversed("abcd"))
print(t)

my_array = array("i", [4, 7, 9, 10])
my_array[0] = 99
print(my_array)

my_deque = deque(my_list)
print(my_deque)
my_deque.append(100)
my_deque.popleft()
print(my_deque)

my_tuple = (4,)
my_other_tuple = 7, 9
print(my_other_tuple)
a_tuple = ("a string",)
a_tuple_of_lists = (my_list,)
a_tuple_of_lists[0].append(198)

my_dictionary = {"John": 745123456, "Maria": 723555444, "George": 781999000}
print(my_dictionary["George"])
print(my_dictionary.get("george", -1))
my_dictionary["Jay"] = 766123789
my_dictionary["Maria"] = 123456
print(my_dictionary)
for kv in my_dictionary.items():
    print(kv[0], " ", kv[1])

my_set = {1, 3, 5, 1, 9, 99}
print(my_set)
my_other_set = set(my_list)
print(my_other_set)
print(my_set | my_other_set)  # set union
print(my_set & my_other_set)  # set intersection
print(my_set - my_other_set)  # set difference
print(my_set ^ my_other_set)  # set semantic difference
