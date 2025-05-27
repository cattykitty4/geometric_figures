import doctest
import math


class Triangle:
    def __init__(self, a_side: float, b_side: float, c_side: float):
        """
        Создание и подготовка к работе объекта Треугольник.
        :param a_side: Сторона a
        :param b_side: Сторона b
        :param c_side: Сторона c

        Примеры:
        >>> x = Triangle(4, 5, 6)       # корректное создание объекта
        >>> y = Triangle(7, 8, 9)       # корректное создание объекта
        >>> j = Triangle('7', '8', '9') # некорректное создание объекта
        Traceback (most recent call last):
        ...
        ValueError: Длина одной стороны треугольника не может превосходить сумму длин двух других его сторон.
        """
        # Производится проверка на правило "Неравенства треугольника"
        if a_side + b_side < c_side or a_side + c_side < b_side or b_side + c_side < a_side:
            raise ValueError('Длина одной стороны треугольника не может превосходить сумму длин двух других его сторон.')

        # Производится проверка на корректность вводимых данных
        if not isinstance(a_side, (int, float)):
            raise TypeError('Вводимое число должно быть флоатером или целым числом.')
        if not isinstance(b_side, (int, float)):
            raise TypeError('Вводимое число должно быть флоатером или целым числом.')
        if not isinstance(c_side, (int, float)):
            raise TypeError('Вводимое число должно быть флоатером или целым числом.')

        self.a_side = a_side
        self.b_side = b_side
        self.c_side = c_side

    def get_basic_info(self):
        """
        :return: Возвращает общую информацию о треугольнике. Периметр, полупериметр и площадь по формуле Герона

        Пример:
        >>> x = Triangle(12, 10, 10)
        >>> x.get_basic_info() # Полупериметр 16, Периметр 32, Площадь 48.
        (16.0, 32.0, 48.0)
        """
        half_perimeter = (self.a_side + self.b_side + self.c_side) / 2
        area = math.sqrt(half_perimeter *
            (half_perimeter - self.a_side) * (half_perimeter - self.b_side) * (half_perimeter - self.c_side))

        return half_perimeter, half_perimeter * 2, round(area, 2)

    def get_triangle_height(self):
        """
        :return: Возвращает высоту треугольника

        Пример:
        >>> x = Triangle(12, 10, 10)
        >>> x.get_triangle_height()
        8.0
        """
        area = self.get_basic_info()[2]
        return (2 * area) / self.a_side


doctest.testmod()
