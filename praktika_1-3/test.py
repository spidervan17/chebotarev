# Подключаем библиотеку для тестирования
import unittest
# Подключаем тестируемую библиотеку
import lib

# Класс, описывающий набор тестов
class LibTest(unittest.TestCase):

    # Тестируем работу sqrt с положительными аргументами
    def test_even_non_negative_arg(self):
        # Набор проверок
        self.assertTrue(lib.even(0))
        self.assertTrue(lib.even(14))
        self.assertFalse(lib.even(-1))

    def test_even_negative(self):
        # Набор проверок
        self.assertFalse(lib.even(-1))
        self.assertTrue(lib.even(-2))

# Запускаем тесты на исполнение
unittest.main(verbosity=2)
