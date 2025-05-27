import doctest
import math


class Rectangle:
    # передаем два аргумента в конструктор класса
    def __init__(self, height: float = 1.0, length: float = 1.0):
        """
        Создание и подготовка к работе объекта "Прямоугольник"

        :param height: Высота прямоугольника
        :param length: Ширина прямоугольника

        Примеры:
        >>> x = Rectangle(1, 2)     # корректное создание объекта
        >>> y = Rectangle(4, 5)     # корректное создание объекта
        >>> j = Rectangle('5', '6') # некорректное создание объекта
        Traceback (most recent call last):
        ...
        TypeError: Вводимый результат должен быть флоатером или целым числом
        """

        if not isinstance(height, (int, float)):
            raise TypeError('Вводимый результат должен быть флоатером или целым числом')
        if height <= 0:
            raise ValueError('Сторона прямоугольника не может быть равна или меньше нуля')
        # конвертируем аргумент в атрибут экземпляра класса
        self.height = height

        if not isinstance(length, (int, float)):
            raise TypeError('Вводимый результат должен быть флоатером или целым числом')
        if length <= 0:
            raise ValueError('Сторона прямоугольника не может быть равна или меньше нуля')
        # конвертируем аргумент в атрибут экземпляра класса
        self.length = length

    # создаем метод экземпляра класса (т.к. есть self)
    def get_rectangle_area(self) -> float:
        """
        Рассчитываем площадь прямоугольника.

        :return: Площадь прямоугольника

        Пример:
        >>> y = Rectangle(3, 4)  # инициализация экземпляра класса
        >>> y.get_rectangle_area()
        12
        """

        self.area = self.height * self.length
        return self.area

    def get_rectangle_perimeter(self) -> float:
        """
        Рассчитываем периметр прямоугольника.

        :return: Периметр прямоугольника

        Пример:
        >>> y = Rectangle(3, 4)
        >>> y.get_rectangle_perimeter()
        14
        """
        
        self.perimeter = 2 * (self.length + self.height)
        return self.perimeter

    def get_rectangle_diagonal(self) -> float:
        """
        Рассчитываем диагональ прямоугольника
        :return: Получаем диагональ

        Пример:
        >>> y = Rectangle(3, 4)
        >>> y.get_rectangle_diagonal()
        5.0
        """
        
        half_perimeter = self.get_rectangle_perimeter() / 2  # высчитывается полупериметр прямоугольника
        
        rectangle_diagonal = math.sqrt((half_perimeter ** 2) # высчитывается диагональ прямоугольника
                                       - (2 * self.get_rectangle_area()))
        return rectangle_diagonal


doctest.testmod()  # тестирование примеров, которые находятся в документации
