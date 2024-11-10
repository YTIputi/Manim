from manim import *

class InterpolationExample(Scene):
    def construct(self):
        square = Square()
        self.play(square.animate.shift(RIGHT * 4), rate_func=smooth)
        self.play(square.animate.shift(LEFT * 4), rate_func=linear)
