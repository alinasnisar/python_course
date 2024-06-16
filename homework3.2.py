list1 = [3, 14, 6, 31]
list2 = [4]
list3 = []

if len(list1) >= 2:
    last_element1 = list1[-1:]
    remaining_list1 = list1[:-1]
    reversed_list1 = last_element1 + remaining_list1
    print(f"{list1} => {reversed_list1}")
else:
    print(f"{list1} => {list1}")

if len(list2) >= 2:
    last_element2 = list2[-1:]
    remaining_list2 = list2[:-1]
    reversed_list2 = last_element2 + remaining_list2
    print(f"{list2} => {reversed_list2}")
else:
    print(f"{list2} => {list2}")

if len(list3) >= 2:
    last_element3 = list3[-1:]
    remaining_list3 = list3[:-1]
    reversed_list3 = last_element3 + remaining_list3
    print(f"{list3} => {reversed_list3}")
else:
    print(f"{list3} => {list3}")
