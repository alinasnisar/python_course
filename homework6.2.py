seconds = int(input("Введіть секунди: "))

if not isinstance(seconds, int) or seconds < 0 or seconds >= 8640000:
    print("Необхідне ввести ціле число, яке менше ніж 8640000.")
else:
    days = seconds // 86400
    remaining_seconds = seconds % 86400

    hours = remaining_seconds // 3600
    remaining_seconds %= 3600

    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60

    days_str = str(days).zfill(2)
    hours_str = str(hours).zfill(2)
    minutes_str = str(minutes).zfill(2)
    seconds_str = str(seconds).zfill(2)

    last_digit = days % 10
    if last_digit == 1 and last_digit != 11:
        word_day = "день"
    elif 2 <= last_digit <= 4:
        word_day = "дні"
    else:
        word_day = "днів"

    time_str = f"{days_str} {word_day}, {hours_str}:{minutes_str}:{seconds_str}"

    print(f"Введений час: {time_str}")
