import keyword
import string

user_string = input("Введіть рядок: ")

result = True

if user_string[0].isdigit():
    result = False
elif user_string in keyword.kwlist:
    result = False
elif user_string.count("_") == len(user_string) and len(user_string) > 1:
    result = False

for char in user_string:
    if not result:
        break
    if char == "_":
        continue
    elif char.isupper():
        result = False
        break
    elif (char in string.punctuation or
            char.isspace()):
        result = False
        break
print(result)
