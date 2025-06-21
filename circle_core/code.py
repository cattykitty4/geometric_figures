import math
import doctest


class Circle:

    count_of_callings = 0

    # передаем два аргумента в конструктор класса. Аргументы имеют значения "по умолчанию".
    def __init__(self, radius: float = 1, angle: float = 0):
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

        self.add_one_to_amount_of_callings()

    @classmethod
    def add_one_to_amount_of_callings(cls):
        # метод класса для подсчета созданных экземпляров класса
        cls.count_of_callings += 1

    def __str__(self):
        # метод для человекочитаемого вывода Circle()
        return f'Этот класс создан для выполнения расчетов для окружности со следующими параметрами: \
        radius = {self.radius}, angle = {math.degrees(self.angle):.1f}°'

    def __repr__(self):
        # метод для воссоздания экземляра класса Circle()
        return f'circle_example = {self.__class__.__name__}({self.radius}, {math.degrees(self.angle):.1f})'

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

show_all_attr = dir(Circle)
print(f'Показывает все атрибуты и методы которые можно применить к объекту,\n'
      f'и которые были явным образом указаны внутри объекта - {show_all_attr}\n')

show_user_attr = Circle.__dict__
print(f'Показывает все атрибуты и методы, которые находятся внутри класса - {show_user_attr}')


circle_instance = Circle(3, 45)           # инициализируем экземпляр класса
human_read_output = str(circle_instance)  # с помощью функции str получаем человекочитаемый результат
print(human_read_output)


circle_instance_1 = Circle(4, 24)               # инициализируем экземпляр класса
machine_read_output = repr(circle_instance_1)   # с помощью функции repr получаем машиночитаемый результат
print(machine_read_output)

print(Circle.count_of_callings)
