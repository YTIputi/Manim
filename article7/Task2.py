from manim import *

class CustomColors(Scene):
    def construct(self):
        circle = Circle(color=rgb_to_color((0.2, 0.4, 0.6)), fill_opacity=0.5)  # Используем rgb_to_color для RGB
        square = Square(color=rgb_to_color((0.5, 0.2, 0.8, 0.5)), fill_opacity=0.5)  # Встроенная поддержка прозрачности

        self.add(circle, square)
        self.play(circle.animate.shift(LEFT), square.animate.shift(RIGHT))

