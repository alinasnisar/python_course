value1 = float(input("Введіть число"))
mathematical_operation = input("Введіть математичну операцію: +, -, /, *")
value2 = float(input("Введіть число"))

if mathematical_operation == "+":
    result = value1 + value2
elif mathematical_operation == "-":
    result = value1 - value2
elif mathematical_operation == "/" and value2 != 0:
    result = value1 / value2
elif mathematical_operation == "*":
    result = value1 * value2
else:
    result = "Неправильна операція"

print(f"{value1} {mathematical_operation} {value2} = {result}")

