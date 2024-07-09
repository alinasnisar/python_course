import string

while True:
    start_char, end_char = input("Введіть два символи через дефіс: ").split("-")

    all_chars = list(string.ascii_letters)

    if start_char not in all_chars or end_char not in all_chars:
        print("Невірні символи. Спробуйте ще раз.")
        continue

    start_idx = all_chars.index(start_char)
    end_idx = all_chars.index(end_char)
    result = "".join(all_chars[start_idx: end_idx + 1])
    print(result)
    break
