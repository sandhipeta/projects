my_list = [2, 4, 6, 10, 1]

result = []

for i in range(len(my_list)):
    total = my_list[i]
    for j in range(len(my_list)):
        if (i != j) and (my_list[j] > my_list[i]):
            total += my_list[j]
    result.append(total)


print(result)