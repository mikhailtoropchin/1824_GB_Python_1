"""
2. Пользователь вводит время в секундах.
   Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""

time = int(input("Введите время в секундах: "))

hour = 0
minute = 0
second = 0

if time <= 60:
    second = time
    print(f"{hour:02}:{minute:02}:{second:02}")
elif 60 < time < 3600:
    minute = time // 60
    second = time % 60
    print(f"{hour:02}:{minute:02}:{second:02}")
elif time >= 3600:
    hour = time // 3600
    minute = (time % 3600) // 60
    second = (time % 3600) % 60
    print(f"{hour:02}:{minute:02}:{second:02}")

