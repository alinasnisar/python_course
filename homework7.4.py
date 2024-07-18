def common_elements():
    first_list = [x for x in range(100) if x % 3 == 0]
    second_list = [x for x in range(100) if x % 5 == 0]

    common_values = set(first_list) & set(second_list)

    return common_values


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("OK")
