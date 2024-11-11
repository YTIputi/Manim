import pandas as pd
from manim import *

class DataFrameVisualization(Scene):
    def construct(self):
        # Создаем DataFrame
        data = {'X': [1, 2, 3, 4, 5], 'Y': [2, 4, 6, 8, 10]}
        df = pd.DataFrame(data)

        # Создаем оси для визуализации данных
        axes = Axes(x_range=[0, 6], y_range=[0, 12], axis_config={"color": BLUE})
        
        # Визуализируем данные как точки
        points = [
            axes.c2p(x, y) for x, y in zip(df['X'], df['Y'])
        ]
        dots = VGroup(*[Dot(point) for point in points])

        # Отображаем оси и точки
        self.play(Create(axes), Create(dots))
