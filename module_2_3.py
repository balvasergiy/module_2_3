my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
pozit = []
no = -1
while len(pozit) < len(my_list):
    no += 1
    if my_list[no] < 0: break
    pozit.append(my_list[no])
print(pozit)
