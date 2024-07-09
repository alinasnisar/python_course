users_input = int(input("Введіть ціле число: "))

if not isinstance(users_input, int):
    print("Неправильний тип даних")
    exit()

product = 1

while users_input > 9:
    for digit in str(users_input):
        product *= int(digit)

    users_input = product
    product = 1

print(f"Результат: {users_input}")
