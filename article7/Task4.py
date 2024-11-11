from manim import *

class ShapeStyles(Scene):
    def construct(self):
        circle = Circle(stroke_color=RED, stroke_width=6, fill_color=YELLOW, fill_opacity=0.5)
        square = Square(stroke_color=BLUE, stroke_width=4, fill_color=GREEN, fill_opacity=0.3)
        
        self.add(circle, square)
        self.play(circle.animate.shift(LEFT), square.animate.shift(RIGHT))
