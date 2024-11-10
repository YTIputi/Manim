from manim import *

class WriteExample(Scene):
    def construct(self):
        text = Text("Write")
        self.play(Write(text))
        