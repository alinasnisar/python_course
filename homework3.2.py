list_vales1 = [15, 7, 5, 11, 9]
list_vales1[::] = list_vales1[-1:] + list_vales1[:-1]
print(list_vales1)

list_vales2 = [6]
list_vales2[::] = list_vales2[-1:] + list_vales2[:-1]
print(list_vales2)

list_vales3 = []
list_vales3[::] = list_vales3[-1:] + list_vales3[:-1]
print(list_vales3)
