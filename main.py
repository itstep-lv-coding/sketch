from sketch import Sketch
from real_figures.point import Point
from real_figures.line import Line
from real_figures.quadrilateral import Quadrilateral

def main():
    sketch = Sketch("My Scaled Sketch", description="A sketch with scaled axes")
    p1 = Point(1, 3)
    p2 = Point(3, 3)
    p3 = Point(2, 1)
    p4 = Point(5, 3)

    line = Line(p1, p2, color='red')
    line1 = Line(p3, p4, color='green')

    quad = Quadrilateral(Point(1,1), Point(1,5), Point(5,8), Point(8,1))

    sketch.add_figure(p1)
    sketch.add_figure(p2)
    sketch.add_figure(p3)
    sketch.add_figure(p4)
    sketch.add_figure(line)
    sketch.add_figure(line1)
    sketch.add_figure(quad)

    sketch.draw(scale=10)
    print(sketch)


if __name__ == '__main__':
    main()