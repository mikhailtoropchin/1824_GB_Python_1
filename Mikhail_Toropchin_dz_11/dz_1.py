import re
from exceptions import *

class Data:

    def __init__(self, date):
        self.date = date

    @classmethod
    def extract_date(cls, date):
        day = int(date[:2])
        month = int(date[3:5])
        year = int(date[6:])
        return day, month, year


    @staticmethod
    def validate_date(date):
        try:
            RE_DATE = re.compile(r'(?:\d{2}[./-]){2}\d{4}')
            if RE_DATE.match(date):
                day, month, year = Data.extract_date(date)
                if int(day) not in range(1, 32):
                    raise WrongDay(day)
                if int(month) not in range(1, 13):
                    raise WrongMonth
                if int(year) < 0:
                    raise WrongYear(year)
            else:
                raise WrongDate
        except (WrongDate, WrongDay, WrongMonth, WrongYear) as err:
            print(err)
        else:
            return True


d = "13-11-1231"
example = Data(d)

if example.validate_date(d):
    Data.extract_date(d)
