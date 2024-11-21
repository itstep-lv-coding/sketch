from figure import Figure
from .point import Point

class Line(Figure):
    def __init__(self, start: Point, end: Point, color='green'):
        super().__init__("Line", color=color)
        self.start = start
        self.end = end

    def __str__(self):
        return f"Line ({self.start}-{self.end}, line color={self.color})"


    def draw(self, scale=1, ax=None):
        if ax:
            ax.plot(
                [self.start.x * scale, self.end.x * scale],
                [self.start.y * scale, self.end.y * scale],
                label=f'Line({self})',
                color=self.color
            )
        print(f"Drawing Line {self}, scale {scale}")
