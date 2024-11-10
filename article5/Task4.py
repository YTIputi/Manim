from manim import *

class AdvancedAnimation(Scene):
    def construct(self):
        square = Square().set_color(BLUE)
        circle = Circle().set_color(RED).shift(RIGHT * 4)

        # Движение с интерполяцией
        self.play(square.animate.shift(RIGHT * 4), rate_func=smooth)
        
        # Трансформация квадрата в круг
        self.play(ReplacementTransform(square, circle))

        # Функция для динамического изменения размера
        def grow_circle(mob, dt):
            mob.scale(1 + dt).shift(-dt * 2 * RIGHT)

        circle.add_updater(grow_circle)

        # Короткая пауза, чтобы видеть изменение круга
        self.wait(2)
        circle.remove_updater(grow_circle)
