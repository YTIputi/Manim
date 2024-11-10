from manim import *


class SuccessionExample(Scene):
    def construct(self):
        square = Square()
        circle = Circle()
        self.play(Succession(GrowFromCenter(square), Transform(square, circle)))