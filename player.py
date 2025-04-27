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
        self.inventory = {}  # Инвентарь как словарь {описание: количество}
        self.in_shelter = False  # Находится ли в шалаше

    def get_inventory_display(self):
        # Форматированный вывод инвентаря
        if not self.inventory:
            return "Пусто"
        return ", ".join(f"{desc}: {count}" for desc, count in self.inventory.items())

    def add_to_inventory(self, item_description, count=1):
        # Добавление предмета в инвентарь
        if item_description in self.inventory:
            self.inventory[item_description] += count
        else:
            self.inventory[item_description] = count


def move_player(player, direction, game_map, env):
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
        # Проверка на животное
        if game_map[new_y][new_x] == 'A':
            choice = input("Животное на пути! Охотиться (H) или убежать (R)? ").lower()
            if choice == 'h':
                if random.random() < 0.4:  # 40% шанс успешной охоты
                    print("Охота удалась! Получено мясо.")
                    player.add_to_inventory("Мясо")
                    player.hunger = min(100, player.hunger + 30)
                    game_map[new_y][new_x] = '.'  # Животное исчезает
                else:
                    print("Охота провалилась! Вы ранены.")
                    player.energy = max(0, player.energy - 20)
                    return  # Не двигаемся
            else:
                print("Вы убежали от животного.")
                return  # Не двигаемся

        player.x, player.y = new_x, new_y
        player.in_shelter = (game_map[new_y][new_x] == 'S')  # Проверяем, вошли ли в шалаш
    else:
        print("Нельзя пройти в воду!")


def inspect_tile(player, game_map):
    # Осмотр клетки
    tile = game_map[player.y][player.x]

    if tile == 'B':
        print("Вы видите куст с ягодами. Они выглядят свежими.")
        if random.random() < 0.5:  # 50% шанс найти ягоды
            effect = get_berry_effect()
            print(f"Найдены ягоды! Эффект: {effect['description']}")
            player.add_to_inventory(effect['description'])
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
    elif tile == 'T':
        print("Вы видите высокое дерево с густой листвой.")
        if random.random() < 0.3:  # 30% шанс собрать ветки
            print("Собраны ветки с дерева.")
            player.add_to_inventory("Ветки")
        else:
            print("Не удалось собрать ветки.")
    elif tile == '.':
        print("Вы видите пустую землю, покрытую травой.")
    elif tile == 'W':
        print("Вы видите водоём с чистой водой.")
    elif tile == 'R':
        print("Вы видите большой серый камень.")
    elif tile == 'A':
        print("Вы видите дикое животное, оно насторожено.")
    elif tile == 'S':
        print("Вы видите шалаш, сделанный из веток.")


def build_shelter(player, game_map):
    # Постройка шалаша
    if game_map[player.y][player.x] != '.':
        print("Шалаш можно построить только на пустой земле!")
        return

    # Проверка наличия веток
    branches = player.inventory.get("Ветки", 0)
    if branches < 3:
        print("Нужно минимум 3 ветки для постройки шалаша!")
        return

    # Уменьшение количества веток
    player.inventory["Ветки"] -= 3
    if player.inventory["Ветки"] == 0:
        del player.inventory["Ветки"]

    game_map[player.y][player.x] = 'S'  # Шалаш на карте
    player.in_shelter = True
    print("Шалаш построен! Вы в безопасности.")