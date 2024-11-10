from manim import *

# class TransformExample(Scene):
#     def construct(self):
#         square = Square()
#         circle = Circle()
#         self.play(Transform(square, circle))

# class TransformVsReplacementTransform(Scene):
#     def construct(self):
#         text1 = Text("Hello")
#         text2 = Text("World")
        
#         # Попытка трансформировать `text1` в `text2` с помощью Transform
#         self.play(Transform(text1, text2))  # может выглядеть странно
        
#         self.wait(1)
        
#         text3 = Text("Replacement")

#         # Используем ReplacementTransform для плавного замещения `text2`
#         self.play(ReplacementTransform(text1, text3))  # более плавное замещение


class ApplyMethodExample(Scene):
    def construct(self):
        square = Square()
        self.play(ApplyMethod(square.shift, RIGHT * 2))
