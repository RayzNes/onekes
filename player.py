from items import get_berry_effect
import random


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hunger = 100  # Голод
        self.thirst = 100  # Жажда
        self.energy = 100  # Энергия
        self.temperature = 37  # Температура тела
        self.inventory = []  # Инвентарь


def move_player(player, direction, game_map):
    # Движение игрока
    new_x, new_y = player.x, player.y

    if direction == 'w' and player.y > 0:
        new_y -= 1
    elif direction == 's' and player.y < len(game_map) - 1:
        new_y += 1
    elif direction == 'a' and player.x > 0:
        new_x -= 1
    elif direction == 'd' and player.x < len(game_map[0]) - 1:
        new_x += 1

    # Проверка возможности хода
    if game_map[new_y][new_x] != 'W':  # Нельзя ходить по воде
        player.x, player.y = new_x, new_y
    else:
        print("Нельзя пройти в воду!")


def inspect_tile(player, game_map):
    # Осмотр клетки
    tile = game_map[player.y][player.x]

    if tile == 'B':
        if random.random() < 0.5:  # 50% шанс найти ягоды
            effect = get_berry_effect()
            print(f"Найдены ягоды! Эффект: {effect['description']}")
            player.inventory.append(effect)
            if effect['edible']:
                player.hunger = min(100, player.hunger + effect['hunger'])
                player.thirst = min(100, player.thirst + effect['thirst'])
                print("Ягоды съедены, голод и жажда уменьшены.")
            else:
                player.hunger = max(0, player.hunger - effect['hunger'])
                player.thirst = max(0, player.thirst - effect['thirst'])
                print("Ягоды оказались ядовитыми! Голод и жажда увеличились.")
        else:
            print("На этом кусте ягод нет.")
    elif tile == '.':
        print("Просто пустая земля.")
    elif tile == 'T':
        print("Крепкое дерево.")
    elif tile == 'W':
        print("Водоём.")
    elif tile == 'R':
        print("Большой камень.")
    elif tile == 'A':
        print("Дикое животное. Лучше не беспокоить!")