import requests
import sys
from datetime import datetime
from decimal import Decimal


def currency_rates(valute: str) -> tuple:
    """
    Возвращает курс валюты и дату, которая передается в ответе с сайта ЦБ
    :param valute: название валюты в формате EUR
    :return: кортеж из двух элементов: 1 - Decimal курс валюты (либо None), 2 - дата и время в виде объекта date
    """
    r = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    if not r.ok:
        print(f'Запрос не успешен: {response.status_code}')
        sys.exit(0)

    middle_name = [] # достаем строку, разделяем по тэгу
    [middle_name.append(name.split("</CharCode")) for name in r.text.split("<CharCode>")]
    name_valute = [] # вырезаем то, что внутри тэга
    [name_valute.append(name[0]) for name in middle_name if len(name) > 1]
    middle_value = [] # достаем строку, разделяем по тэгу
    [middle_value.append(name.split("</Value")) for name in r.text.split("<Value>")]
    value_valute = [] # вырезаем то, что внутри тэга
    [value_valute.append(name[0]) for name in middle_value if len(name) > 1]
    result = dict(zip(name_valute, value_valute)) # словарь, где ключ - название валюты, а знач. - курс
    # Для получения даты:
    date_r = " ".join(r.headers.get("Date").split(" ")[1:-1])
    result_date = datetime.strptime(date_r, "%d %b %Y %H:%M:%S")
    if result.get(valute.upper()) == None: # это нужно для перевода курса в Decimal, иначе ошибка (если инпут неверный)
        return None, result_date
        sys.exit(0)
    ultimate_result = Decimal(result.get(valute.upper()).replace(',','.')) # переводим в Decimal
    return ultimate_result, result_date
    # как вариант возвращать строку, но мне неоч:
    # return f"Курс {valute}: {ultimate_result}\nВремя: {result_date}"


print(f"Курс доллара: {currency_rates('usd')[0]} \nКурс евро: {currency_rates('eUr')[0]}\
        \nВремя: {currency_rates('sd')[1]}")
