a way to delete an element from a tuple directly

my_tuple = (1, 2, 3, 4, 5)
element_to_delete = 3
my_list = list(my_tuple)
my_list.remove(element_to_delete)
new_tuple = tuple(my_list)
print(new_tuple)

how to convert a tuple to a set in Python

my_tuple = (1, 2, 3)
my_set = set(my_tuple)
print(my_set)