import random


class Environment:
    def __init__(self):
        self.time_of_day = "День"  # День или Ночь
        self.weather = "Ясно"  # Ясно, Дождь, Снег


def update_environment(env, turn):
    # Обновление времени суток (цикл 10 ходов: 5 день, 5 ночь)
    if turn % 10 < 5:
        env.time_of_day = "День"
    else:
        env.time_of_day = "Ночь"

    # Обновление погоды (10% шанс смены каждые 5 ходов)
    if turn % 5 == 0 and random.random() < 0.1:
        env.weather = random.choice(["Ясно", "Дождь", "Снег"])