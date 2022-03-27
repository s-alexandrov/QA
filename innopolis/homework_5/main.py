import random
from typing import Any
from abc import ABC, abstractmethod


class Game:
    """Главный класс игры."""
    hero_character = ""
    hero_attack = 10
    hero_hp = 15
    item_type = ""
    inventory = {}

    def __init__(self) -> None:
        self.monster_count = 0
        self.hero_character = ""
        self.hero_attack = 10
        self.hero_hp = 15
        self.monster_attack = 0
        self.monster_hp = 0
        self.item_type = ""
        self.sword_item = 0
        self.bow_item = 0
        self.book_magic_item = 0
        self.totem_item = 0
        self.inventory = {}
        self.itemsword = ItemSword
        self.itemtotem = ItemTotem
        self.itembookmagic = ItemBookMagic
        self.itemarrows = ItemArrows
        self.itembow = ItemBow

    def begin_game(self) -> Any:
        """Запуск игры."""
        print("Игра началась! Вы должны убить 10 монстров. Выбирите тип героя: 1 - воин, 2 - лучник, 3 - маг.")
        if self.monster_count >= 10:
            print("Игра закончилась! Вы победили 10 монстров!")
            exit()
        else:
            self.hero_choice()

    def hero_choice(self) -> None:
        """Выбор типа героя"""
        print("Выбирите тип героя: 1 - воин, 2 - лучник, 3 - маг")
        hero_input = input()
        if hero_input == "1":
            print(f"Теперь вы воин мечник! Ваша атака = {self.hero_attack} и hp = {self.hero_hp}. "
                  f"Ваше оружие в начале игры - меч.")
            self.hero_character = "berserk"
            self.item_spawner()
        elif hero_input == "2":
            print(f"Теперь вы лучник! Ваша атака = {self.hero_attack} и hp = {self.hero_hp}. "
                  f"Ваше оружие в начале игры - меч.")
            self.hero_character = "archer"
            self.item_spawner()
        elif hero_input == "3":
            print(f"Теперь вы маг! Ваша атака = {self.hero_attack} и hp = {self.hero_hp}. "
                  f"Ваше оружие в начале игры - меч.")
            self.hero_character = "wizard"
            self.item_spawner()
        else:
            print("Вы ввели неверное значение, попробуйте еще раз.")
            self.hero_choice()

    def item_spawner(self) -> None:
        """Рандом игровых процессов."""
        random_spawner = random.randint(1, 2)
        if random_spawner == 1:
            self.monster_spawner()  # Вызывам монстра
            self.response_to_monster()  # После появления монстра решаем атаковать или бежать
        elif random_spawner == 2:
            self.object_spawner()  # Вызываем предмет
            self.response_to_item()  # После появления предмета решаем взять его или нет
        else:
            print("Вы ввели неправильное число, можно только 1 или 2")

    def response_to_monster(self) -> None:
        """Реакция героя на появления монстра."""
        print("Вы можете атаковать его (1) или убежать (2).")
        input_response_to_monster = input()
        if input_response_to_monster == "1":
            print("Вы решили атаковать. Но автор еще пока не придумал как реализовать бой. Поэтому начинаем заново. =)")
            self.item_spawner()
        elif input_response_to_monster == "2":
            self.run()
        else:
            print("Вы ввели некорректное число, попробуйте еще раз.")
            self.response_to_monster()

    def response_to_item(self) -> None:
        """Реакция героя на появления предмета."""
        print("Вы можете взять предмет (1) или пройти мимо (2).")
        input_response_to_item = input()
        if input_response_to_item == "1":
            print("Вы взяли предмет.")
            self.take_item()
        elif input_response_to_item == "2":
            self.run()
        else:
            print("Вы ввели некорректное число, попробуйте еще раз.")
            self.response_to_item()

    def take_item(self) -> None:
        """Взять предмет в инвентарь."""
        if self.item_type == "тотем":
            self.itemtotem.take_item()
        if self.item_type == "лук":
            self.itembow.take_item()
        if self.item_type == "стрелы":
            self.itemarrows.take_item()
        if self.item_type == "меч":
            self.itemsword.take_item()
        if self.item_type == "книга магии":
            self.itembookmagic.take_item()

    def run(self) -> None:
        """Побег от монстра."""
        print("Вы прошли мимо! Продолжаем.")
        self.item_spawner()

    def monster_spawner(self) -> None:
        """Рандом монстров."""
        item_monster = {
            "ogre": OgreFactory,
            "goblin": GoblinFactory,
            "necromancer": NecromancerFactory,
        }
        list_item_monster = ["ogre", "goblin", "necromancer"]
        random_monster = random.choice(list_item_monster)
        item_monster[random_monster](Game)

    def object_spawner(self) -> None:
        """Генератор предметов."""
        item_spawner = {
            "sword": SwordFactory,
            "bow": BowFactory,
            "arrows": ArrowsFactory,
            "book_magic": BookMagicFactory,
            "apple": AppleFactory,
            "totem": TotemFactory,
        }
        list_item_spawner = ["sword", "bow", "arrows", "book_magic", "apple", "totem"]
        random_spawner = random.choice(list_item_spawner)
        item_spawner[random_spawner](Game)


