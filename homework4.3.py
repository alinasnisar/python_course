# Ввести значення самостійно
# listed_values = [6, 3, 7]
#
# if len(listed_values) <= 2:
#     result = "Введіть три числа"
# else:
#     result = listed_values[0], listed_values[2], listed_values[-2]
# print(result)

# Згенерувати рандомні числа
import random

random_length = random.randint(3, 10)
random_values = [random.randint(1, 100) for _ in range(random_length)]

new_values = random_values[0], random_values[2], random_values[-2]

print(f"{random_values} => {new_values}")
