# Geometric Figures

Этот репозиторий содержит 3 директории. В каждой из них размещен класс, отвечающий за нахождение площади, периметра и прочих геометрических свойств фигур, указанных по названию класса соответственно. 
То есть class Rectangle соответствует фигуре "Прямоугольник" и содержит в себе функции отвечающие за выполнение вычислений ее геометрических свойств соответственно. 

Репозиторий носит учебный характер, был загружен в качестве домашнего задания для отработки базовых навыков программирования.

## 🚀 Функционал репозитория

**Содержит модуль Circle позволяющий производить следующие операции:**
- находить площадь окружности `circle_area()`
- находить периметр окружности `circle_perimeter()`
- находить хорду окружности     `get_chord_length()`

**Содержит модуль Triangle, который:**
- выводит общую информацию о Треугольнике. Рассчитывает его периметр, полупериметр и площадь `get_basic_info()`
- позволяет находить высоту у треугольника `get_triangle_height(self)`

**Содержит модуль Rectangle позволяющий производить следующие операции:**
- находить площадь прямоугольника `get_rectangle_area()`
- находить периметр прямоугольника `get_rectangle_perimeter()`
- находить диагональ прямоугольника `get_rectangle_diagonal()`

## Примеры использования класса Circle с каждым методом класса
```bash
find_circle_per = Circle(5)
show_circle_perimeter = find_circle_per.circle_perimeter().__round__(2)
print(show_circle_perimeter)

find_circle_area = Circle(5)
show_circle_perimeter = find_circle_area.circle_area()
print(round(show_circle_perimeter, 2))

find_chord = Circle(2, 40)
show_chord_length = find_chord.get_chord_length().__round__(2)
print(show_chord_length)
```
## Примеры использования класса Triangle с каждым методом класса
```bash
get_info = Triangle(19, 20, 25)                  
show_info = get_info.get_basic_info()            
print(show_info)                                 

get_height = Triangle(10, 5, 8)                  
show_height = get_height.get_triangle_height()   
print(show_height)                              
```
## Примеры использования класса Rectangle с каждым методом класса
```bash
find_rec_area = Rectangle(4, 5)                                   
show_rec_area = find_rec_area.get_rectangle_area()                
print(f"Площадь прямоугольника: {show_rec_area}")                 

find_rec_perimeter = Rectangle(4, 5)                              
show_rec_perimeter = find_rec_perimeter.get_rectangle_perimeter() 
print(f"Периметр прямоугольника: {show_rec_perimeter}")           

find_rec_diagonal = Rectangle(4, 5)                               
show_rec_diagonal = find_rec_diagonal.get_rectangle_diagonal()    
print(f"Диагональ прямоугольника: {show_rec_diagonal:.2f}")       
```

## 📦 Установка
 Клонируйте репозиторий:
   ```bash
   git clone https://github.com/cattykitty4/geometric_figures.git

