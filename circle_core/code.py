import math
import doctest


class Circle:
    # передаем два аргумента в конструктор класса. Аргументы имеют значения "по умолчанию".
    def __init__(self, radius: float = 1, angle: int = 0):
        """
        Создание и подготовка к работе объекта "Круг".
        :param radius: Радиус круга.
        :param angle: Угол, образованный от центра окружности, если известен. Если аргумент пропущен, то 0.

        Примеры:
        >>> x = Circle(3)       # создание экземпляра класса Circle с передачей аргумента 3.
        >>> y = Circle(33, 40)  # создание экземпляра класса Circle с передачей аргумента 33 для радиуса и 40 для угла.
        >>> j = Circle('33')    # неправильное создание экземпляра класса Circle
        Traceback (most recent call last):
        ...
        TypeError: Вводимое число должно быть флоатером или целым числом
        """
        
        if not isinstance(radius, (int, float)):
            raise TypeError('Вводимое число должно быть флоатером или целым числом')
        if radius <= 0:
            raise ValueError('Значение радиуса не должно быть меньше или равно 0')
        self.radius = radius

        if not isinstance(angle, int):
            raise TypeError('Угол окружности должен быть целым числом')
        if angle < 0:
            self.angle = angle * (-1)
        self.angle = math.radians(angle)

    def circle_perimeter(self) -> float:
        """
        Рассчитываем периметр круга
        :return: Получаем периметр

        Пример:
        >>> y = Circle(2)
        >>> y.circle_perimeter().__round__(2)
        12.57
        """
        
        # Высчитывается из геометрической формулы. Формула: P = 2 * pi * R
        perimeter = 2 * math.pi * self.radius
        
        return perimeter
        
    def circle_area(self) -> float:
        """
        Рассчитываем площадь круга
        :return: Получаем площадь

        Пример:
        >>> y = Circle(2)
        >>> y.circle_area().__round__(2)
        12.57
        """
        
        # Площадь (S) высчитывается из геометрической формулы. Формула: S = 2 * pi * R ** 2
        s = math.pi * math.pow(self.radius, 2)
        
        return s
        
    def get_chord_length(self) -> float:
        """
        Рассчитываем хорду окружности
        :return: Получаем хорду окружности

        Пример:
        >>> y = Circle(2, 40)
        >>> y.get_chord_length().__round__(2)
        1.37
        """
        
        # Хорда высчитывается исходя из геометрической формулы по нахождению длины хорды,
        # когда известен радиус и величина угла в радиусах. Формула: AB = 2 * R * sin(alpha / 2)
        chord_length = 2 * self.radius * math.sin(self.angle / 2)
        
        return chord_length


doctest.testmod()

