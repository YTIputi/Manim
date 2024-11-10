from manim import *

class LaggedStartExample(Scene):
    def construct(self):
        # squares = VGroup(*[Square(side_length=0.5).shift(i * RIGHT) for i in range(1, 6)])
        # squares1 = VGroup(*[Square(side_length=0.5).shift(i * RIGHT).shift(DOWN) for i in range(1, 6)])
        # self.play(Succession(LaggedStart(*[Create(square) for square in squares])), 
        #           LaggedStart(*[Create(square) for square in squares1]))

        for j in range(3):
            squares = VGroup(*[Square(side_length=0.5).shift(i * RIGHT).shift(j * DOWN) for i in range(1, 6)])
            self.play(LaggedStart(*[Create(square) for square in squares]))