class Monsters(ABC):
    """Абстрактный класс игровых мнстров."""

    def __init__(self, game: Any) -> None:
        """Инициализация класса."""
        super().__init__()
        self.game = game


    @abstractmethod
    def spawn(self) -> None:
        """Пораждение монстра. Метод, наличие которого обязательно у всех."""
        print("Вы встретили монстра!")


class MonsterOgre(Monsters):
    """Класс огра мечника."""

    def __init__(self, game: Any, attack, hp) -> None:
        """Инициализация класса."""
        self.game = game
        super().__init__(self.game)
        self.attack = attack
        self.hp = hp

    def spawn(self) -> None:
        self.monster_attack = self.attack
        self.monster_hp = self.hp
        print(f"Вы встретили огра мечник с атакой = {self.attack} и hp = {self.hp}")


class MonsterGoblin(Monsters):
    """Класс огра мечника."""

    def __init__(self, game: Any, attack, hp) -> None:
        """Инициализация класса."""
        self.game = game
        super().__init__(self.game)
        self.attack = attack
        self.hp = hp

    def spawn(self) -> None:
        self.monster_attack = self.attack
        self.monster_hp = self.hp
        print(f"Вы встретили гоблина лучника с атакой = {self.attack} и hp = {self.hp}")


class MonsterNecromancer(Monsters):
    """Класс огра мечника."""

    def __init__(self, game: Any, attack, hp) -> None:
        """Инициализация класса."""
        self.game = game
        super().__init__(self.game)
        self.attack = attack
        self.hp = hp

    def spawn(self) -> None:
        self.monster_attack = self.attack
        self.monster_hp = self.hp
        print(f"Вы встретили мага некроманта с атакой = {self.attack} и hp = {self.hp}")


class MonsterFactory(ABC):
    """Абстракная фабрика монстров"""

    def __init__(self, game: Any) -> None:
        self.game = game
        super().__init__()
        self.create_monster()

    @abstractmethod
    def create_monster(self) -> object:
        pass


class OgreFactory(MonsterFactory):
    """Фабрика огров."""

    def __init__(self, game: Any) -> None:
        self.game = game
        super().__init__(self.game)

    def create_monster(self) -> None:
        attack = random.randint(5, 20)
        hp = random.randint(10, 30)
        ogre = MonsterOgre(self.game, attack, hp)
        ogre.spawn()


class GoblinFactory(MonsterFactory):
    """Фабрика гоблинов."""

    def __init__(self, game: Any) -> None:
        self.game = game
        super().__init__(self.game)

    def create_monster(self) -> None:
        attack = random.randint(5, 20)
        hp = random.randint(5, 25)
        goblin = MonsterGoblin(self.game, attack, hp)
        goblin.spawn()


class NecromancerFactory(MonsterFactory):
    """Фабрика огров."""

    def __init__(self, game: Any) -> None:
        self.game = game
        super().__init__(self.game)

    def create_monster(self) -> None:
        attack = random.randint(10, 30)
        hp = random.randint(5, 20)
        necromancer = MonsterNecromancer(self.game, attack, hp)
        necromancer.spawn()


class Items(ABC):
    """Абстрактный класс игровых предметов."""

    def __init__(self, game: Any) -> None:
        """Инициализация класса."""
        super().__init__()
        self.game = game

    @abstractmethod
    def spawn(self) -> None:
        """Пораждение монстра. Метод, наличие которого обязательно у всех."""
        print("Вы получили предмет!")

    @abstractmethod
    def take_item(self) -> None:
        """Берем игровой предмет в инвентарь. Метод, наличие которого обязательно у всех."""
        print("Вы взяли предмет!")


class ItemSword(Items):
    """Класс меча."""
    def __init__(self, game: Any, power: int) -> None:
        self.game = game
        super().__init__(self.game)
        self.power = power

    def spawn(self) -> None:
        print(f"Мы нашли меч с силой атаки {self.power}")

    def take_item(self) -> None:
        print("Вы положили предмет в инвентарь.")
        self.game.sword_item = 1
        print("Кол-во предметов ", self.game.sword_item)
        self.game.item_spawner()


class ItemBow(Items):
    """Класс лука."""
    def __init__(self, game: Any) -> None:
        self.game = game
        super().__init__(self.game)

    def spawn(self) -> None:
        print(f"Вы нашли лук. Не забудьте найти стрелы к нему.")

    def take_item(self) -> None:
        print("Вы положили предмет в инвентарь.")
        self.game.bow_item = 1
        print("Кол-во предметов ", self.game.bow_item)
        self.game.item_spawner()


