import random

def get_berry_effect():
    # Получение эффекта ягод
    if random.random() < 0.7:  # 70% шанс съедобных ягод
        return {
            'description': 'Вкусные ягоды',
            'edible': True,
            'hunger': 10,
            'thirst': 5
        }
    else:
        return {
            'description': 'Ядовитые ягоды',
            'edible': False,
            'hunger': 20,
            'thirst': 10
        }