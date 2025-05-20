# Geometric Figures

Этот репозиторий содержит 3 директории. В каждой из них размещен класс, отвечающий за нахождение площади, периметра и прочих геометрических свойств фигур, указанных по названию класса соответственно. 
То есть class Rectangle соответствует фигуре "Прямоугольник" и содержит в себе функции отвечающие за выполнение вычислений ее геометрических свойств соответственно. 

Репозиторий носит учебный характер, был загружен в качестве домашнего задания для отработки базовых навыков программирования.

## 🚀 Особенности
**Содержит модуль Circle позволяющий производить следующие операции:**
- находить площадь окружности
- находить периметр окружности
- находить хорду окружности

**Пример использования кода:**
'''
find_circle_per = Circle(5)
show_circle_perimeter = find_circle_per.circle_perimeter().__round__(2)
print(show_circle_perimeter)

find_circle_area = Circle(5)
show_circle_perimeter = find_circle_area.circle_area()
print(round(show_circle_perimeter, 2))

find_chord = Circle(2, 40)
show_chord_length = find_chord.get_chord_length().__round__(2)
print(show_chord_length)
'''


## 📦 Установка

Как установить проект? Например:

```bash
git clone https://github.com/ваш-юзернейм/ваш-репозиторий.git
cd ваш-репозиторий
npm install  # или pip install -r requirements.txt, или другой менеджер пакетов
