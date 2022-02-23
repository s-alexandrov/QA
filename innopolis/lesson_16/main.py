import random

hp = 10
attack = 10
monster_counter = 0


def player_turn() -> int:
    """Генерируем случайное число от 1 до 3: бой с монстром, получает яблочко или меч."""
    move = int(random.randint(1, 3))
    return move


def apple() -> int:
    """Определяем сколько бонусов получит рыцарь к здоровью."""
    add_hp = int(random.randint(1, 5))
    global hp
    hp += add_hp
    print(
        "Вы получили яблочко +",
        add_hp,
        "hp. Кол-во ваших жизней увеличилось на",
        add_hp,
        "и теперь =",
        hp,
        "\n",
    )
    return add_hp


def sword() -> int:
    """Выпадение меча. Игрок может взять меч(1) или отказаться(2)"""
    global attack
    add_attack = int(random.randint(5, 20))
    print(
        "Вы нашли меч с силой атаки:",
        add_attack,
        "Сейчас ваша сила атаки =",
        attack,
        "\nНажмите 1 (взять меч) или 2 (выбросить меч)",
    )
    take_sword_or_not = int(input())
    if take_sword_or_not == 1:
        attack = add_attack
        print("Вы взяли новый меч, теперь ваша сила атаки =", attack, "\n")
        return attack
    elif take_sword_or_not == 2:
        print("Вы выбросили меч, ваша сила атаки осталась =", attack, "\n")
        return attack
    else:
        print("Вы ввели неверное значение, введите 1 или 2")
        take_sword_or_not = int(input())
        return take_sword_or_not


def game():
    """Главная функция боя."""
    global attack  # текущая сила удара героя
    global hp  # текущее состояние здоровье героя
    global monster_counter  # счетчик поверженных героем чудовищ
    while monster_counter < 10:
        g_player_turn = (
            player_turn()
        )  # Вызываем функцию которая определяет 1-монстр, 2-яблоко, 3-меч
        if g_player_turn == 1:
            monster_health = int(random.randint(1, 20))  # жизни монстра
            monster_power = int(random.randint(1, 15))  # сила удара монстра
            print(
                "БОЙ! Вы встретили монстра с",
                monster_health,
                "жизнями и силой удара:",
                monster_power,
                "\nСейчас кол-во ваших жизней:",
                hp,
                "и сила атаки:",
                attack,
                "\nВведите 1, чтобы атаковать или 2, чтобы убежать",
            )
            fight_or_run = int(input())
            if fight_or_run == 1:
                if attack > monster_health:
                    hp -= monster_power  # Уменьшаем кол-во жизни рыцаря отнимая силы атаки монстра
                    if hp <= 0:  # Если после боя у рыцаря <= 0 hp - он тоже умирает
                        print(
                            "ПОРАЖЕНИЕ! После атаки кол-во ваших жизней стало =",
                            hp,
                            "Попробуйте еще раз",
                        )
                        return False
                    else:
                        monster_counter += 1  # Увеличиваем счетчик побед
                        print(
                            "ПОБЕДА! Вы победили уже",
                            monster_counter,
                            "раз. Теперь ваше здоровье =",
                            hp,
                            "\n",
                        )
                else:
                    print("ПОРАЖЕНИЕ! Попробуйте сыграть еще раз")
                    return False
            if (
                fight_or_run == 2
            ):  # Если игрок не берет меч - опять выкидываем числло от 1 до 3
                player_turn()
        if g_player_turn == 2:  # Вызываем функцию получения яблочка
            apple()
        if g_player_turn == 3:  # Вызываем функцию получения мяча
            sword()
    print("Вы победели всех монстров! Игра закончена!")


game()
