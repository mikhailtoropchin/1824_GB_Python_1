# constant values
minute = 60
hour = minute * 60
day = hour * 24
#----------------
duration = 755869

if duration < minute:
    print(f"{duration} сек")
elif duration >= minute and duration < hour:
    print(f"{duration // minute} мин {duration % minute} сек")
elif duration >= hour and duration < day:
    print(f"{duration // hour} час {(duration % hour) // minute} мин {(duration % hour) % minute} сек")
elif duration >= day:
    print(f"{(duration // day)} дн {(duration % day) // hour} час {(duration % hour) // minute} мин {(duration % hour) % minute} сек")


# По примечанию
# list_of_durations = [645, 3942, 878465]
#
# for duration in list_of_durations:
#     if duration < minute:
#         print(f"{duration} сек")
#     elif duration >= minute and duration < hour:
#         print(f"{duration // minute} мин {duration % minute} сек")
#     elif duration >= hour and duration < day:
#         print(f"{duration // hour} час {(duration % hour) // minute} мин {(duration % hour) % minute} сек")
#     elif duration >= day:
#         print(
#             f"{(duration // day)} дн {(duration % day) // hour} час {(duration % hour) // minute} мин {(duration % hour) % minute} сек")
