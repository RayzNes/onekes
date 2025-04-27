import random
from math import sqrt


def generate_map(size):
    # Генерация карты (двумерный список)
    game_map = [['.' for _ in range(size)] for _ in range(size)]
    objects = ['T', 'B', 'W', 'R', 'A']
    weights = [0.1, 0.1, 0.05, 0.1, 0.05]  # Вероятности появления объектов

    for i in range(size):
        for j in range(size):
            if random.random() < 0.3:  # 30% шанс размещения объекта
                game_map[i][j] = random.choices(objects, weights)[0]

    return game_map


def print_map(game_map, player, env):
    # Вывод карты с учетом видимости ночью
    size = len(game_map)
    for i in range(size):
        for j in range(size):
            # Расстояние от игрока
            distance = sqrt((player.x - j) ** 2 + (player.y - i) ** 2)
            if env.time_of_day == "Ночь" and distance > 2:
                print('?', end=' ')  # Не видно дальше 2 клеток ночью
            else:
                if i == player.y and j == player.x:
                    print('@', end=' ')
                else:
                    print(game_map[i][j], end=' ')
        print()