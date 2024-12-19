from figure import Figure
from .point import Point

class Circle(Figure):
    def __init__(self, centre: Point, radius: int, color='red'):
        super().__init__("Circle", color=color)
        self.centre = centre
        self.radius = radius

    def __str__(self):
        return f"Circle ({self.centre}-{self.radius}, line color={self.color})"


    def draw(self, scale=1, ax=None):
        # if ax:
        #     ax.plot(
        #         [self.start.x * scale, self.end.x * scale],
        #         [self.start.y * scale, self.end.y * scale],
        #         label=f'Line({self})',
        #         color=self.color
        #     )
        print(f"Drawing Circle {self}, scale {scale}")