class ItemArrows(Items):
    """Класс стрел."""
    def __init__(self, game: Any, amount: int, power: int) -> None:
        self.game = game
        super().__init__(self.game)
        self.amount = amount
        self.power = power

    def spawn(self) -> None:
        print(f"Вы нашли стрелы({self.amount} шт). Сила атаки одной стрелы {self.power}")

    def take_item(self) -> None:
        print("Вы положили предмет в инвентарь.")
        self.game.bow_item = self.amount
        print("Кол-во предметов ", self.game.bow_item)
        self.game.item_spawner()


class ItemBookMagic(Items):
    """Класс книги заклинаний."""
    def __init__(self, game: Any, power: int) -> None:
        self.game = game
        super().__init__(self.game)
        self.power = power

    def spawn(self) -> None:
        print(f"Вы нашли книгу заклинаний с силой атаки {self.power}")

    def take_item(self) -> None:
        print("Вы положили предмет в инвентарь.")
        self.game.book_magic_item = 1
        print("Кол-во предметов ", self.game.book_magic_item)
        self.game.item_spawner()


class ItemApple(Items):
    """Класс яблочка."""
    def __init__(self, game: Any, apple_hp: int, hero_hp: int) -> None:
        self.game = game
        super().__init__(self.game)
        self.apple_hp = apple_hp
        self.game.hero_hp = hero_hp

    def spawn(self) -> None:
        print(f"Вы нашли яблочко, ваше hp увеличислось на {self.apple_hp} и теперь = {self.game.hero_hp}")
        # self.game.item_spawner()

    def take_item(self) -> None:
        print("Вы съели яблокочко.")
        pass


class ItemTotem(Items):
    """Класс тотема."""
    def __init__(self, game: Any) -> None:
        self.game = game
        super().__init__(self.game)

    def spawn(self) -> None:
        print(f"Вы нашли тотем и могли бы сохранить игру, но автор пока не придумал как это сделать. =)")

    def take_item(self) -> None:
        print("Вы положили предмет в инвентарь.")
        self.game.totem_item = 1
        print("Кол-во предметов ", self.game.totem_item)
        self.game.item_spawner()


class ItemsFactory(ABC):
    """Абстрактная фабрика предметов."""

    def __init__(self, game: Any) -> None:
        self.game = game
        super().__init__()
        self.create_items()

    @abstractmethod
    def create_items(self) -> object:
        pass


class SwordFactory(ItemsFactory):
    """Фабрика мечей."""
    def __init__(self, game: Any) -> None:
        self.game = game
        super().__init__(self.game)

    def create_items(self) -> None:
        self.game.item_type = "меч"
        power = random.randint(5, 20)
        if self.game.hero_character == "berserk":
            power += 5
        sword = ItemSword(self.game, power)
        sword.spawn()


class BowFactory(ItemsFactory):
    """Фабрика луков."""
    def __init__(self, game: Any) -> None:
        self.game = game
        super().__init__(self.game)

    def create_items(self) -> None:
        self.game.item_type = "лук"
        bow = ItemBow(self.game)
        bow.spawn()


class ArrowsFactory(ItemsFactory):
    """Фабрика стрел."""
    def __init__(self, game: Any) -> None:
        self.game = game
        super().__init__(self.game)

    def create_items(self) -> None:
        self.game.item_type = "стрелы"
        amount = random.randint(1, 5)
        power = random.randint(5, 20)
        if self.game.hero_character == "archer":
            power += 5
        arrows = ItemArrows(self.game, amount, power)
        arrows.spawn()


class BookMagicFactory(ItemsFactory):
    """Фабрика книг магии."""
    def __init__(self, game: Any) -> None:
        self.game = game
        super().__init__(self.game)

    def create_items(self) -> None:
        self.game.item_type = "книга магии"
        power = random.randint(5, 20)
        if self.game.hero_character == "wizard":
            power += 5
        book_magic = ItemBookMagic(self.game, power)
        book_magic.spawn()


class AppleFactory(ItemsFactory):
    """Фабрика яблок."""
    def __init__(self, game: Any) -> None:
        self.game = game
        super().__init__(self.game)

    def create_items(self) -> None:
        apple_hp = random.randint(1, 10)
        self.game.hero_hp += apple_hp
        apple = ItemApple(self.game, apple_hp, self.game.hero_hp)
        apple.spawn()


class TotemFactory(ItemTotem):
    """Фабрика тотемов."""
    def __init__(self, game: Any) -> None:
        self.game = game
        super().__init__(self.game)

    def create_items(self) -> None:
        totem = ItemTotem(self.game)
        totem.spawn()


if __name__ == "__main__":
    heroes = Game()
    heroes.begin_game()
