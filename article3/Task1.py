from manim import *

class FadeExample(Scene):
    def construct(self):
        text = Text("Hello")
        self.play(FadeIn(text))
        self.wait()
        self.play(FadeOut(text))