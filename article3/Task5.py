from manim import *


class TransformExample(Scene):
    def construct(self):
        square = Square()
        circle = Circle()
        self.play(Transform(square, circle))