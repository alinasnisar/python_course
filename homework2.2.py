numbers_of_users = input("Введіть 5-ти значне число")
number = int(numbers_of_users)

digit1 = number % 10
digit2 = (number % 100) // 10
digit3 = (number % 1000) // 100
digit4 = (number % 10000) // 1000
digit5 = number // 10000
print(digit1,digit2,digit3,digit4,digit5)
