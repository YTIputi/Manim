from manim import *

class StandardColors(Scene):
    def construct(self):
        circle = Circle(color=BLUE)  # Используем стандартный цвет
        square = Square(color=YELLOW)
        
        self.add(circle, square)
        self.play(circle.animate.shift(LEFT), square.animate.shift(RIGHT))
