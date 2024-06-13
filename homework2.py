numbers_of_users = input("Введіть 4-х значне число")
number=int(numbers_of_users)

digit1 = number // 1000
digit2 = (number % 1000) // 100
digit3 = (number % 100) // 10
digit4 = number % 10

print(digit1)
print(digit2)
print(digit3)
print(digit4)
