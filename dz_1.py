import re
from exceptions import *


class Data:
    def __init__(self, data):
        self.data = data


    @classmethod
    def get_data(cls, data):
        day = data.split('-')[0]
        month = data.split('-')[1]
        year = data.split('-')[2]
        return day, month, year

    @staticmethod
    def validate_data(data):
        try:
            RE_DATE = re.compile(r'(?:\d{1,2}\-){2}\d{4}')
            if RE_DATE.match(data):
                day, month, year = Data.get_data(data)
                if int(day) not in range(1, 32):
                    raise WrongDay
                if int(month) not in range(1, 13):
                    raise WrongMonth
                if int(year) < 0:
                    raise WrongYear

            else:
                raise WrongDate
        except (WrongDate, WrongYear, WrongMonth, WrongDay) as err:
            print(err)
        else:
            return True


some_date = "03-12-1997"
test = Data(some_date)

if test.validate_data(some_date):
    Data.get_data(some_date)
    print("Данные верны")




# dz_2 Test my zero division exception
def my_div(num_1: int, num_2: int):
    try:
        if not num_2:
            raise MyZeroDIV
        result = num_1 / num_2
        return result
    except MyZeroDIV as err:
        print(err)

my_div(2, 0)

