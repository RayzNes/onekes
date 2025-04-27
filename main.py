import random
from map import generate_map, print_map
from player import Player, move_player, inspect_tile
from items import get_berry_effect


def main():
    # Инициализация игры
    map_size = 20
    game_map = generate_map(map_size)
    player = Player(map_size // 2, map_size // 2)

    while True:
        print_map(game_map, player)
        print(
            f"Голод: {player.hunger}, Жажда: {player.thirst}, Энергия: {player.energy}, Температура: {player.temperature}")

        # Получение действия игрока
        action = input("Введите действие (WASD для движения, I для осмотра, Q для выхода): ").lower()

        if action == 'q':
            print("Игра завершена!")
            break
        elif action in ['w', 'a', 's', 'd']:
            move_player(player, action, game_map)
        elif action == 'i':
            inspect_tile(player, game_map)

        # Обновление параметров игрока
        player.hunger = max(0, player.hunger - 1)
        player.thirst = max(0, player.thirst - 2)
        player.energy = max(0, player.energy - 1)

        # Проверка условий окончания игры
        if player.hunger == 0 or player.thirst == 0:
            print("Игра окончена! Вы умерли от голода или обезвоживания.")
            break


if __name__ == "__main__":
    main()