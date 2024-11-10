from manim import *

class MultipleAnimationsExample(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        self.add(circle, square)
        
        # Перемещаем круг с помощью animate
        self.play(circle.animate.shift(UP * 2))
        
        # Трансформируем круг в квадрат с помощью Transform
        self.play(Transform(circle, square))
        
        # Поворачиваем квадрат с помощью ApplyMethod
        self.play(ApplyMethod(circle.rotate, PI / 2))
