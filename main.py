import random
from map import generate_map, print_map
from player import Player, move_player, inspect_tile, build_shelter
from items import get_berry_effect
from environment import Environment, update_environment


def main():
    # Инициализация игры
    map_size = 20
    game_map = generate_map(map_size)
    player = Player(map_size // 2, map_size // 2)
    env = Environment()

    turn = 0
    while True:
        # Отображение карты и состояния
        print_map(game_map, player)
        print(
            f"Голод: {player.hunger}, Жажда: {player.thirst}, Энергия: {player.energy}, Температура: {player.temperature}")
        print(f"Время: {env.time_of_day}, Погода: {env.weather}, Ход: {turn}")
        print(f"Инвентарь: {player.get_inventory_display()}")

        # Получение команды игрока
        action = input(
            "Введите действие (WASD для движения, I для осмотра, B для постройки шалаша, Q для выхода): ").lower()

        if action == 'q':
            print("Игра завершена!")
            break
        elif action in ['w', 'a', 's', 'd']:
            move_player(player, action, game_map, env)
        elif action == 'i':
            inspect_tile(player, game_map)
        elif action == 'b':
            build_shelter(player, game_map)

        # Обновление окружающей среды
        update_environment(env, turn)

        # Обновление параметров игрока
        player.hunger = max(0, player.hunger - 1)
        player.thirst = max(0, player.thirst - 2)
        player.energy = max(0, player.energy - 1)

        # Влияние погоды и времени суток на температуру
        temp_change = 0
        if env.time_of_day == "Ночь":
            temp_change -= 2
        if env.weather == "Дождь":
            temp_change -= 1
        elif env.weather == "Снег":
            temp_change -= 3
        if player.in_shelter:
            temp_change += 2  # Шалаш защищает от холода
        player.temperature = max(0, min(100, player.temperature + temp_change))

        # Проверка условий смерти
        if player.hunger == 0 or player.thirst == 0 or player.temperature == 0:
            print("Игра окончена! Вы умерли от голода, обезвоживания или переохлаждения.")
            break

        turn += 1


if __name__ == "__main__":
    main()