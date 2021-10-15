distorted_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for name in distorted_list:
    print(f"'Привет, {name.split()[-1].capitalize()}!'")
