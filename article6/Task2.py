from manim import *
import numpy as np

class ParametricSurfaceExample(ThreeDScene):
    def construct(self):
        # Определение параметрической функции поверхности
        surface = Surface(
            lambda u, v: np.array([
                u,
                v,
                np.sin(u) * np.cos(v)
            ]),
            u_range=[-3, 3],
            v_range=[-3, 3],
            resolution=(32, 32)
        )
        surface.set_color(BLUE)

        # Добавление поверхности на сцену
        self.add(surface)
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        self.begin_ambient_camera_rotation(rate=1)
        self.wait()
