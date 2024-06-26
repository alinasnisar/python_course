list_of_values = [9, 4, 1, 3, 7]

if not list_of_values:
    result = [[], []]
elif len(list_of_values) % 2 == 0:
    midpoint = len(list_of_values) // 2
    first_half = list_of_values[:midpoint]
    second_half = list_of_values[midpoint:]
    result = [first_half, second_half]
else:
    midpoint = len(list_of_values) // 2 + 1
    first_half = list_of_values[:midpoint]
    second_half = list_of_values[midpoint:]
    result = [first_half, second_half]

print(f"{list_of_values} => {result}")

# my_list = [1, 2, 3, 9, 4, 5, 6]
#
# separator = len(my_list) - len(my_list) // 2
# new_list = [my_list[:separator], my_list[separator:]]
#
# print(new_list)
