from manim import *


class Example(Scene):
    def construct(self):
        square = Square()
        for _ in range(10):
            square.target = square.copy().shift(2 * RIGHT)
            self.play(MoveToTarget(square, run_time=0.1))
            square.target = square.copy().shift(2 * LEFT)
            self.play(MoveToTarget(square, run_time=0.1))
        
        square.target = square.copy().shift(2 * RIGHT)
        self.play(MoveToTarget(square, rate_func=smooth))
        square.target = square.copy().shift(2 * LEFT)
        self.play(MoveToTarget(square, rate_func=there_and_back))