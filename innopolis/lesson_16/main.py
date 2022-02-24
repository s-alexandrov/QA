import random

hp = 10
attack = 10
monster_counter = 0


def player_turn() -> int:
    """Генерируем случайное число от 1 до 3: бой с монстром, получает яблочко или меч."""
    move = random.randint(1, 3)
    return move


def apple() -> int:
    """Определяем сколько бонусов получит рыцарь к здоровью."""
    add_hp = random.randint(1, 5)
    global hp
    hp += add_hp
    print("Вы получили яблочко +", add_hp, "hp. Кол-во ваших жизней увеличилось на", add_hp, "и теперь =", hp, "\n",)
    return add_hp


def sword() -> int:
    """Выпадение меча. Игрок может взять меч(1) или отказаться(2)"""
    global attack
    add_attack = random.randint(5, 20)
    print("Вы нашли МЕЧ с силой атаки:", add_attack, "Сейчас ваша сила атаки =", attack,
          "\nНажмите 1 (взять меч) или 2 (выбросить меч)",)
    take_sword_or_not = int(input())
    if take_sword_or_not == 1:
        attack = add_attack
        print("Вы взяли новый меч, теперь ваша сила атаки =", attack, "\n")
        return attack
    elif take_sword_or_not == 2:
        print("Вы выбросили меч, ваша сила атаки осталась =", attack, "\n")
        return attack
    else:
        while take_sword_or_not != 1 and take_sword_or_not != 2:  # Добиваемся ввода правильного числа пользователя
            print("Вы ввели неверное значение, введите 1 или 2")
            take_sword_or_not = int(input())
        return take_sword_or_not


def game():
    """Главная функция боя."""
    global attack  # текущая сила удара героя
    global hp  # текущее состояние здоровье героя
    global monster_counter  # счетчик поверженных героем чудовищ
    while monster_counter < 10:
        g_player_turn = player_turn()  # Вызываем функцию которая определяет 1-монстр, 2-яблоко, 3-меч
        if g_player_turn == 1:
            monster_health = random.randint(1, 20)  # жизни монстра
            monster_power = random.randint(1, 15)  # сила удара монстра
            print("БОЙ! Вы встретили монстра с", monster_health, "жизнями и силой удара:", monster_power,
                  "\nСейчас кол-во ваших жизней:", hp, "и сила атаки:", attack,
                  "\nВведите 1, чтобы атаковать или 2, чтобы убежать")
            fight_or_run = int(input())
            while fight_or_run != 1 and fight_or_run != 2:  # Добиваемся ввода правильного числа пользователя
                print("Вы ввели неверное значение, введите 1 или 2")
                fight_or_run = int(input())
            if fight_or_run == 1:
                while hp > 0 and monster_health > 0:
                    hp -= monster_power  # Уменьшаем кол-во жизни рыцаря отнимая силу атаки монстра
                    monster_health -= attack  # Уменьшаем кол-во жизни монстра отнимая силу атаки рыцаря
                    if hp > monster_health and hp > 0:
                        player_turn()
                    if hp <= 0:
                        print("ПОРАЖЕНИЕ! Попробуйте сыграть еще раз.")
                        return False
                monster_counter += 1
                print("ПОБЕДА! Кол-во побед:", monster_counter, "из 10. Ваше здоровье:", hp,
                      "Здоровье монстра:", monster_health, "\n")
            if fight_or_run == 2:
                player_turn()
        if g_player_turn == 2:  # Вызываем функцию получения яблочка
            apple()
        if g_player_turn == 3:  # Вызываем функцию получения мяча
            sword()
    print("Вы победели всех монстров! Игра закончена!")


game()