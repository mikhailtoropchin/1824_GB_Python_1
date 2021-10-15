default_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for idx in range(len(default_list)):
    if default_list[idx].isdigit():
        default_list[idx] = f"{int(default_list[idx]):02}"
    else:
        for name in default_list[idx]:
            if name.isdigit() and "+" in default_list[idx]:
                default_list[idx] = f"+{int(name):02}"
            elif name.isdigit() and "-" in default_list[idx]:
                default_list[idx] = f"-{int(name):02}"

print(" ".join(default_list))
# з.ы. Так и не смог in place добавить скобки.
