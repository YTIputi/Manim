from manim import *

class CircleScene(Scene):
    def construct(self):
        # Создаем круг
        circle = Circle()
        circle.set_fill(RED, opacity=0.5)  # Устанавливаем цвет заливки и прозрачность
        circle.set_stroke(RED, width=10)    # Устанавливаем цвет обводки и ширину
        circle.shift(LEFT).scale(1)      # Сдвиг и масштабирование круга
        self.play(Create(circle))          # Анимация создания круга
        self.wait()