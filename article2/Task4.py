from manim import *

class Photo(Scene):
    def construct(self):
        image = ImageMobject("/home/sb/Downloads/Manim/article2/photo_2024-11-08_00-42-16.jpg")
        image.scale(0.5)

        self.play(FadeIn(image))
        self.wait(1)
        self.play(Rotate(image, 45))