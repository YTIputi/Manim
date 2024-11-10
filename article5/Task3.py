from manim import *

class UpdaterExample(Scene):
    def construct(self):
        square = Square().shift(LEFT * 3)
        circle = Circle().shift(RIGHT * 3)

        # Функция для следования за квадратом
        def follow_square(mob):
            mob.move_to(square.get_center() - LEFT * 2)

        # Добавляем обновление к кругу
        circle.add_updater(follow_square)

        # Анимация перемещения квадрата
        self.add(square, circle)
        self.play(square.animate.shift(RIGHT * 6), run_time=4)
        circle.remove_updater(follow_square)  # Удаление updater, чтобы прекратить обновление
