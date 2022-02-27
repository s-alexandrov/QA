import unittest
from unittest import TestCase
from unittest.mock import patch

import importlib

rpg = importlib.import_module("main")


class RpgTestCase(TestCase):
    """Юнит тест для домашнего задания 1."""

    def setUp(self) -> None:
        """Начальные условия для тестов."""
        self.input = ""
        self.victory_count = 0
        self.fail_count = 0

    def fake_io_with_asserts(self, *args):
        """Обработка print() и input() в программе с проверками результата."""
        last_io = "".join(args)
        if "БОЙ" in last_io:
            self.input = "1"
        elif "МЕЧ" in last_io:
            self.input = "2"
        elif "ПОБЕДА" in last_io:
            self.assertEqual(rpg.monster_counter, 10)
            self.assertTrue(rpg.hp > 0)
            self.victory_count += 1
            self.input = "\n"
        elif "ПОРАЖЕНИЕ" in last_io:
            self.assertTrue(rpg.monster_counter < 10)
            self.assertTrue(rpg.hp <= 0)
            self.fail_count += 1
            self.input = "\n"
        else:
            self.input = "\n"
        return last_io

    def test_game_e2e(self):
        """Тест, выполняющий полностью прохождение игры."""
        with patch("builtins.print", new=self.fake_io_with_asserts):
            with patch("builtins.input", side_effect=lambda _: self.input):
                with self.assertRaises(SystemExit):
                    rpg.game()

    def test_game_e2e_until_at_least_one_victory(self):
        """Тест, проверяющий что в игру возможно когда-нибудь выиграть."""
        with patch("builtins.print", new=self.fake_io_with_asserts):
            with patch("builtins.input", side_effect=lambda _: self.input):
                while self.victory_count == 0:
                    with self.assertRaises(SystemExit):
                        rpg.game()
        self.assertEqual(self.victory_count, 1)


if __name__ == "__main__":
    unittest.main()
