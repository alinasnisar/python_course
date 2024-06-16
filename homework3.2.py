list_of_values = [18, 7, 31, 4]
if len(list_of_values) >= 2:
    list_of_values[::] = list_of_values[-1:] + list_of_values[:-1]

print(list_of_values)

one_value_list = [5]
if len(one_value_list) >= 2:
    one_value_list[::] = one_value_list[-1:] + one_value_list[:-1]

print(one_value_list)

empty_list = []
if len(empty_list) >= 2:
    empty_list[::] = empty_list[-1:] + empty_list[:-1]

print(empty_list)

list_of_values2 = [3, 11, 7, 4, 21]
if len(list_of_values2) >= 2:
    list_of_values2[::] = list_of_values2[-1:] + list_of_values2[:-1]

print(list_of_values2)
