import utils
import sys


# просто рандомные тестовые вызовы
print(f"Курс доллара: {utils.currency_rates('usd')[0]} \nКурс евро: {utils.currency_rates('eur')[0]}\
        \nвремя: {utils.currency_rates('usd')[1]}")
print(utils.currency_rates('rub'))
some_valute = utils.currency_rates('azn')
eur = utils.currency_rates("eUr")
print(eur[0])
print(some_valute)
