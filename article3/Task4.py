from manim import *


class MoveToTargetExample(Scene):
    def construct(self):
        square = Square()
        square.target = square.copy().shift(RIGHT * 2)
        self.play(MoveToTarget(square))