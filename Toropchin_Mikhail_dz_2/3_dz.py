default_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
list_of_numbers = []

for idx in range(len(default_list)):
    if default_list[idx].isdigit():
        if len(default_list[idx]) == 1:
            list_of_numbers.append('"')
            list_of_numbers.append(f"0{default_list[idx]}")
            list_of_numbers.append('"')
        else:
            list_of_numbers.append('"')
            list_of_numbers.append(default_list[idx])
            list_of_numbers.append('"')

    if not default_list[idx].isdigit():
        part_list = list(default_list[idx])
        if "+" in part_list or "-" in part_list:
            for x in part_list:
                if x.isdigit():
                    list_of_numbers.append('"')
                    list_of_numbers.append(f"+0{x}")
                    list_of_numbers.append('"')
        else:
            list_of_numbers.append(default_list[idx])


print(default_list)
print(list_of_numbers)
print(" ".join(list_of_numbers))
