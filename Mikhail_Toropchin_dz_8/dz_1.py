# Написать функцию email_parse(<email_address>),
# которая при помощи регулярного выражения извлекает имя пользователя и почтовый домен
# из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError.
import re


def name_is_valid(name):
    RE_NAME = re.compile(r'\b([\w./-]*)\@(\w*\.\w*)\b')
    if RE_NAME.match(name):
        parsed = RE_NAME.findall(name)
        result_dict = {}
        result_dict.setdefault("username", parsed[0][0])
        result_dict.setdefault("domain", parsed[0][1])
        return result_dict
    else:
        msg = f'wrong email: {name}'
        raise ValueError(msg)

print(name_is_valid("fu12-efvi@mail.com"))
