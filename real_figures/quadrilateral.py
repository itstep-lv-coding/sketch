from figure import Figure
from .point import Point

class Quadrilateral(Figure):
    def __init__(self, p1: Point, p2: Point, p3: Point, p4: Point):
        super().__init__('Quadrilateral')
        self.points = [p1, p2, p3, p4]

    def __str__(self):
        return f"Quadrilateral({self.points[0]},{self.points[1]},{self.points[2]},{self.points[3]}), color={self.color}"

    def draw(self, scale=1, ax=None):
        if ax:
            x = [p.x * scale for p in self.points] + [self.points[0].x * scale]
            y = [p.y * scale for p in self.points] + [self.points[0].y * scale]
            ax.plot(x, y, label=f'Quadrilateral')
        print(f"Drawing {self}, scale {scale}")
