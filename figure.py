class  Figure:
    def __init__(self, name, description="", color='blue'):
        self.name = name
        self.area = 0
        self.perimeter = 0
        self.color=color
        self.description = description

    def __str__(self):
        return f"Figure {self.name}"

    def draw(self, scale=1, ax=None):
        print(f"!!!!! YOU MUST REALIZE Drawing Figure:{self.name}, scale {scale}")

    def calculate_area(self):
        print(f"!!!!! YOU MUST REALIZE calculate_area for Figure:{self.name}")

    def calculate_perimeter(self):
        print(f"!!!!! YOU MUST REALIZE calculate_perimeter for Figure:{self.name}")
