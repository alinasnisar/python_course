def difference(*args):
    if not args:
        return 0
    min_num = max_num = args[0]
    for num in args[1:]:
        min_num = min(min_num, num)
        max_num = max(max_num, num)

    if abs(max_num - min_num) >= 0.01:
        return round(max_num - min_num, 2)
    else:
        return max_num - min_num


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
