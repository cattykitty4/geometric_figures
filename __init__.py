from .circle_core import Circle
from .rectangle_core import Rectangle
from .triangle_core import Triangle

__all__ = ('Circle', 'Rectangle', 'Triangle')
# from geometric_figures import *
# при таком импорте сработает переменная __all__
# которая импортирует только переданные в нее классы
