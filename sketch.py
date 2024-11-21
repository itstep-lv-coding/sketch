import matplotlib.pyplot as plt
from figure import Figure

class Sketch:
    def __init__(self, name, description=""):
        self.name = name
        self.description = description
        self.figures = []
        self.area = 0
        self.perimeter = 0

    def __str__(self):
        return f"Sketch {self.name}. I have {len(self.figures)} figures. My description is {self.description}. My area is {self.area}. My perimeter is {self.perimeter}"

    def draw(self, scale=1):
        plt.figure(figsize=(6, 6))
        ax = plt.gca()
        ax.set_aspect('equal', adjustable='box')
        for figure in self.figures:
            figure.draw(scale, ax)
        plt.title(self.name)
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.grid(True)
        plt.show()
        print(f"Drawing {self.name} finished, scale {scale}")

    def add_figure(self, figure):
        self.figures.append(figure)
        self.area += figure.area



