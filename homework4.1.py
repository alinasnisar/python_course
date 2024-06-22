listed_values = [31, 5, 8, 0, 4, 0, 23, 0, 3, 0, 1]

zero_values = 0
for i in range(len(listed_values)):
    if listed_values[i] != 0:
        listed_values[zero_values], listed_values[i] = listed_values[i], listed_values[zero_values]
        zero_values += 1
print(listed_values)
