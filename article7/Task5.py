from manim import *

class TransparencyExample(Scene):
    def construct(self):
        circle = Circle(fill_color=BLUE, fill_opacity=0.3, stroke_color=RED, stroke_opacity=0.7)
        square = Square(fill_color=GREEN, fill_opacity=0.5, stroke_color=YELLOW, stroke_opacity=0.2)
        
        self.add(circle, square)
        self.play(circle.animate.shift(LEFT), square.animate.shift(RIGHT))
