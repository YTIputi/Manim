from manim import *

class TransformExample(Scene):
    def construct(self):
        text1 = Text("Hello")
        text2 = Text("World")
        self.add(text1)
        # Используем Transform для превращения текста "Hello" в "World"
        self.play(Transform(text1, text2))
