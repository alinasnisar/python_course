listed_values = [0, 5, 8, 9, 3, 6]

if not listed_values:
    result = 0
else:
    indexes = 0
    for i in range(len(listed_values)):
        if i % 2 == 0:
            indexes += listed_values[i]

    result = indexes * listed_values[-1]

print(result)
