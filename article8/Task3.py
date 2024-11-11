from manim import *


class ExampleAxes(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-5, 5],
            y_range=[-5, 5],
            axis_config={"color": WHITE}
        )
        number_plane = NumberPlane(
            x_range=[-5, 5], 
            y_range=[-5, 5],
            axis_config={"stroke_color": BLUE}
        )

        self.play(Succession(Create(number_plane), Create(axes)))


# class MovingVertices(Scene):
#     def construct(self):
#         vertices = [1, 2, 3, 4]
#         edges = [(1, 2), (2, 3), (3, 4), (1, 3), (1, 4)]
#         g = Graph(vertices, edges)
#         self.play(Create(g))
#         self.wait()
#         self.play(g[1].animate.move_to([3, 1, 0]),
#                     g[2].animate.move_to([-1, 4, 0]),
#                     g[3].animate.move_to([2, -1, 0]),
#                     g[4].animate.move_to([-1, 0, 0]))
#         self.wait()
