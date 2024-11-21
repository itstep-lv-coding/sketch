from figure import Figure

class Point(Figure):
    def __init__(self, x, y, color='blue'):
        super().__init__("Point", color=color)
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x},{self.y}, color={self.color})"

    def draw(self, scale=1, ax=None):
        #ax is the axis object from matplotlib. Цей об'єкт малює,
        # ми не можемо його тут створювати, оскільки він намалює тільки одну точку,
        # а наступна точка все стре і намалює себе заново
        # тому малювалка створює на рівні скеча і передається сюди, як і в інші фігури

        if ax:
            ax.plot(self.x * scale, self.y * scale, 'ro', label=f'Point({self.x},{self.y})', color=self.color)
            print(f"Drawing {self}")
        else:
            print(f"Could not drawing Point at ({self.x}, {self.y}) because ax is None")
