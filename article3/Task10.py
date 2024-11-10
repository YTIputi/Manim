from manim import *


class FullAnimationExample(Scene):
    def construct(self):
        text = Text("Hello")
        circle = Circle()

        self.play(Write(text, run_time=2))
        self.play(Transform(text, circle, run_time=2, rate_func=smooth))
        self.play(FadeOut(text, run_time=2))