import random


def generate_map(size):
    # Генерация карты
    game_map = [['.' for _ in range(size)] for _ in range(size)]
    objects = ['T', 'B', 'W', 'R', 'A']
    weights = [0.1, 0.1, 0.05, 0.1, 0.05]  # Вероятности появления объектов

    for i in range(size):
        for j in range(size):
            if random.random() < 0.3:  # 30% шанс размещения объекта
                game_map[i][j] = random.choices(objects, weights)[0]

    return game_map


def print_map(game_map, player):
    # Вывод карты
    for i in range(len(game_map)):
        for j in range(len(game_map[0])):
            if i == player.y and j == player.x:
                print('@', end=' ')
            else:
                print(game_map[i][j], end=' ')
        print()