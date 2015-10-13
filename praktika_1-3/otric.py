# Подключаем библиотеку для тестирования
import unittest
# Подключаем тестируемую библиотеку
import lib

# Класс, описывающий набор тестов
class LibTest(unittest.TestCase):

    # Тестируем работу
    def test_palindrom_fd(self):
        # Набор проверок
        self.assertTrue(lib.palindrome('asdsa'))
        self.assertFalse(lib.palindrome('asdf'))
        self.assertTrue(lib.palindrome('asfsa'))
        self.assertTrue(lib.palindrome('0'))



# Запускаем тесты на исполнение
unittest.main(verbosity=2)