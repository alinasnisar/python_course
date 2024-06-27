list1 = [3, 14, 6, 31]

if len(list1) >= 2:
    last_element1 = list1[-1:]
    remaining_list1 = list1[:-1]
    reversed_list1 = last_element1 + remaining_list1
    print(f"{list1} => {reversed_list1}")
else:
    print(f"{list1} => {list1}")

# original_list = [12, 5, 6, 7, 8]
#
# if len(original_list) > 1:
#     last_element = original_list.pop()
#     original_list.insert(0, last_element)
# print(original_list)
