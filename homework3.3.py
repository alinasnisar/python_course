list_of_values = [7, 1, 3, 9, 5]

if not list_of_values:
    result = [[], []]
elif len(list_of_values) % 2 == 0:
    midpoint = len(list_of_values) // 2
    first_half = list_of_values[:midpoint]
    second_half = list_of_values[midpoint:]
    result = [first_half, second_half]
else:
    midpoint = len(list_of_values) // 2
    first_half = list_of_values[midpoint:]
    second_half = list_of_values[:midpoint]
    result = [first_half, second_half]

print(f"{list_of_values} => {result}")
