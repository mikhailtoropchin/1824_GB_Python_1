from random import choice

jokes_count = int(input("Сколько шуток хотите? "))


def get_jokes(n: int, not_repeated: object = False) -> list:
    """Возвращает случайно сгенерированные шутки"""

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    result = []
    count = 0

    while count < n:
        chosen_noun = choice(nouns)
        chosen_adverb = choice(adverbs)
        chosen_adjective = choice(adjectives)
        if not_repeated:  # Не более 5 уникальных шуток, иначе ошибка.
            nouns.remove(chosen_noun)
            adverbs.remove(chosen_adverb)
            adjectives.remove(chosen_adjective)
        result.append(f"{chosen_noun} {chosen_adverb} {chosen_adjective}")
        count += 1
    return result

print(get_jokes(jokes_count, not_repeated=True))
