from manim import *

class GrowExample(Scene):
    def construct(self):
        circle = Circle()
        text = Text("HUY")
        self.play(GrowFromCenter(text))

