import random


class Environment:
    def __init__(self):
        self.time_of_day = "Утро"  # Утро, День, Вечер, Ночь
        self.weather = "Солнечно"  # Солнечно, Дождь, Снег


def update_environment(env, turn):
    # Обновление времени суток (цикл 10 ходов: Утро, День, Вечер, Ночь)
    cycle = turn % 10
    if cycle < 2.5:
        env.time_of_day = "Утро"
    elif cycle < 5:
        env.time_of_day = "День"
    elif cycle < 7.5:
        env.time_of_day = "Вечер"
    else:
        env.time_of_day = "Ночь"

    # Обновление погоды (30% шанс смены каждые 20 ходов)
    if turn % 20 == 0 and random.random() < 0.3:
        env.weather = random.choice(["Солнечно", "Дождь", "Снег"])