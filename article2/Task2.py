from manim import *


class TextManim(Scene):
    def construct(self):
        text = Text("2 + 2 = 4")
        math_tex = MathTex(r"\frac{d}{dx} e^x = e^x")
        math_tex1 = MathTex(r"e^{i \pi} + 1 = 0")

        self.play(Write(text))
        self.play(FadeOut(text))
        self.play(Write(math_tex))
        self.play(FadeOut(math_tex))
        self.play(Write(math_tex1))
        self.play(FadeOut(math_tex1))
        self.play(FadeIn(Text("Сосал?")))
        self.wait(0.1)