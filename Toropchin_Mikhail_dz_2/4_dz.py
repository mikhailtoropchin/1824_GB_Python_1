distorted_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

print([f"Привет, {str(name.split()[-1].capitalize())}!" for name in distorted_list])

for name in distorted_list:
    print(f"Привет, {name.split()[-1].capitalize()}!")